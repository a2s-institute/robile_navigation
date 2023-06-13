cmake_minimum_required(VERSION 3.8)
project(robile_navigation)

# find dependencies
find_package(ament_cmake REQUIRED)

################################################################################
# Install
################################################################################

install(DIRECTORY launch config maps 
	DESTINATION share/${PROJECT_NAME}
)

################################################################################
# Macro for ament package
################################################################################
ament_package()
