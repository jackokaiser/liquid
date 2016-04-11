#!/usr/bin/env python
PKG = 'liquid'
import roslib; roslib.load_manifest(PKG)

import rospy
from dvs_msgs.msg import Event
from dvs_msgs.msg import EventArray
from sensor_msgs.msg import Image, CameraInfo
from rospy.numpy_msg import numpy_msg
import numpy as np
import sys
import rosbag


def main():
    if (len(sys.argv) < 2):
        print('Usage: '+sys.argv[0]+' {bagfile}')
        return 1

    print('Reading bag '+sys.argv[1])
    bag = rosbag.Bag(sys.argv[1])
    for topic, msg, t in bag.read_messages(topics=['dvs/events', 'target_ground_truth']):
        print msg

    bag.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
