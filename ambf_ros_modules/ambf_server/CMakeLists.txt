#  Software License Agreement (BSD License)
#  Copyright (c) 2020, AMBF.
#  (https://github.com/WPI-AIM/ambf)
#
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#  * Redistributions of source code must retain the above copyright
#  notice, this list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above
#  copyright notice, this list of conditions and the following
#  disclaimer in the documentation and/or other materials provided
#  with the distribution.
#
#  * Neither the name of authors nor the names of its contributors may
#  be used to endorse or promote products derived from this software
#  without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#
#  $Author: Adnan Munawar $
#  $Date:  $
#  $Rev: $

cmake_minimum_required(VERSION 3.0.2)
project(ambf_server)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED
geometry_msgs
ambf_msgs
tf
message_generation)

catkin_package(
    INCLUDE_DIRS include
    LIBRARIES ambf_server
    CATKIN_DEPENDS ambf_msgs message_runtime
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories( include ${catkin_INCLUDE_DIRS})

set (HDR_FILES
    include/${PROJECT_NAME}/RosComBase.h
    include/${PROJECT_NAME}/CmdWatchDog.h
    include/${PROJECT_NAME}/Actuator.h
    include/${PROJECT_NAME}/ActuatorRosCom.h
    include/${PROJECT_NAME}/Camera.h
    include/${PROJECT_NAME}/CameraRosCom.h
    include/${PROJECT_NAME}/Light.h
    include/${PROJECT_NAME}/LightRosCom.h
    include/${PROJECT_NAME}/Object.h
    include/${PROJECT_NAME}/ObjectRosCom.h
    include/${PROJECT_NAME}/RigidBody.h
    include/${PROJECT_NAME}/RigidBodyRosCom.h
    include/${PROJECT_NAME}/Sensor.h
    include/${PROJECT_NAME}/SensorRosCom.h
    include/${PROJECT_NAME}/Vehicle.h
    include/${PROJECT_NAME}/VehicleRosCom.h
    include/${PROJECT_NAME}/World.h
    include/${PROJECT_NAME}/WorldRosCom.h)

set (SRC_FILES
    src/RosComBase.cpp
    src/Actuator.cpp
    src/ActuatorRosCom.cpp
    src/Camera.cpp
    src/CameraRosCom.cpp
    src/Light.cpp
    src/LightRosCom.cpp
    src/Object.cpp
    src/ObjectRosCom.cpp
    src/RigidBody.cpp
    src/RigidBodyRosCom.cpp
    src/Sensor.cpp
    src/SensorRosCom.cpp
    src/Vehicle.cpp
    src/VehicleRosCom.cpp
    src/World.cpp
    src/WorldRosCom.cpp
    )

## Declare a C++ library
add_library(ambf_server ${HDR_FILES} ${SRC_FILES})

add_dependencies(ambf_server ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(ambf_server ${catkin_LIBRARIES})
