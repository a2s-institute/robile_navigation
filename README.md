# robile_navigation
Navigation launch files for robile in gazebo and real robot with ROS2. Also suport multi robot navigation.

## Instalation

This package depends on the robile packages and different ros navigation packages for the launch files to run.

1. [Robile Description](https://github.com/mas-group/robile_description/tree/ros2_humble)
2. [Robile Gazebo](https://github.com/mas-group/robile_gazebo/tree/ros2_humble)

Follow the [robile_gazebo](https://github.com/mas-group/robile_gazebo/tree/ros2_humble) instalation instructions and install the apt packages required for gazebo and launching robot in gazebo.
Here we install packages required for navigation.
~~~ sh

cd ~/ros2_ws/src
git clone https://github.com/mas-group/robile_description.git -b ros2_humble
git clone https://github.com/mas-group/robile_gazebo.git -b ros2_humble
git clone https://github.com/mas-group/robile_navigation.git -b ros2



cd ~/ros2_ws  #Very important to do below command only from worspace folder and always
sudo rosdep init
rosdep update
rosdep install -i --from-path src --rosdistro humble -y

colcon build robile_description robile_gazebo
colcon build
source ~/ros2_ws/devel/setup.bash
~~~

## Usage

### Single Robile 
To start the gazebo simulator, use one of the launch files defined in the [launch/](launch/) directory as follows:

~~~ sh
roslaunch robile_gazebo single_robile_sim.launch.py
~~~

This will launch the robile in simulation. Now we will launch the navigation stack to localize in the map

~~~ sh
roslaunch robile_navigation single_robile_nav2_bringup.launch.py
~~~

### Multiple Robile 
To start the gazebo simulator with multiple Robiles, use one of the launch files defined in the [launch/](launch/) directory as follows:

~~~ sh
roslaunch robile_gazebo multi_robile_sim.launch.py
~~~

This will launch the robile in simulation. Now we will launch the navigation stack to localize in the map

~~~ sh
roslaunch robile_navigation multi_nav2_bringup.launch.py
~~~

