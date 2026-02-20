#!/usr/bin/env python 3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class RobotStatePublisherNode(Node):

    def __init__(self):
        super().__init__("robot_state_publisher")

        self.counter_ = 0

        self.publisher_ = self.create_publisher(String, "state_publisher", 10)
        self.timer_ = self.create_timer(1, self.publish_state)

        self.get_logger().info("Robot state publisher has been started.")

    def publish_state(self):
        msg = String()
        msg.data = str(self.counter_) 
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing: " + msg.data)
        self.counter_ += 1   


def main(args=None):
    rclpy.init(args=args)
    node = RobotStatePublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()    