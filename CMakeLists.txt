cmake_minimum_required(VERSION 3.0.2)
project(robile_navigation)

find_package(catkin REQUIRED COMPONENTS
	  amcl
	  map_server
	  move_base
)
###################################
## catkin specific configuration ##
###################################
catkin_package()

###########
## Build ##
###########
include_directories(
	# include
	  ${catkin_INCLUDE_DIRS}
)























































