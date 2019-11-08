#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

def onPanAngle(data):
    if data < 0 :
        data = 0
    if data > 360 :
        data = 360
    panTick.publish((data/360)*4095)

def onTiltAngle(data):
    if data < 0 :
        data = 0
    if data > 180 :
        data = 180
    tiltTick.publish((data/360)*4095 + 1024)

def panTiltAngle():
    panTick = rospy.Publisher('pan_goal_position', Int16, queue_size=1)
    tiltTick = rospy.Publisher('tilt_goal_position', Int16, queue_size=1)
    rospy.init_node('panTiltAngle', anonymous=True)
    rospy.Subscriber('pan_goal_angle', Int16, onPanAngle)
    rospy.Subscriber('tilt_goal_angle', Int16, onTiltAngle)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.spin()
        rate.sleep()

if __name__ == '__main__':
    try:
        panTiltAngle()
    except rospy.ROSInterruptException:
        pass
