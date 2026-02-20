import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class SatelliteNode(Node):

    def __init__(self):
        super().__init__("satellite")

        self.subscriber_ = self.create_subscription(
            String, 
            "state_publisher", 
            self.callback_satellite, 
            10)
        
        self.publisher_ = self.create_publisher(
            String,
            "satellite_report",
            10)

        self.get_logger().info("Satellite has benn started")

    def callback_satellite(self, msg):
        value = int(msg.data)
        report_msg = String()

        if value % 2 == 0:
            report_msg.data = "cift sayıdayız"
            self.get_logger().info("cift sayıdayız")
        else:
            report_msg.data = "tek sayıdayız" 
            self.get_logger().info("tek sayıdayız")    

        if value == 31:
            self.get_logger().info("terbiyesiz bir sayıya geldik: " + str(value))

        self.publisher_.publish(report_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SatelliteNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()    
            