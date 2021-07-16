#!/usr/bin/env python
# coding=utf-8

# /* ----------------------------------------------------------------------------
#  * Copyright 2020, Jesus Tordesillas Torres, Aerospace Controls Laboratory
#  * Massachusetts Institute of Technology
#  * All Rights Reserved
#  * Authors: Jesus Tordesillas, et al.
#  * See LICENSE file for the license information
#  * -------------------------------------------------------------------------- */


import math
import os
import sys
import time
from random import *
# import numpy as np
# from pyquaternion import Quaternion
from tf.transformations import quaternion_from_euler, euler_from_quaternion

def sendCommand(action,quad,x,y,z,goal_x,goal_y,goal_z, yaw):
    if(action=="start"):
        #Kota comment: this line launches mader_specific.launch
        os.system("roslaunch mader mader_specific.launch gazebo:=false quad:="+quad+" x:="+str(x)+" y:="+str(y)+" z:="+str(z)+" yaw:="+str(yaw)); 
    if(action=="mader"):
        os.system("roslaunch mader mader.launch quad:="+quad) #Kota comment: this line launches mader.launch with the argument of quad number
    if(action=="send_goal"):
        os.system("rostopic pub /"+quad+"/term_goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: 'world'}, pose: {position: {x: "+str(goal_x)+", y: "+str(goal_y)+", z: "+str(goal_z)+"}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 0.0}}}'")
    
        
if __name__ == '__main__':

    # set quad number, initial positions, and goals (for now, manually)

    # agent1 (NUC1)
    quad="SQ01s";
    x = 10;
    y = 0;
    z = 1.0;
    yaw = 0;
    goal_x = -10;
    goal_y = 0;
    goal_z = 1.0;

    # agent2 (NUC2)
    #quad="SQ02s";
    #x = -10
    #y = 0
    #z = 1.0
    #yaw = math.pi;
    #goal_x = 10;
    #goal_y = 0;
    #goal_z = 1.0;

    sendCommand(sys.argv[1],quad,x,y,z,goal_x,goal_y,goal_z, yaw);

    x_tmp="{:5.3f}".format(x);
    y_tmp="{:5.3f}".format(y);
    z_tmp="{:5.3f}".format(z);

    goal_x_tmp="{:5.3f}".format(goal_x);
    goal_y_tmp="{:5.3f}".format(goal_y);
    goal_z_tmp="{:5.3f}".format(goal_z);
 
    print (' "start": [',x_tmp,', ',y_tmp,', ',z_tmp,'], "goal": [',goal_x_tmp,', ',goal_y_tmp,', ',goal_z_tmp,']  ')

    if(sys.argv[1]!="send_goal"):
        time.sleep(1); #Kota added to make this "if statement" works even when i comment out the above line
    else: ##if send_goal, kill after some time
        time.sleep(num_of_agents); #The more agents, the more I've to wait to make sure the goal is sent correctly