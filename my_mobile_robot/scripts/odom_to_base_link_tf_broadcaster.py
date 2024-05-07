#!/usr/bin/env python

import rospy
import tf2_ros
import geometry_msgs.msg
import tf.transformations

def broadcast_odom_to_base_link():
    rospy.init_node('odom_to_base_link_tf_broadcaster')
    
    # Set up the transform broadcaster
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    # Set parent and child frames
    t.header.frame_id = 'odom'
    t.child_frame_id = 'base_footprint'

    # Set the translation and rotation of the transform
    t.transform.translation.x = 0.0
    t.transform.translation.y = 0.0
    t.transform.translation.z = 0.0

    # Set a valid quaternion (no rotation in this case)
    t.transform.rotation.x = 0.0
    t.transform.rotation.y = 0.0
    t.transform.rotation.z = 0.0
    t.transform.rotation.w = 1.0

    rate = rospy.Rate(100.0)
    while not rospy.is_shutdown():
        t.header.stamp = rospy.Time.now()
        br.sendTransform(t)
        rate.sleep()

if __name__ == '__main__':
    try:
        broadcast_odom_to_base_link()
    except rospy.ROSInterruptException:
        pass
