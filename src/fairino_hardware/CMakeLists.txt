cmake_minimum_required(VERSION 3.8)
project(fairino_hardware)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic -fPIC -g -ggdb3)
endif()

# 设置编译模式为 Release 提高性能
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_STANDARD 17)

# --- 查找依赖 ---
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(hardware_interface REQUIRED)
find_package(pluginlib REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(fairino_msgs REQUIRED)

# --- 设置源码变量 ---
file(GLOB SRC_DIR ./src/command_server.cpp ./src/command_server_node.cpp)
file(GLOB EXP_SRC_DIR ./examples/src/*.cpp)

# --- 编译前在源码目录创建软链接 (可选，用于本地调试) ---
file(CREATE_LINK 
"${CMAKE_CURRENT_SOURCE_DIR}/libfairino/lib/libfairino.so.2.1.4"
"${CMAKE_CURRENT_SOURCE_DIR}/libfairino/lib/libfairino.so.2"
SYMBOLIC)

file(CREATE_LINK 
"${CMAKE_CURRENT_SOURCE_DIR}/libfairino/lib/libfairino.so.2"
"${CMAKE_CURRENT_SOURCE_DIR}/libfairino/lib/libfairino.so"
SYMBOLIC)

# --- 定义生成目标 ---
add_executable(ros2_cmd_server ${SRC_DIR})
add_executable(srv_test_client ${EXP_SRC_DIR})

# hardware_interface 插件库
add_library(
  fairino_hardware 
  SHARED 
  ./src/fairino_hardware_interface.cpp
)

# 设置 RPATH，让可执行程序运行时优先在自己目录下找库
set_target_properties(ros2_cmd_server PROPERTIES INSTALL_RPATH "$ORIGIN")

# --- 包含头文件 ---
target_include_directories(ros2_cmd_server PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include/ ${CMAKE_CURRENT_SOURCE_DIR}/)
target_include_directories(srv_test_client PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/examples/include)

target_include_directories(fairino_hardware PUBLIC 
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/>
  $<INSTALL_INTERFACE:include/fairino_hardware>
)

# --- 链接底层 SDK 库 ---
target_link_libraries(ros2_cmd_server ${CMAKE_CURRENT_SOURCE_DIR}/libfairino/lib/libfairino.so)
target_link_libraries(fairino_hardware ${CMAKE_CURRENT_SOURCE_DIR}/libfairino/lib/libfairino.so)

# --- 添加 ROS 2 依赖 ---
ament_target_dependencies(ros2_cmd_server rclcpp fairino_msgs)
ament_target_dependencies(srv_test_client rclcpp fairino_msgs)
ament_target_dependencies(fairino_hardware 
  hardware_interface
  pluginlib
  rclcpp
  fairino_msgs
  rclcpp_lifecycle 
)

# 导出硬件插件说明文件
pluginlib_export_plugin_description_file(hardware_interface fairino_hardware.xml)

# --- 安装逻辑 (关键修改点) ---

# 1. 安装可执行文件到 lib/ (ROS 2 规范)
install(TARGETS ros2_cmd_server srv_test_client
  DESTINATION lib/${PROJECT_NAME}
)

# 2. 安装硬件插件库到 lib 根目录 (确保能被自动搜索到)
install(TARGETS fairino_hardware
  EXPORT fairino_hardware
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
)

# 3. 部署法奥 SDK 库文件到 install/lib 根目录
file(MAKE_DIRECTORY "${CMAKE_INSTALL_PREFIX}/lib")

file(COPY_FILE "libfairino/lib/libfairino.so.2.1.4" 
"${CMAKE_INSTALL_PREFIX}/lib/libfairino.so.2.1.4")

# 创建符号链接，确保运行时能找到 libfairino.so.2
file(CREATE_LINK 
"libfairino.so.2.1.4" 
"${CMAKE_INSTALL_PREFIX}/lib/libfairino.so.2" 
SYMBOLIC)

file(CREATE_LINK 
"libfairino.so.2" 
"${CMAKE_INSTALL_PREFIX}/lib/libfairino.so" 
SYMBOLIC)

# --- 导出与包管理 ---
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_export_targets(fairino_hardware HAS_LIBRARY_TARGET)
ament_export_dependencies(ament_cmake rclcpp hardware_interface pluginlib rclcpp_lifecycle)

ament_package()
