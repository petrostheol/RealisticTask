#!/usr/bin/env python

#THE filter NODE SUBSCRIBES TO /sensors/temperature, THUS GETTING ALL THE MESSAGES
#THAT THE SENSOR (thermal_sensor) IS PUBLISHING.
#THE CALLBACK FUNCTION HANDLES THESE MESSAGES AND PUBLISHES A STRING "thermal"
#IF THE SENSOR'S MEASUREMENT EXCEEDED 37 CELSIUS DEGREES

#filter SUBSCRIBES TO '/sensors/temperature'
#callback HANDLES THE MESSAGES OF THE SUBSCRIPTION
#AFTER THE DATA IS PROCESSED, A MESSAGE (TYPE:STRING) IS PUBLISHED IN /data_fusion/victim_found STRING MESSAGES

import rospy
from simple_robot_msgs.msg import TemperatureReading, VictimFound

def filter():                                                                           #DEFINE FILTER
    rospy.init_node("filter",anonymous=True)                                            #INITIALIZE NODE 'filter'
    rospy.Subscriber('/sensors/temperature', TemperatureReading, callback)              #SUBSCRIBE TO /sensor/temperature AND SEND THE MESSAGES TO callback AS data
    rospy.spin()

pub = rospy.Publisher("/data_fusion/victim_found", VictimFound, queue_size=10)          #CREATE A TOPIC NAMED /data_fusion/victim_found IN WHICH VictimFound MESSAGES ARE PUBLISHED


def callback(data):                                                                     #data IS THE MESSAGE THAT THE SUBSCRIBER (LINE 17) READ. IT'S TYPE: TemperatureReading.
                                                                                        #TemperatureReading.msg has only 1 VARIABLE NAMED temp (type: int64)

    if data.temp > 37:                                                                  #FROM THE MESSAGE YOU RECEIVED, EXTRACT THE VARIABLE NAMED temp AND COMPARE IT TO 37
        pub.publish("thermal")                                                          #IF data (SENSOR'S MEASUREMENT) IS >37, PUBLISH "thermal" IN pub
        rospy.loginfo(data)                                                             #PRINT THE INFO OF THE MESSAGE

if __name__ == "__main__":
    filter()                                                                            #CALLING filter() AUTOMATICALLY CALLS callback() [BECAUSE OF SUBSCRIBER]
