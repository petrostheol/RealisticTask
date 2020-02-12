#!/usr/bin/env python

import rospy
import random
import actionlib
from simple_robot_msgs.msg import GetRobotPoseAction, GetRobotPoseResult

class ActionServer():

    def __init__(self):
        self.a_server=actionlib.SimpleActionServer("post_location", GetRobotPoseAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def execute_cb(self, goal):
        success= True
        result=GetRobotPoseResult()

        result.x = random.randint(0,9)
        result.y = random.randint(0,9)
        self.a_server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node("location_server")
    s = ActionServer()
    rospy.spin()
