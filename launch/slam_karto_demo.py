# Copyright 2018 ADLINK Technology, Inc.
# Developer: HaoChih, LIN (haochih.lin@adlinktech.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory
from launch.exit_handler import restart_exit_handler
from ros2run.api import get_executable_path


def launch(launch_descriptor, argv):
    ld = launch_descriptor
    package = 'turtlebot2_drivers'
    ld.add_process(
        cmd=[get_executable_path(package_name=package, executable_name='kobuki_node')],
        name='kobuki_node',
        exit_handler=restart_exit_handler,
    )

    package = 'ydlidar'
    ld.add_process(
        cmd=[get_executable_path(package_name=package, executable_name='ydlidar_node')],
        name='ydlidar_node',
        exit_handler=restart_exit_handler,
    )

    package = 'tf2_ros'
    ld.add_process(
        # Transform from base_link to laser_frame 
        cmd=[
            get_executable_path(
                package_name=package, executable_name='static_transform_publisher'),
            '0.0', '0.0', '0.1',
            '0', '0', '0', '1',
            'base_link',
            'laser_frame'
        ],
        name='static_tf_pub_base_rgb',
        exit_handler=restart_exit_handler,
    )
			
    package = 'joy'
    ld.add_process(
        cmd=[get_executable_path(package_name=package, executable_name='joy_node')],
        name='joy_node',
        exit_handler=restart_exit_handler,
    )
	
    package = 'teleop_twist_joy'
    ld.add_process(
        cmd=[get_executable_path(package_name=package, executable_name='teleop_node')],
        name='teleop_node',
        exit_handler=restart_exit_handler,
    )
	
    package = 'slam_karto'
    ld.add_process(
        cmd=[get_executable_path(package_name=package, executable_name='slam_karto')],
        name='slam_karto',
        exit_handler=restart_exit_handler,
    )

    return ld
