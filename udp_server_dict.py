import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import socket
import pickle

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

UDP_IP = "Client IP Address" # write your Client IP Address
UDP_PORT = 5005 #port number 
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

def callback(data):
    # print(type(sock))
    twist = Twist()
    # vertical left stick axis = linear rate
    twist.linear.x = 1*data.axes[4]
    # horizontal left stick axis = turn rate
    twist.angular.z = -1*data.axes[0]
    command = {"longitudinal_cntrl_shock_level": twist.linear.x,
         "lateral_cntrl_shock_level": twist.angular.z
         }

    MESSAGE = pickle.dumps(command)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    pub.publish(twist)

    # print(twist.linear.x)
    # print(twist.angular.z)

# Intializes everything
def start():
    rospy.init_node('Joy2WindowPC')
    global pub
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()


if __name__ == '__main__':

    start()
sock.close()
