from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():

    pkg_path = os.path.join(
        os.getenv('HOME'), 'ros2_ws/src/my_robot'
    )

    urdf = os.path.join(pkg_path, 'urdf/my_robot.urdf')

    return LaunchDescription([

        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open(urdf).read()}]
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description', '-entity', 'my_robot']
        )
    ])

