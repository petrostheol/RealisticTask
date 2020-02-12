#!/usr/bin/env python

import rospy
import random
import actionlib
from simple_robot_msgs.msg import GetRobotPoseAction, GetRobotPoseGoal, VictimFound, GetRobotPoseGoal, GetRobotPoseResult

def feedback_cb(msg):
    print 'Feedback received: ', msg

def call_server():

    client = actionlib.SimpleActionClient('post_location', GetRobotPoseAction)

    client.wait_for_server()

    goal = GetRobotPoseGoal()

    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result

def controller():
    rospy.init_node("action_client", anonymous= True)
    rospy.Subscriber("/data_fusion/victim_found", VictimFound, callback)
    rospy.spin()

def callback(data):
    if data.thermal == "thermal":
        result=call_server()
        print "The result is: ", result

if __name__=="__main__":

    try:
        controller()
    except rospy.ROSInterruptException as e:
        print "Something went wrong: ",e
