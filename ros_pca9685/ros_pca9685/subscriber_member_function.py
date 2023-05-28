#!/usr/bin/python3

import time

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

from adafruit_servokit import ServoKit

class RosPca9685Subscriber(Node):

    def __init__(self):
        super().__init__('ros_pca9685_subscriber')

        self.kit = ServoKit(channels=16)
        self.kit.continuous_servo[0].set_pulse_width_range(500, 2500)  #from https://www.agfrc.com/index.php?id=2535    

        

        self.subscription = self.create_subscription(Twist,'/cmd_vel',self.subscription_callback,10)
        self.subscription  # prevent unused variable warning


    def subscription_callback(self, msg):
        self.kit.servo[0].angle = 180
        self.get_logger().info('I Hight:')
        time.sleep(5)

        self.kit.servo[0].angle = 0
        self.get_logger().info('I low:')
        time.sleep(5)

        # self.kit.continuous_servo[0].throttle = 1
        # time.sleep(1)
        # self.kit.continuous_servo[0].throttle = -1
        # time.sleep(1)
        # self.kit.continuous_servo[0].throttle = 0




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
