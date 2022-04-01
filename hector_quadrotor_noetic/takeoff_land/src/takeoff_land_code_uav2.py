#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

def takeoff_callback(msg): 
  twist_msg.linear.z = 0.4
  i = 0
  while i < 4:
      cmd_vel_pub.publish(twist_msg)
      i = i + 1
      rate.sleep()
  
  twist_msg.linear.z = 0
  cmd_vel_pub.publish(twist_msg)
  
def land_callback(msg): 
  twist_msg.linear.z = -0.5
  i = 0
  while i < 10:
      cmd_vel_pub.publish(twist_msg)
      i = i + 1
      rate.sleep()
  
  twist_msg.linear.z = 0
  cmd_vel_pub.publish(twist_msg)

rospy.init_node('takoff_land')
rate = rospy.Rate(1)

takeoff_sub = rospy.Subscriber('/uav2/takeoff', Empty, takeoff_callback)
land_sub = rospy.Subscriber('/uav2/land', Empty, land_callback)
cmd_vel_pub = rospy.Publisher('/uav2/cmd_vel', Twist, queue_size=1)

empty_msg = Empty()
twist_msg = Twist()

rospy.spin()