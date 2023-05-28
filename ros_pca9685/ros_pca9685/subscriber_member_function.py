#!/usr/bin/python3

import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

from adafruit_servokit import ServoKit

class RosPca9685Subscriber(Node):

    def __init__(self):
        super().__init__('ros_pca9685_subscriber')

        channels = 16
        self.kit = ServoKit(channels=channels)
        for idx in range(0,channels-1):
            self.kit.continuous_servo[idx].set_pulse_width_range(500, 2500)  #from https://www.agfrc.com/index.php?id=2535    

        self.subscription = self.create_subscription(Float32MultiArray,'pca9685/cmd',self.subscription_callback,10)
        self.subscription  # prevent unused variable warning


    def subscription_callback(self, msg):
        for idx, value in enumerate(msg.data):
            self.kit.continuous_servo[idx].throttle = value


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
