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
import pylab

def main():
    if (len(sys.argv) < 2):
        print('Usage: '+sys.argv[0]+' {bagfile}')
        return 1

    pylab.ion()
    print('Reading bag '+sys.argv[1])
    bag = rosbag.Bag(sys.argv[1])
    allEvents = []
    allPositions = []

    for topic, msg, t in bag.read_messages(topics=['dvs/events']):
        allEvents = allEvents + msg.events

    for topic, msg, t in bag.read_messages(topics=['target_ground_truth']):
        allPositions.append({
            'ts': msg.header.stamp,
            'x': msg.pose.pose.position.x
        })
    bag.close()

    # filter single column of positive events
    colNumber = 10
    colEvents = [ {
        'ts': e.ts,
        'v': e.y
    } for e in allEvents if e.x is colNumber and e.polarity is True ]

    plotX = [ e['ts'].to_sec() for e in colEvents ]
    plotY = [ e['v'] for e in colEvents ]
    pylab.plot(plotX, plotY)
    raw_input("Press Enter to continue...")

    return 0


if __name__ == "__main__":
    sys.exit(main())
