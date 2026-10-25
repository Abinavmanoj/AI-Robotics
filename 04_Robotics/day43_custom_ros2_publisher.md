# Day 43: Custom ROS 2 Python Publisher

## Goal
Create a Python ROS 2 node that publishes robot status messages every second.

## Concepts Learned
- Node: A program that performs a specific task.
- Publisher: Sends messages.
- Topic: A channel for communication between ROS 2 nodes.
- Timer: Calls a function periodically.
- String message: Carries text using std_msgs/msg/String.

## Project
Package: robot_learning
Node: robot_status_publisher
Topic: /robot_status

## Commands

Build the package:

    cd ~/ros2_ws
    source /opt/ros/jazzy/setup.bash
    colcon build --packages-select robot_learning

Run the publisher:

    source ~/ros2_ws/install/setup.bash
    ros2 run robot_learning robot_status_publisher

Monitor the topic in a second Ubuntu terminal:

    source /opt/ros/jazzy/setup.bash
    ros2 topic echo /robot_status

## Result
Successfully ran a custom ROS 2 Python publisher and verified that messages were received through the /robot_status topic.

## Next Goal
Create a custom subscriber that reads robot status messages.
