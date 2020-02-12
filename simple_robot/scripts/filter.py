#!/usr/bin/env python

import rospy
from simple_robot_msgs.msg import TemperatureReading, VictimFound

def filter():
    rospy.init_node("filter",anonymous=True)
    rospy.Subscriber('/sensors/temperature', TemperatureReading, callback)
    rospy.spin()

pub = rospy.Publisher("/data_fusion/victim_found", VictimFound, queue_size=10)


def callback(data):
    if data.temp > 37:
        pub.publish("thermal")
        rospy.loginfo(data)

if __name__ == "__main__":
    filter()
