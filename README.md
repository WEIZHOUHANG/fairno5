
ljw2@DESKTOP-OG671DC:~/fairno5$ ros2 launch fairino5_v6_moveit2_config demo.launch.py
[INFO] [launch]: All log files can be found below /home/ljw2/.ros/log/2026-02-02-09-53-00-990892-DESKTOP-OG671DC-11287
[INFO] [launch]: Default logging verbosity is set to INFO
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
Using load_yaml() directly is deprecated. Use xacro.load_yaml() instead.
[INFO] [robot_state_publisher-1]: process started with pid [11296]
[INFO] [move_group-2]: process started with pid [11298]
[INFO] [rviz2-3]: process started with pid [11300]
[INFO] [ros2_control_node-4]: process started with pid [11302]
[INFO] [spawner-5]: process started with pid [11304]
[INFO] [spawner-6]: process started with pid [11306]
[INFO] [spawner-7]: process started with pid [11308]
[robot_state_publisher-1] [WARN] [1769997181.565682956] [kdl_parser]: The root link base_link has an inertia specified in the URDF, but KDL does not support a root link with an inertia.  As a workaround, you can add an extra dummy link to your URDF.
[robot_state_publisher-1] [INFO] [1769997181.565768921] [robot_state_publisher]: got segment base_link
[robot_state_publisher-1] [INFO] [1769997181.565809786] [robot_state_publisher]: got segment camera_link
[robot_state_publisher-1] [INFO] [1769997181.565815003] [robot_state_publisher]: got segment camera_optical_link
[robot_state_publisher-1] [INFO] [1769997181.565817516] [robot_state_publisher]: got segment forearm_link
[robot_state_publisher-1] [INFO] [1769997181.565819687] [robot_state_publisher]: got segment left_inner_finger
[robot_state_publisher-1] [INFO] [1769997181.565821871] [robot_state_publisher]: got segment left_inner_finger_pad
[robot_state_publisher-1] [INFO] [1769997181.565824494] [robot_state_publisher]: got segment left_inner_knuckle
[robot_state_publisher-1] [INFO] [1769997181.565826901] [robot_state_publisher]: got segment left_outer_finger
[robot_state_publisher-1] [INFO] [1769997181.565828911] [robot_state_publisher]: got segment left_outer_knuckle
[robot_state_publisher-1] [INFO] [1769997181.565830952] [robot_state_publisher]: got segment right_inner_finger
[robot_state_publisher-1] [INFO] [1769997181.565832929] [robot_state_publisher]: got segment right_inner_finger_pad
[robot_state_publisher-1] [INFO] [1769997181.565835065] [robot_state_publisher]: got segment right_inner_knuckle
[robot_state_publisher-1] [INFO] [1769997181.565837093] [robot_state_publisher]: got segment right_outer_finger
[robot_state_publisher-1] [INFO] [1769997181.565839050] [robot_state_publisher]: got segment right_outer_knuckle
[robot_state_publisher-1] [INFO] [1769997181.565841085] [robot_state_publisher]: got segment robotiq_arg2f_base_link
[robot_state_publisher-1] [INFO] [1769997181.565843203] [robot_state_publisher]: got segment shoulder_link
[robot_state_publisher-1] [INFO] [1769997181.565845280] [robot_state_publisher]: got segment tool_link
[robot_state_publisher-1] [INFO] [1769997181.565847335] [robot_state_publisher]: got segment upperarm_link
[robot_state_publisher-1] [INFO] [1769997181.565849337] [robot_state_publisher]: got segment wrist1_link
[robot_state_publisher-1] [INFO] [1769997181.565851360] [robot_state_publisher]: got segment wrist2_link
[robot_state_publisher-1] [INFO] [1769997181.565853425] [robot_state_publisher]: got segment wrist3_link
[ros2_control_node-4] [WARN] [1769997181.582469962] [controller_manager]: [Deprecated] Passing the robot description parameter directly to the control_manager node is deprecated. Use '~/robot_description' topic from 'robot_state_publisher' instead.
[ros2_control_node-4] [INFO] [1769997181.582759116] [resource_manager]: Loading hardware 'FakeSystem'
[ros2_control_node-4] [INFO] [1769997181.584409425] [resource_manager]: Initialize hardware 'FakeSystem'
[ros2_control_node-4] [INFO] [1769997181.584476015] [resource_manager]: Successful initialization of hardware 'FakeSystem'
[ros2_control_node-4] [INFO] [1769997181.584509328] [resource_manager]: 'configure' hardware 'FakeSystem'
[ros2_control_node-4] [INFO] [1769997181.584514122] [resource_manager]: Successful 'configure' of hardware 'FakeSystem'
[ros2_control_node-4] [INFO] [1769997181.584517558] [resource_manager]: 'activate' hardware 'FakeSystem'
[ros2_control_node-4] [INFO] [1769997181.584520956] [resource_manager]: Successful 'activate' of hardware 'FakeSystem'
[ros2_control_node-4] [INFO] [1769997181.591798782] [controller_manager]: update rate is 100 Hz
[ros2_control_node-4] [INFO] [1769997181.591830752] [controller_manager]: Spawning controller_manager RT thread with scheduler priority: 50
[ros2_control_node-4] [WARN] [1769997181.591914289] [controller_manager]: Could not enable FIFO RT scheduling policy: with error number <1>(Operation not permitted). See [https://control.ros.org/master/doc/ros2_control/controller_manager/doc/userdoc.html] for details on how to enable realtime scheduling.
[move_group-2] [INFO] [1769997181.602334254] [moveit_rdf_loader.rdf_loader]: Loaded robot model in 0.00202478 seconds
[move_group-2] [INFO] [1769997181.602389980] [moveit_robot_model.robot_model]: Loading robot model 'fairino5_v6_robot'...
[move_group-2] [INFO] [1769997181.602394901] [moveit_robot_model.robot_model]: No root/virtual joint specified in SRDF. Assuming fixed joint
[move_group-2] [WARN] [1769997181.673501130] [kdl_parser]: The root link base_link has an inertia specified in the URDF, but KDL does not support a root link with an inertia.  As a workaround, you can add an extra dummy link to your URDF.
[move_group-2] [INFO] [1769997181.825608898] [moveit_ros.planning_scene_monitor.planning_scene_monitor]: Publishing maintained planning scene on 'monitored_planning_scene'
[move_group-2] [INFO] [1769997181.825891217] [moveit.ros_planning_interface.moveit_cpp]: Listening to 'joint_states' for joint states
[move_group-2] [INFO] [1769997181.826794849] [moveit_ros.current_state_monitor]: Listening to joint states on topic 'joint_states'
[move_group-2] [INFO] [1769997181.827313645] [moveit_ros.planning_scene_monitor.planning_scene_monitor]: Listening to '/attached_collision_object' for attached collision objects
[move_group-2] [INFO] [1769997181.827370007] [moveit_ros.planning_scene_monitor.planning_scene_monitor]: Starting planning scene monitor
[move_group-2] [INFO] [1769997181.828045245] [moveit_ros.planning_scene_monitor.planning_scene_monitor]: Listening to '/planning_scene'
[move_group-2] [INFO] [1769997181.828071085] [moveit_ros.planning_scene_monitor.planning_scene_monitor]: Starting world geometry update monitor for collision objects, attached objects, octomap updates.
[move_group-2] [INFO] [1769997181.828481367] [moveit_ros.planning_scene_monitor.planning_scene_monitor]: Listening to 'collision_object'
[move_group-2] [INFO] [1769997181.828955884] [moveit_ros.planning_scene_monitor.planning_scene_monitor]: Listening to 'planning_scene_world' for planning scene world geometry
[move_group-2] [WARN] [1769997181.829102733] [moveit.ros.occupancy_map_monitor.middleware_handle]: Resolution not specified for Octomap. Assuming resolution = 0.1 instead
[move_group-2] [ERROR] [1769997181.829113734] [moveit.ros.occupancy_map_monitor.middleware_handle]: No 3D sensor plugin(s) defined for octomap updates
[ros2_control_node-4] [INFO] [1769997181.843443853] [controller_manager]: Loading controller 'joint_state_broadcaster'
[ros2_control_node-4] [INFO] [1769997181.862445092] [controller_manager]: Loading controller 'fairino5_controller'
[spawner-7] [INFO] [1769997181.870124101] [spawner_joint_state_broadcaster]: Loaded joint_state_broadcaster
[ros2_control_node-4] [WARN] [1769997181.878777586] [fairino5_controller]: [Deprecated]: "allow_nonzero_velocity_at_trajectory_end" is set to true. The default behavior will change to false.
[move_group-2] [INFO] [1769997181.882249176] [moveit.ros_planning_interface.moveit_cpp]: Loading planning pipeline 'ompl'
[ros2_control_node-4] [INFO] [1769997181.882737538] [controller_manager]: Configuring controller 'joint_state_broadcaster'
[ros2_control_node-4] [INFO] [1769997181.882879857] [joint_state_broadcaster]: 'joints' or 'interfaces' parameter is empty. All available state interfaces will be published
[spawner-5] [INFO] [1769997181.890140470] [spawner_fairino5_controller]: Loaded fairino5_controller
[ros2_control_node-4] [INFO] [1769997181.892448952] [controller_manager]: Configuring controller 'fairino5_controller'
[ros2_control_node-4] [INFO] [1769997181.892573195] [fairino5_controller]: No specific joint names are used for command interfaces. Using 'joints' parameter.
[ros2_control_node-4] [INFO] [1769997181.892586901] [fairino5_controller]: Command interfaces are [position] and state interfaces are [position].
[ros2_control_node-4] [INFO] [1769997181.892603685] [fairino5_controller]: Using 'splines' interpolation method.
[ros2_control_node-4] [INFO] [1769997181.893125131] [fairino5_controller]: Controller state will be published at 50.00 Hz.
[ros2_control_node-4] [INFO] [1769997181.894709371] [fairino5_controller]: Action status changes will be monitored at 20.00 Hz.
[move_group-2] [INFO] [1769997181.910760032] [moveit.ros_planning.planning_pipeline]: Using planning interface 'OMPL'
[move_group-2] [INFO] [1769997181.914556466] [moveit_ros.add_time_optimal_parameterization]: Param 'ompl.path_tolerance' was not set. Using default value: 0.100000
[move_group-2] [INFO] [1769997181.914584062] [moveit_ros.add_time_optimal_parameterization]: Param 'ompl.resample_dt' was not set. Using default value: 0.100000
[move_group-2] [INFO] [1769997181.914587452] [moveit_ros.add_time_optimal_parameterization]: Param 'ompl.min_angle_change' was not set. Using default value: 0.001000
[move_group-2] [INFO] [1769997181.914599138] [moveit_ros.fix_workspace_bounds]: Param 'ompl.default_workspace_bounds' was not set. Using default value: 10.000000
[move_group-2] [INFO] [1769997181.914608022] [moveit_ros.fix_start_state_bounds]: Param 'ompl.start_state_max_bounds_error' was set to 0.100000
[move_group-2] [INFO] [1769997181.914610646] [moveit_ros.fix_start_state_bounds]: Param 'ompl.start_state_max_dt' was not set. Using default value: 0.500000
[move_group-2] [INFO] [1769997181.914616132] [moveit_ros.fix_start_state_collision]: Param 'ompl.start_state_max_dt' was not set. Using default value: 0.500000
[move_group-2] [INFO] [1769997181.914618702] [moveit_ros.fix_start_state_collision]: Param 'ompl.jiggle_fraction' was set to 0.050000
[move_group-2] [INFO] [1769997181.914621526] [moveit_ros.fix_start_state_collision]: Param 'ompl.max_sampling_attempts' was not set. Using default value: 100
[move_group-2] [INFO] [1769997181.914627093] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Add Time Optimal Parameterization'
[move_group-2] [INFO] [1769997181.914629242] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Resolve constraint frames to robot links'
[move_group-2] [INFO] [1769997181.914630773] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Fix Workspace Bounds'
[move_group-2] [INFO] [1769997181.914632363] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Fix Start State Bounds'
[move_group-2] [INFO] [1769997181.914654185] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Fix Start State In Collision'
[move_group-2] [INFO] [1769997181.914655837] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Fix Start State Path Constraints'
[move_group-2] [INFO] [1769997181.917028614] [moveit.ros_planning_interface.moveit_cpp]: Loading planning pipeline 'chomp'
[spawner-7] [INFO] [1769997181.922952983] [spawner_joint_state_broadcaster]: Configured and activated joint_state_broadcaster
[move_group-2] [INFO] [1769997181.926518351] [moveit.ros_planning.planning_pipeline]: Using planning interface 'CHOMP'
[move_group-2] [INFO] [1769997181.927044243] [moveit_ros.add_time_optimal_parameterization]: Param 'chomp.path_tolerance' was not set. Using default value: 0.100000
[move_group-2] [INFO] [1769997181.927062366] [moveit_ros.add_time_optimal_parameterization]: Param 'chomp.resample_dt' was not set. Using default value: 0.100000
[move_group-2] [INFO] [1769997181.927065101] [moveit_ros.add_time_optimal_parameterization]: Param 'chomp.min_angle_change' was not set. Using default value: 0.001000
[move_group-2] [INFO] [1769997181.927076665] [moveit_ros.fix_workspace_bounds]: Param 'chomp.default_workspace_bounds' was not set. Using default value: 10.000000
[move_group-2] [INFO] [1769997181.927083997] [moveit_ros.fix_start_state_bounds]: Param 'chomp.start_state_max_bounds_error' was set to 0.100000
[move_group-2] [INFO] [1769997181.927086430] [moveit_ros.fix_start_state_bounds]: Param 'chomp.start_state_max_dt' was not set. Using default value: 0.500000
[move_group-2] [INFO] [1769997181.927091914] [moveit_ros.fix_start_state_collision]: Param 'chomp.start_state_max_dt' was not set. Using default value: 0.500000
[move_group-2] [INFO] [1769997181.927094507] [moveit_ros.fix_start_state_collision]: Param 'chomp.jiggle_fraction' was set to 0.050000
[move_group-2] [INFO] [1769997181.927096637] [moveit_ros.fix_start_state_collision]: Param 'chomp.max_sampling_attempts' was not set. Using default value: 100
[move_group-2] [INFO] [1769997181.927101764] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Add Time Optimal Parameterization'
[move_group-2] [INFO] [1769997181.927103793] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Resolve constraint frames to robot links'
[move_group-2] [INFO] [1769997181.927105304] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Fix Workspace Bounds'
[move_group-2] [INFO] [1769997181.927106831] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Fix Start State Bounds'
[move_group-2] [INFO] [1769997181.927108302] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Fix Start State In Collision'
[move_group-2] [INFO] [1769997181.927109743] [moveit.ros_planning.planning_pipeline]: Using planning request adapter 'Fix Start State Path Constraints'
[move_group-2] [INFO] [1769997181.927709870] [moveit.ros_planning_interface.moveit_cpp]: Loading planning pipeline 'pilz_industrial_motion_planner'
[move_group-2] [INFO] [1769997181.931290050] [moveit.pilz_industrial_motion_planner.joint_limits_aggregator]: Reading limits from namespace robot_description_planning
[move_group-2] [INFO] [1769997181.935041534] [moveit.pilz_industrial_motion_planner]: Available plugins: pilz_industrial_motion_planner/PlanningContextLoaderCIRC pilz_industrial_motion_planner/PlanningContextLoaderLIN pilz_industrial_motion_planner/PlanningContextLoaderPTP
[move_group-2] [INFO] [1769997181.935070756] [moveit.pilz_industrial_motion_planner]: About to load: pilz_industrial_motion_planner/PlanningContextLoaderCIRC
[move_group-2] [INFO] [1769997181.937527462] [moveit.pilz_industrial_motion_planner]: Registered Algorithm [CIRC]
[move_group-2] [INFO] [1769997181.937554332] [moveit.pilz_industrial_motion_planner]: About to load: pilz_industrial_motion_planner/PlanningContextLoaderLIN
[move_group-2] [INFO] [1769997181.938798427] [moveit.pilz_industrial_motion_planner]: Registered Algorithm [LIN]
[move_group-2] [INFO] [1769997181.938822964] [moveit.pilz_industrial_motion_planner]: About to load: pilz_industrial_motion_planner/PlanningContextLoaderPTP
[move_group-2] [INFO] [1769997181.940162093] [moveit.pilz_industrial_motion_planner]: Registered Algorithm [PTP]
[move_group-2] [INFO] [1769997181.940188689] [moveit.ros_planning.planning_pipeline]: Using planning interface 'Pilz Industrial Motion Planner'
[ros2_control_node-4] [INFO] [1769997181.942470954] [controller_manager]: Loading controller 'gripper_controller'
[spawner-5] [INFO] [1769997181.942910953] [spawner_fairino5_controller]: Configured and activated fairino5_controller
[ros2_control_node-4] [WARN] [1769997181.951700796] [gripper_controller]: [Deprecated]: "allow_nonzero_velocity_at_trajectory_end" is set to true. The default behavior will change to false.
[spawner-6] [INFO] [1769997181.960081822] [spawner_gripper_controller]: Loaded gripper_controller
[ros2_control_node-4] [INFO] [1769997181.960978614] [controller_manager]: Configuring controller 'gripper_controller'
[ros2_control_node-4] [INFO] [1769997181.961059235] [gripper_controller]: No specific joint names are used for command interfaces. Using 'joints' parameter.
[ros2_control_node-4] [INFO] [1769997181.961071085] [gripper_controller]: Command interfaces are [position] and state interfaces are [position].
[ros2_control_node-4] [INFO] [1769997181.961077216] [gripper_controller]: Using 'splines' interpolation method.
[ros2_control_node-4] [INFO] [1769997181.961729102] [gripper_controller]: Controller state will be published at 50.00 Hz.
[ros2_control_node-4] [INFO] [1769997181.963046309] [gripper_controller]: Action status changes will be monitored at 20.00 Hz.
[move_group-2] [INFO] [1769997181.972807887] [moveit.plugins.moveit_simple_controller_manager]: Added FollowJointTrajectory controller for fairino5_controller
[move_group-2] [INFO] [1769997181.974312527] [moveit.plugins.moveit_simple_controller_manager]: Added FollowJointTrajectory controller for gripper_controller
[move_group-2] [INFO] [1769997181.974461978] [moveit.plugins.moveit_simple_controller_manager]: Returned 2 controllers in list
[move_group-2] [INFO] [1769997181.974480900] [moveit.plugins.moveit_simple_controller_manager]: Returned 2 controllers in list
[move_group-2] [INFO] [1769997181.974794042] [moveit_ros.trajectory_execution_manager]: Trajectory execution is managing controllers
[move_group-2] [INFO] [1769997181.974813297] [move_group.move_group]: MoveGroup debug mode is ON
[move_group-2] [INFO] [1769997181.991381328] [move_group.move_group]:
[move_group-2]
[move_group-2] ********************************************************
[move_group-2] * MoveGroup using:
[move_group-2] *     - ApplyPlanningSceneService
[move_group-2] *     - ClearOctomapService
[move_group-2] *     - CartesianPathService
[move_group-2] *     - ExecuteTrajectoryAction
[move_group-2] *     - GetPlanningSceneService
[move_group-2] *     - KinematicsService
[move_group-2] *     - MoveAction
[move_group-2] *     - MotionPlanService
[move_group-2] *     - QueryPlannersService
[move_group-2] *     - StateValidationService
[move_group-2] ********************************************************
[move_group-2]
[move_group-2] [INFO] [1769997181.991417276] [moveit_move_group_capabilities_base.move_group_context]: MoveGroup context using planning plugin ompl_interface/OMPLPlanner
[move_group-2] [INFO] [1769997181.991421960] [moveit_move_group_capabilities_base.move_group_context]: MoveGroup context initialization complete
[move_group-2] Loading 'move_group/ApplyPlanningSceneService'...
[move_group-2] Loading 'move_group/ClearOctomapService'...
[move_group-2] Loading 'move_group/MoveGroupCartesianPathService'...
[move_group-2] Loading 'move_group/MoveGroupExecuteTrajectoryAction'...
[move_group-2] Loading 'move_group/MoveGroupGetPlanningSceneService'...
[move_group-2] Loading 'move_group/MoveGroupKinematicsService'...
[move_group-2] Loading 'move_group/MoveGroupMoveAction'...
[move_group-2] Loading 'move_group/MoveGroupPlanService'...
[move_group-2] Loading 'move_group/MoveGroupQueryPlannersService'...
[move_group-2] Loading 'move_group/MoveGroupStateValidationService'...
[move_group-2]
[move_group-2] You can start planning now!
[move_group-2]
[spawner-6] [INFO] [1769997181.992845907] [spawner_gripper_controller]: Configured and activated gripper_controller
[INFO] [spawner-7]: process has finished cleanly [pid 11308]
[INFO] [spawner-5]: process has finished cleanly [pid 11304]
[INFO] [spawner-6]: process has finished cleanly [pid 11306]
[rviz2-3] [INFO] [1769997183.315570683] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-3] [INFO] [1769997183.315651927] [rviz2]: OpenGl version: 4.1 (GLSL 4.1)
[rviz2-3] [INFO] [1769997183.540280037] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-3] Warning: class_loader.impl: SEVERE WARNING!!! A namespace collision has occurred with plugin factory for class rviz_default_plugins::displays::InteractiveMarkerDisplay. New factory will OVERWRITE existing one. This situation occurs when libraries containing plugins are directly linked against an executable (the one running right now generating this message). Please separate plugins out into their own library or just don't link against the library and use either class_loader::ClassLoader/MultiLibraryClassLoader to open.
[rviz2-3]          at line 253 in /opt/ros/humble/include/class_loader/class_loader/class_loader_core.hpp
[rviz2-3] [ERROR] [1769997186.624857204] [moveit_ros_visualization.motion_planning_frame]: Action server: /recognize_objects not available
