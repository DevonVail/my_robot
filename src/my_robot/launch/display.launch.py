#!/usr/bin/env python3
#

import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='my_robot_node',
            executable='my_robot',
            name='my_robot'),
  ])
