#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Int64
from simple_robot_msgs.msg import TemperatureReading

def thermal_sensor():
    pub = rospy.Publisher('/sensors/temperature', TemperatureReading, queue_size=10)
    rospy.init_node('thermal_sensor', anonymous=True)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        rand_value = random.randint(20,40)
        rospy.loginfo(rand_value)
        pub.publish(rand_value)
        rate.sleep()

if __name__=="__main__":
    try:
        thermal_sensor()
    except rospy.ROSInterruptException:
        pass
