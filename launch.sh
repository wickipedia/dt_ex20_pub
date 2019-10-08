#!/bin/bash

set -e

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------
roscore &
sleep 5
roslaunch get_image multiple_nodes.launch
#rosrun read_bag read.py
