ARG ROS_DISTRO

FROM ros:${ROS_DISTRO}-ros-core

RUN apt update && apt install -y --no-install-recommends python3-pip python3-colcon-common-extensions && rm -rf /var/lib/apt/lists/*

# RUN pip3 install adafruit-circuitpython-pca9685


COPY pca9685-python pca9685-python
RUN cd pca9685-python/library && python3 setup.py install

WORKDIR /colcon_ws/src
COPY ros_pca9685 .

WORKDIR /colcon_ws

RUN . /opt/ros/${ROS_DISTRO}/setup.sh && colcon build --symlink-install

WORKDIR /

COPY ros_entrypoint.sh .
