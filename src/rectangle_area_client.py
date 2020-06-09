#!/usr/bin/env python

import sys
import rospy
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

# the rectangle_area_client is responsible for 
# formulating the request and sending the request to the server
def rectangle_area_client(x, y):
    # first, wait for the service; must make sure server is awake
    # server is defined by the name of the service
    # server name is similar in function to the topic name
    rospy.wait_for_service('rectangle_area')
    try:
        # rospy.ServiceProxy() is responsible for sending the request
        # to the service and specifying the type of the service (RectangleAreaService)
        rectangle_area = rospy.ServiceProxy('rectangle_area', RectangleAreaService)
        resp1 = rectangle_area(x, y)
        return resp1.area
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        # read x and y from the arguments of the rosrun command line
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    # print x and y values 
    print "Requesting %s*%s"%(x, y)
    # execute a method called rectangle_area_client
    s = rectangle_area_client(x, y)
    print "%s * %s = %s"%(x, y, s)