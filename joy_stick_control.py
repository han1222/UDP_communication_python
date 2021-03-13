import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from ackermann_msgs.msg import AckermannDriveStamped
from std_msgs.msg import Bool

class JOY_CONTROL():
    def __init__(self):
        self.VehCommand_pub =rospy.Publisher("/Ackermann/command/joy", AckermannDriveStamped,queue_size=1)
        self.JoyCommand_joy= rospy.Subscriber("/joy", Joy,self.joy_callback)
        self.acceleraion=0.0
        self.steering_angle=0.0
        self.maximum_acceleration =10.0
        self.maximum_steering_angle =360.0


    def joy_callback(self,data):

        self.VehCommand=AckermannDriveStamped()
        
        self.VehCommand.drive.acceleration=0
        self.VehCommand.drive.steering_angle=0
        
        if data.buttons[5]==1 :
            self.VehCommand.drive.acceleration = self.maximum_acceleration * data.axes[4]
            self.VehCommand.drive.steering_angle =self.maximum_steering_angle * data.axes[0]

        self.VehCommand_pub.publish(self.VehCommand)



if __name__ == '__main__':
    rospy.init_node('joy_controller_py')
    JOY_CONTROL()
    rospy.spin()