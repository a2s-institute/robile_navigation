import os 

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from ament_index_python.packages import get_package_share_directory

NUM_ROBOTS = 2


def gen_robot_list(number_of_robots):
    
    robots = []
    
    for i in range(number_of_robots):
        robot_name = "robile_"+ str(i)
        x_pos = float(i)
        robots.append({'name': robot_name, 'x_pose': x_pos, 'y_pose': 0.0, 'z_pose': 0.01})

    return robots 



def generate_launch_description():

    robile_nav_path = get_package_share_directory('robile_navigation')

    # Create the launch configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time')

    robots = gen_robot_list(NUM_ROBOTS) # list of robots with names and poses:
    spawn_robots_cmds = [] # list of commands to spawn robots

    for robot in robots:
        robot_name = robot['name']
        params_file_path = os.path.join(robile_nav_path, 'config', f'{robot_name}_nav2_params.yaml')
        print ("############### ", robot_name)
        print ("############### ", params_file_path)

        group_cmds = GroupAction([
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(robile_nav_path , 'launch', 
                                                            'single_robile_nav2_bringup.launch.py')),
                launch_arguments={
                                  'use_sim_time': use_sim_time,
                                  'robot_name': robot_name,
                                  'namespace': robot_name,
                                  'use_namespace': 'True',
                                  'params_file': params_file_path,
                                  'use_composition': 'False',
                                  }.items()), ])
        
        spawn_robots_cmds.append(group_cmds)

    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true')

    ld =  LaunchDescription()
    ld.add_action(declare_use_sim_time_cmd)
    # Add each cmd as a new "launch action" to the launch description
    for spawn_robot_cmd in spawn_robots_cmds:
        ld.add_action(spawn_robot_cmd)

    return ld
