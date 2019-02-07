#!/usr/bin/env python


## ROS node used to translate the posture of the hand (obtained by the kinect) into a csv file.

import argparse
import sys

import rospy

from BaxterGBI_pbr.msg import *


from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)

from nav_msgs.msg import Odometry
from std_msgs.msg import Header


## Callback function associated with the topic 'mirror_end_effector'.
# Whenever a data is written in the topic, this function is called and obtain from ik_tracking function the joints values to assign and
# move the end effector to the goal.
#
# @param data.pose.pose.position: position we want to achieve.
# @param data.pose.pose.orientation: orientation we want to achieve (Quaternion).
def mirror_callback(data):
    
    global file_name
    
    rospy.loginfo("Reading...")
    file_name.write(str(data.pose.pose.position.x)+","+str(data.pose.pose.position.y)+","+str(data.pose.pose.position.z)+","+str(data.pose.pose.orientation.x)+","+str(data.pose.pose.orientation.y)+","+str(data.pose.pose.orientation.z)+","+str(data.pose.pose.orientation.w)+"\n")
    
       
       
## Main of the node. Takes the information from the topic and move the baxter end effector based on those values.
def mirror_server():
    
    rospy.loginfo("Initializing node... ")
    rospy.init_node('mirror_server')
    
    
    global file_name
    file_name = open("rosbag_output.txt","w+")
    
        
    rospy.Subscriber("odometry/baxter/kinect_right_hand", Odometry, mirror_callback)
    
    def clean_shutdown():
        rospy.loginfo("\nExiting example...")
        file_name.close()
    rospy.on_shutdown(clean_shutdown)

    rospy.spin()

if __name__ == "__main__":
    mirror_server()
