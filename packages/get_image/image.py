#!/usr/bin/env python

import rospy
import picamera
import picamera.array
import math
import os
import numpy as np
from time import sleep
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
vehicle_name = os.environ['VEHICLE_NAME']

topic = '/' + vehicle_name + '/camera_node/image/compressed'
print(topic)
#msg = sensor_msgs.msg.CompressedImage()
pub = rospy.Publisher(topic, CompressedImage, queue_size = 10)  
rospy.init_node("Pub_IMG")
rate = rospy.Rate(10)
sleep(2)
with picamera.PiCamera() as camera:
  camera.resolution = (320, 240)

  while True and not rospy.is_shutdown():
      with picamera.array.PiRGBArray(camera) as output:
          camera.capture(output, 'bgr')
          output = output.array
          output_compressed = CvBridge().cv2_to_compressed_imgmsg(output)
#          rospy.loginfo(output_compressed)
          pub.publish(output_compressed)
          rate.sleep()

