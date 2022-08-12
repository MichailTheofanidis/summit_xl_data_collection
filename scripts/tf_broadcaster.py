#!/usr/bin/env python

import os
import rospy
import tf
import pickle

# Find current path
dir_path = os.getcwd()

# Name of the file
pkl_name = 'Tf_tree.pkl'

# Final path that stores tf
final_dir = dir_path + '/' + pkl_name

# Store the data
with open(final_dir, 'rb') as file:
    tf_tree = pickle.load(file)
    file.close()

rospy.init_node('summitX_tf_broadcaster')

br = tf.TransformBroadcaster()
rate = rospy.Rate(1.0)

while not rospy.is_shutdown():

    for i in range(0,len(tf_tree)):
        br.sendTransform((tf_tree[i].transform.translation.x,tf_tree[i].transform.translation.y,tf_tree[i].transform.translation.z),
                         (tf_tree[0].transform.rotation.x, tf_tree[0].transform.rotation.y, tf_tree[0].transform.rotation.z, tf_tree[0].transform.rotation.w),
                         rospy.Time.now(),
                         tf_tree[i].child_frame_id,
                         tf_tree[i].header.frame_id)
        rate.sleep()
