# Day 42: ROS 2 Nodes and Topics

## What I learned
- A **node** is a program that performs a task in a ROS 2 system.
- A **topic** is a communication channel between nodes.
- A **publisher** sends messages to a topic.
- A **subscriber** receives messages from a topic.
- `ros2 topic echo` displays messages published on a topic.

## Commands practiced

```bash
ros2 node list
ros2 topic list
ros2 topic echo /chatter
ros2 topic info /chatter
```

## Practical result

Topic: `/chatter`

Message type: `std_msgs/msg/String`

Publisher count: 1

Subscription count: 1

Example message: `Hello World: 62`

## What I achieved
Successfully tested ROS 2 Talker–Listener communication and inspected the `/chatter` topic.
