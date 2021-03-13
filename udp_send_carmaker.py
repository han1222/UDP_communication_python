import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from ackermann_msgs.msg import AckermannDriveStamped
from std_msgs.msg import Bool

import socket
import pickle
import struct


# sudo apt-get install ros-kinetic-teleop-twist-joy 
#rostopic echo /joy
#roslaunch teleop_twist_joy teleop.launch
# Author: SEUNGIL HAN
# E-mail: robotics@kaist.ac.kr
# This ROS Node converts Joystick inputs from the joy node
# into commands for Widnow PC with UDP communication

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 4 aka right stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

UDP_IP = "127.0.0.1" # write your Client IP Address local is 127.0.0.1
UDP_PORT = 60001 #port number 
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

def VehCommandCallback(data):
    # print(type(sock))
    acceleration=data.drive.acceleration
    steering_angle = data.drive.steering_angle
    command=struct.pack('=Bddib', 255,steering_angle,acceleration,1,0)
    upcommand= struct.unpack('=Bddib',command)
    # MESSAGE = pickle.dumps(command)
    sock.sendto(command, (UDP_IP, UDP_PORT))
    print(upcommand)

# Intializes everything
def start():
    rospy.init_node('UdoSendToCarmaker')
    rospy.Subscriber("/Ackermann/command/joy", AckermannDriveStamped, VehCommandCallback)
    rospy.spin()


if __name__ == '__main__':

    start()
sock.close()
