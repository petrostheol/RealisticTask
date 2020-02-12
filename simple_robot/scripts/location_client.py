#!/usr/bin/env python

#THIS SCRIPT GETS THE VictimFound MESSAGES AND SENDS A goal TO THE SERVER. The
#SERVER THEN GENERATES THE result WHICH IS PRINTED THROUGH THE SUBSCRIBER'S callback

import rospy
import random
import actionlib
from simple_robot_msgs.msg import GetRobotPoseAction, GetRobotPoseGoal, VictimFound, GetRobotPoseGoal, GetRobotPoseResult

def feedback_cb(msg):
    print 'Feedback received: ', msg

def call_server():

    client = actionlib.SimpleActionClient('post_location', GetRobotPoseAction)                  #CREATE OBJECT client FROM CLASS SimpleActionClient

    client.wait_for_server()                                                                    #WAIT UNTILL SERVER IS OPEN

    goal = GetRobotPoseGoal()                                                                   #CREATE OBJECT goal FROM CLASS GetRobotPoseGoal. IT HAS NO ARGUMENTS

    client.send_goal(goal, feedback_cb=feedback_cb)                                             #SEND THE goal TO SERVER IN WICH YOU HAVE "SUBSCRIBED"

    client.wait_for_result()                                                                    #WAIT FOR SERVER'S RESULT (RESPONSE)

    result = client.get_result()                                                                #IN VARIABLE result SAVE THE RESPONSE (RESULT)

    return result                                                                               #RETURN THE result

def controller():                                                                               #DEFINE SUBSCRIBER THAT DETECTS THE VictimFound MESSAGES
    rospy.init_node("action_client", anonymous= True)                                           #NORMAL SUBSCRIPTION
    rospy.Subscriber("/data_fusion/victim_found", VictimFound, callback)                        #NORMAL SUBSCRIPTION
    rospy.spin()                                                                                #NORMAL SUBSCRIPTION

def callback(data):                                                                             #DEFINE CALLBACK(data = VictimFound message)
    if data.thermal == "thermal":                                                               #thermal IS THE VARIABLE'S NAME THAT WAS DECLARED IN VictimFound.msg
        result=call_server()                                                                    #CREATE THE REQUEST FOR THE SERVER THROUGH call_server() AND SAVE THE RETURN IN result
        print "The result is: ", result                                                         #PRINT THE MESSAGE

if __name__=="__main__":

    try:
        controller()                                                                            #THE controller() FUNCTION INITIALIZES THE SUBSCRIBER. THE SUBSCRIBER'S callback FUNCTION
                                                                                                #SENDS A goal TO THE SERVER AND GETS A result THAT IS THE COORDINATES OF THE ROBOT

    except rospy.ROSInterruptException as e:                                                    #COMMON ERROR
        print "Something went wrong: ",e
