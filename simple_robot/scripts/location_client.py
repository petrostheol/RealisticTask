#!/usr/bin/env python

import rospy
import random
import actionlib
from simple_robot_msgs.msg import GetRobotPoseAction, VictimFound, GetRobotPoseGoal, GetRobotPoseResult

def location_client():
    rospy.init_node("location_client")
    rospy.Subscriber("/data_fusion/victim_found", VictimFound, callback)
    client = actionlib.SimpleActionClient("/slam/get_robot_pose", GetRobotPoseAction)
    client.wait_for_server()
    client.wait_for_result()
    rospy.spin()

def callback(data):
    if data.thermal == "thermal":
        location_client()
        rospy.loginfo("Victim Found! Robot Pose = (%d), (%d)",client.get_result.x,client.get_result.y)



if __name__=="__main__":
    location_client()
