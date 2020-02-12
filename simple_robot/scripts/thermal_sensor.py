#!/usr/bin/env python

#THIS NODE IS A SIMULATION OF A THERMAL SENSOR. WHEN IT IS INITIALISED, IT STARTS
#PUBLISHING MESSAGES OF TYPE TemperatureReading IN THE TOPIC '/sensors/temperature'
#WITH A FREQUENCY SET AT 1Hz(LINE 18)

# NAME OF NODE = thermal_sensor
# NAME OF TOPIC IT PUBLISHES TO: /sensor/temperature
# TYPE OF MESSAGES BEING PUBLISHED: TemperatureReading


import rospy
import random
from std_msgs.msg import Int64
from simple_robot_msgs.msg import TemperatureReading                                    #WHEN simple_robot PACKAGE WAS CREATED, WE ADDED THE simple_robot_msgs DEPENDENCY

def thermal_sensor():                                                                   #DEFINE THERMAL_SENSOR NODE
    pub = rospy.Publisher('/sensors/temperature', TemperatureReading, queue_size=10)    #DEFINE TOPIC NAMED pub ('topic', type of messages being published, queue_size)
    rospy.init_node('thermal_sensor', anonymous=True)                                   #INITIALIZE NODE WITH (ANONYMOUS=UNIQUE) NAME 'thermal_sensor'
    rate = rospy.Rate(1)                                                                #FREQUENCY AT WHICH MESSAGES ARE PUBLISHED = 1Hz

    while not rospy.is_shutdown():
        rand_value = random.randint(20,40)                                              #GENERATE RANDOM VALUE (SENSOR MEASUREMENT SIMULATION)
        rospy.loginfo(rand_value)                                                       #PRINT INFO ABOUT THE RANDOM VALUE (MESSAGE) BEING GENERATED
        pub.publish(rand_value)                                                         #PUBLISH THE rand_value IN TOPIC /sensors/temperature
        rate.sleep()                                                                    #SLEEP LONG ENOUGH TO MANTAIN FREQUENCY 1Hz

if __name__=="__main__":
    try:
        thermal_sensor()
    except rospy.ROSInterruptException:
        pass
