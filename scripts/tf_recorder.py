#!/usr/bin/env python

import os
import rospy
import tf2_ros
import pickle

# Find current path
dir_path = os.getcwd()

# Name of the file
pkl_name = 'Tf_tree.pkl'

# Final path that stores tf
final_dir = dir_path + '/' + pkl_name

tf_tree=[["robot_odom","robot_base_footprint"],
         ["robot_base_footprint", "robot_base_link"],
         ["robot_base_link", "robot_front_rgbd_camera_rgb_base_link"],
         ["robot_front_rgbd_camera_rgb_base_link", "robot_front_rgbd_camera_depth_frame"],
         ["robot_front_rgbd_camera_rgb_base_link", "robot_front_rgbd_camera_depth_optical_frame"],
         ["robot_base_link", "robot_front_laser_link"],
         ["robot_front_laser_link", "robot_front_laser_base_link"],
         ["robot_base_link", "robot_rear_laser_link"],
         ["robot_rear_laser_link", "robot_rear_laser_base_link"]
         ]

t_tree={}

rospy.init_node('tf_listener')

tf_buffer = tf2_ros.Buffer()
tf2_listener = tf2_ros.TransformListener(tf_buffer)

cnt=0
for pair in tf_tree:
    t = tf_buffer.lookup_transform(pair[0], pair[1], rospy.Time(0), rospy.Duration(10))
    t_tree[cnt]=t
    cnt=cnt+1

# Store the data
pickle_out = open(final_dir, "wb")
pickle.dump(t_tree, pickle_out,pickle.HIGHEST_PROTOCOL)
pickle_out.close()
