import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')

        self.publisher = self.create_publisher(
            Float32,
            'robot_distance',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_distance)

    def publish_distance(self):
        msg = Float32()
        msg.data = 150.0

        self.publisher.publish(msg)
        self.get_logger().info(f'Distance: {msg.data} cm')


def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()