from setuptools import setup

package_name = 'ros_pca9685'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rosblox',
    maintainer_email='info@rosblox.com',
    description='TODO: Package description',
    license='BSD3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'ros_pca9685_node = ros_pca9685.subscriber_member_function:main',
        ],
    },
)
