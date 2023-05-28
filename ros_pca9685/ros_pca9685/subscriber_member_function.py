#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

import board
import busio
# from adafruit_motor import servo
from adafruit_pca9685 import PCA9685


class RosPca9685Subscriber(Node):

    def __init__(self):
        super().__init__('ros_pca9685_subscriber')

        self.i2c = i2c = busio.I2C(board.SCL, board.SDA)
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 50

        self.subscription = self.create_subscription(Twist,'/cmd_vel',self.subscription_callback,10)
        self.subscription  # prevent unused variable warning

    def subscription_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)



def main(args=None):
    rclpy.init(args=args)

    ros_pca9685_subscriber = RosPca9685Subscriber()

    rclpy.spin(ros_pca9685_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ros_pca9685_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
