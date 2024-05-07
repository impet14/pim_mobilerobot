#!/bin/bash

# Kill all ROS processes
killall -9 roscore
killall -9 rosmaster
killall -9 rosout
killall -9 roslaunch
killall -9 rosnode
killall -9 rosservice
killall -9 rosparam
killall -9 rostopic
killall -9 rosrun

# Kill Gazebo processes
killall -9 gzserver
killall -9 gzclient
pkill -f ros
