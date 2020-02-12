#!/usr/bin/env python

import rospy
import random
import actionlib
from simple_robot_msgs.msg import GetRobotPoseAction, GetRobotPoseResult

class ActionServer():

    def __init__(self):
        self.a_server=actionlib.SimpleActionServer("post_location",
         GetRobotPoseAction, execute_cb=self.execute_cb, auto_start=False)          #self IS THE OBJECT CREATED BY THE ActionServer() CLASS.
                                                                                    #IT OPENS THE SERVER "post_location" WHICH ACCEPTS MESSAGES OF TYPE GetRobotPoseAction
                                                                                    #execute_cb IS THE CALLBACK FUNCTION OF THE OBJECT self
                                                                                    #auto_start=False IN ORDER !NOT! TO START THE SERVER AUTOMATICALLY, BUT ONLY IN __main__

        self.a_server.start()                                                       #START UP THE SERVER

    def execute_cb(self, goal):                                                     #DEFINE CALLBACK WHICH "BELONGS" TO THE self OBJECT AND PROCESSES THE goal
        success= True                                                               #success=True. IF goalID IS SENT IN THE /cancel TOPIC IN WHICH THE SERVER SUBSCRIBES, goal is cancelled BY SETTING success=False
        result=GetRobotPoseResult()                                                 #CREATE OBJECT result FROM CLASS GetRobotPoseResult()

        result.x = random.randint(0,9)                                              #SET x VALUE FROM result OBJECT
        result.y = random.randint(0,9)                                              #SET y VALUE FROM result OBJECT
        self.a_server.set_succeeded(result)                                         #OUTPUT THE RESULT(RESPONSE) TO THE SERVER

if __name__ == "__main__":
    rospy.init_node("location_server")                                              #INITIALIZE NODE "location_server"
    s = ActionServer()                                                              #CREATE OBJECT s FROM CLASS ActionServer()
    rospy.spin()                                                                    #KEEP "location_server" OPEN
