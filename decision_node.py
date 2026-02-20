import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class decisionNode(Node):

    def __init__(self):
        super().__init__('decision_node')

        #satellite_listenerın yayınladığı raporu dinliyoruz
        self.subscription = self.create_subscription(String,'satellite_report',self.decision_callback,10)

        self.get_logger().info("decision_node has been started")
    def decision_callback(self, msg):
        report = msg.data

        if report == "tek sayıdayız":
            self.get_logger().warn("ALARM! uydu anormal değer gönderiyor!")

        elif report == "cift sayıdayız":
            self.get_logger().info("sistem stabil bir sorun yok.")

        else:
            self.get_logger().info("bilinmeyen veri geldi")


def main(args=None):
    rclpy.init(args=args)
    node = decisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

