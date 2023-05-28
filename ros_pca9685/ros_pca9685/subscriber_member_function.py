# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

#  Import the PCA9685 module.
# from pca9685_driver import PCA9685


class RosPca9685Subscriber(Node):

    def __init__(self):
        super().__init__('ros_pca9685_subscriber')

        # Initialize the PCA9685 board
        # self.pca9685 = PCA9685(0x40)


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
