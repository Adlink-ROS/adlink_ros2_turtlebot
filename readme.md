# ADLINK ROS2 Turtlebot (Demo launch)
Provides ROS 2.0 launch file for turtlebot applications.  

## Features  
* ydlidar + slam_karto (ros2 ver.)  

## Developer    
HaoChih, Lin (haochih.lin@adlinktech.com)  

## Dependencies   
From ADLINK-ROS github:   
* ydlidar (ros2 ver.) https://github.com/Adlink-ROS/ydlidar_ros2    
* slam_karto (ros2 ver.) https://github.com/Adlink-ROS/slam_karto_ros2  
  
From OSRF ROS2 github:  
* turtlebot2_drivers (ros2 ver.)  
* teleop_twist_joy (ros2 ver.)  
* joy (ros2 ver.)  
Installation steps: https://github.com/ros2/turtlebot2_demo  

## Compile  
$ cd AMENT_WS  
$ ament build --isolated --symlink-install --parallel --only adlink_ros2_neuronbot  

## Execute  
Open a new terminal (or source your ament_ws again)  
$ launch `ros2 pkg prefix adlink_ros2_turtlebot`/share/adlink_ros2_turtlebot/launch/slam_karto_demo.py  
  
## Visualization  
Since the current version of rviz2 dose not support "nav_msgs/MapMetaData" msg type,  
the best way to visulize the mapping result is still through the "ros1_briage".  
(Remember to install ros1_briage in advance)   
* Open three new terminals (source both ROS1 & 2 setup.bash)  
* $ roscore  
* $ rviz  
* $ ros2 run ros1_bridge dynamic_bridge --bridge-all-2to1-topics  
  
# License   
Apache License 2.0 (Copyright 2018 ADLINK Technology, Inc.)   
