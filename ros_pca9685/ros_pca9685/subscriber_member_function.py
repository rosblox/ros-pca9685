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
from sensor_msgs.msg import BatteryState


import smbus
from pca9685 import INA220


class RosPca9685Publisher(Node):

    def __init__(self):
        super().__init__('ros_pca9685_publisher')

        bus = smbus.SMBus(1)
        self.pca9685 = INA220(i2c_addr=0x41, i2c_dev=bus)

        self.publisher_ = self.create_publisher(BatteryState, 'pca9685/data', 10)
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        current_draw, bus_voltage, shunt_voltage = self.pca9685.get_measurements()

        msg = BatteryState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "ros_pca9685"

        msg.current = current_draw
        msg.voltage = bus_voltage

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    ros_pca9685_publisher = RosPca9685Publisher()

    rclpy.spin(ros_pca9685_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ros_pca9685_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
