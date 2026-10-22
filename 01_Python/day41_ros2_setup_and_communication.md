# Day 41: ROS 2 Setup and Communication

## Objective
Install ROS 2 Jazzy on Ubuntu 24.04 using WSL and verify communication between ROS 2 nodes.

## Environment
- Windows with WSL 2
- Ubuntu 24.04 LTS
- ROS 2 Jazzy Desktop
- VS Code

## What I Learned
- A ROS 2 node is a program that performs a specific task.
- A Talker node publishes messages.
- A Listener node receives messages.
- ROS 2 nodes communicate using topics.

## Practical Test

**Terminal 1 — Talker**
```bash
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_cpp talker
```

**Terminal 2 — Listener**
```bash
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_py listener
```

## Result
The Listener successfully received messages published by the Talker, including messages such as:

`I heard: [Hello World: 88]`

## Key Takeaway
Successfully installed ROS 2 Jazzy and verified communication between two ROS 2 nodes.

## Next Step
Learn ROS 2 nodes and topics using the ROS 2 command-line tools.