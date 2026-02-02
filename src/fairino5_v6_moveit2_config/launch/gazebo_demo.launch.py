import os
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    OpaqueFunction,
    RegisterEventHandler,
)
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import xacro


def generate_launch_description():
    
    declared_arguments = []
    
    declared_arguments.append(
        DeclareLaunchArgument(
            "rviz_config",
            default_value="moveit.rviz",
            description="RViz configuration file",
        )
    )
    
    declared_arguments.append(
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="true",
            description="Use simulation time",
        )
    )
    
    declared_arguments.append(
        DeclareLaunchArgument(
            "world",
            default_value="empty.sdf",
            description="Gazebo world file",
        )
    )

    return LaunchDescription(
        declared_arguments + [OpaqueFunction(function=launch_setup)]
    )


def launch_setup(context, *args, **kwargs):
    
    use_sim_time = LaunchConfiguration("use_sim_time")
    rviz_config = LaunchConfiguration("rviz_config")
    world = LaunchConfiguration("world")
    
    # Package Directories
    pkg_fairino_description = get_package_share_directory("fairino_description")
    pkg_moveit_config = get_package_share_directory("fairino5_v6_moveit2_config")
    
    # Robot Description
    xacro_file = os.path.join(
        pkg_fairino_description,
        "urdf",
        "fairino5_v6_robot.urdf.xacro"
    )
    
    robot_description_config = xacro.process_file(
        xacro_file,
        mappings={
            "use_fake_hardware": "false",
            "use_gazebo": "true",
            "initial_positions_file": os.path.join(
                pkg_moveit_config, "config", "initial_positions.yaml"
            ),
        },
    )
    robot_description = {"robot_description": robot_description_config.toxml()}
    
    # Robot Description Semantic (SRDF)
    srdf_file = os.path.join(pkg_moveit_config, "config", "fairino5_v6_robot.srdf")
    with open(srdf_file, "r") as file:
        robot_description_semantic = {"robot_description_semantic": file.read()}
    
    # Kinematics
    kinematics_file = os.path.join(
        pkg_moveit_config, "config", "kinematics.yaml"
    )
    
    # Planning Pipeline
    ompl_planning_pipeline_config = {
        "move_group": {
            "planning_plugin": "ompl_interface/OMPLPlanner",
            "request_adapters": "default_planner_request_adapters/AddTimeOptimalParameterization "
                              "default_planner_request_adapters/ResolveConstraintFrames "
                              "default_planner_request_adapters/FixWorkspaceBounds "
                              "default_planner_request_adapters/FixStartStateBounds "
                              "default_planner_request_adapters/FixStartStateCollision "
                              "default_planner_request_adapters/FixStartStatePathConstraints",
            "start_state_max_bounds_error": 0.1,
        }
    }
    
    ompl_planning_yaml = os.path.join(
        pkg_moveit_config, "config", "ompl_planning.yaml"
    )
    
    # Controllers
    ros2_controllers_path = os.path.join(
        pkg_moveit_config, "config", "ros2_controllers.yaml"
    )
    
    moveit_controllers_path = os.path.join(
        pkg_moveit_config, "config", "moveit_controllers.yaml"
    )
    
    # Gazebo Launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("ros_gz_sim"), "/launch", "/gz_sim.launch.py"]
        ),
        launch_arguments={"gz_args": world}.items(),
    )
    
    # Robot State Publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[
            robot_description,
            {"use_sim_time": use_sim_time},
        ],
    )
    
    # Spawn Robot in Gazebo
    spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic", "robot_description",
            "-name", "fairino5_v6_robot",
            "-allow_renaming", "true",
            "-z", "0.1",
        ],
        output="screen",
    )
    
    # Joint State Broadcaster
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager", "/controller_manager",
        ],
    )
    
    # Arm Controller
    arm_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "fairino5_controller",
            "--controller-manager", "/controller_manager",
        ],
    )
    
    # Gripper Controller
    gripper_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "gripper_controller",
            "--controller-manager", "/controller_manager",
        ],
    )
    
    # Delay controllers
    delay_arm_controller = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[arm_controller_spawner],
        )
    )
    
    delay_gripper_controller = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=arm_controller_spawner,
            on_exit=[gripper_controller_spawner],
        )
    )
    
    # Move Group Node
    move_group_params = [
        robot_description,
        robot_description_semantic,
        kinematics_file,
        ompl_planning_pipeline_config,
        ompl_planning_yaml,
        moveit_controllers_path,
        {"use_sim_time": use_sim_time},
    ]
    
    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=move_group_params,
    )
    
    # RViz
    rviz_config_file = os.path.join(pkg_moveit_config, "config", rviz_config.perform(context))
    
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
        parameters=[
            robot_description,
            robot_description_semantic,
            ompl_planning_pipeline_config,
            kinematics_file,
            {"use_sim_time": use_sim_time},
        ],
    )
    
    # Clock Bridge
    clock_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=["/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock"],
        output="screen",
    )
    
    nodes_to_start = [
        gazebo,
        robot_state_publisher,
        spawn_entity,
        joint_state_broadcaster_spawner,
        delay_arm_controller,
        delay_gripper_controller,
        move_group_node,
        rviz_node,
        clock_bridge,
    ]
    
    return nodes_to_start
