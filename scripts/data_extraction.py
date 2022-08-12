#!/usr/bin/env python

import rosbag
import os
import cv2

from cv_bridge import CvBridge
from sensor_msgs.msg import Image


def make_directory(directory):

    directory = directory + '/Images'

    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory


# Name of the Bag
bag_name = 'Data-07-29-22-Time-11-08-43.bag'

# Path of bag
bag_path = '/media/sneh/Heracleia/Robot_Data/Indoor_Data/'

# Path to store the data
data_dir = '/home/sneh/Data/'

# Image directory
img_dir = make_directory(data_dir)

# Counters
img_ctr = 0

for topic, msg, t in rosbag.Bag(bag_path+bag_name).read_messages():

    if topic == 'img':
        print('Image frame:')
        print(img_ctr)

        img_data = Image()

        img_data.width = msg.width
        img_data.height = msg.height
        img_data.encoding = msg.encoding
        img_data.data = msg.data

        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(img_data, "passthrough")

        cv2.imwrite(img_dir + '/image_' + str(img_ctr) + '.png', cv_image)
        img_ctr += 1

    """
    if topic == 'joints':
        print('Joints frame:')
        print(msg.header.frame_id)

    if topic == 'laser':
        print('Front laser frame:')
        print(msg.header.frame_id)

    if topic == 'front_laser':
        print('Front laser frame:')
        print(msg.header.frame_id)

    if topic == 'rear_laser':
        print('Rear laser frame:')
        print(msg.header.frame_id)

    if topic == 'cloud':
        print('Cloud frame:')
        print(msg.header.frame_id)
    """