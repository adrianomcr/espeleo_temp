#!/usr/bin/python
import rospy
from math import sqrt
import numpy as np
import cv2
import yaml
#from scipy.optimize import linear_sum_assignment

from visualization_msgs.msg import Marker
from tf2_msgs.msg import TFMessage
from sensor_msgs.msg import CameraInfo
from tf.transformations import *


H_c_r = np.matrix([[0.0, 0.0, 1.0, 0.2],[-1.0, 0.0, 0.0, 0.0],[0.0, -1.0, 0.0, 0.0],[0.0, 0.0, 0.0, 1.0]]);

print "H_c_r = ", H_c_r



#H_a_w_list = [];

def callback_aruco(data):

    global H_a_w_list

    aruco_id = data.id
    px = data.pose.position.x
    py = data.pose.position.y
    pz = data.pose.position.z
    qw = data.pose.orientation.w
    qx = data.pose.orientation.x
    qy = data.pose.orientation.y
    qz = data.pose.orientation.z



    H_a_w = H_a_w_list[aruco_id-1];
    #H_a_c = np.matrix([[1.0, 0.0, 0.0, 0.2],[0.0, 1.0, 0.0, 0.0],[0.0, 0.0, 1.0, 0.0],[0.0, 0.0, 0.0, 1.0]]);


    #H_r_w = H_a_w*H_a_c.inverse()*H_c_r.inverse();


    print "H_a_w = ", H_a_w





def main():

  rospy.init_node("aruco_node")

  rospy.Subscriber("/visualization_marker", Marker, callback_aruco)

  rate = rospy.Rate(100.0)


  while not rospy.is_shutdown():
    rate.sleep()






# Funcao inicial
if __name__ == '__main__':


    global H_a_w_list

    H_a_w_list = []
    H1 = np.matrix([[-0.000000,0.000000,-1.000000,3.000000],[-1.000000,0.000000,0.000000,2.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H1)
    H2 = np.matrix([[-0.000000,0.000000,-1.000000,5.000000],[-1.000000,0.000000,0.000000,0.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H2)
    H3 = np.matrix([[-0.000000,0.000000,-1.000000,7.000000],[-1.000000,0.000000,0.000000,2.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H3)
    H4 = np.matrix([[-0.000000,0.000000,-1.000000,9.000000],[-1.000000,0.000000,0.000000,0.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H4)
    H5 = np.matrix([[-0.000000,0.000000,-1.000000,11.000000],[-1.000000,0.000000,0.000000,2.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H5)
    H6 = np.matrix([[-0.000000,0.000000,-1.000000,13.000000],[-1.000000,0.000000,0.000000,0.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H6)
    H7 = np.matrix([[-0.000000,0.000000,-1.000000,15.000000],[-1.000000,0.000000,0.000000,2.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H7)
    H8 = np.matrix([[-0.000000,0.000000,-1.000000,17.000000],[-1.000000,0.000000,0.000000,0.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H8)
    H9 = np.matrix([[-0.000000,0.000000,-1.000000,19.000000],[-1.000000,0.000000,0.000000,2.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H9)
    H10 = np.matrix([[-0.000000,0.000000,-1.000000,21.000000],[-1.000000,0.000000,0.000000,0.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H10)
    H11 = np.matrix([[-0.000000,0.000000,-1.000000,23.000000],[-1.000000,0.000000,0.000000,2.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H11)
    H12 = np.matrix([[-0.000000,0.000000,-1.000000,25.000000],[-1.000000,0.000000,0.000000,0.120000],[0.000000,1.000000,0.000000,0.110000],[0.0,0.0,0.0,1.0]])
    H_a_w_list.append(H12)


    try:
        main()
    except rospy.ROSInterruptException:
        pass
