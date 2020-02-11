#!/usr/bin/env python

import rospy
import random
import actionlib
from simple_robot_msgs.msg import GetRobotPoseAction, GetRobotPoseResult

def callback(goal):
    result = GetRobotPoseResult()
    result.x = random.randint(0,9)
    result.y = random.randint(0,9)
    server.set_succeeded(result)

def create_server():
    rospy.init_node('location_server')
    server = actionlib.SimpleActionServer('/slam/get_robot_pose', GetRobotPoseAction, callback, False)
    server.start()
    rospy.spin()

if __name__=="__main__":
    create_server()
