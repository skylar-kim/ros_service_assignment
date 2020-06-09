#!/usr/bin/env python

from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse

import rospy

def handle_rectangle_area(req):
    print "Returning [%s * %s = %s]"%(req.width, req.height, (req.width * req.height))
    # returns the response, contains only 1 argument
    return RectangleAreaServiceResponse(req.width * req.height)

def rectangle_area_server():
	# initializes the node with the name 'add_two_ints_server'
    rospy.init_node('rectangle_area_server')
    # start the service by listening to incoming requests
    s = rospy.Service('rectangle_area', RectangleAreaService, handle_rectangle_area)
    print "Ready to find rectangle area."
    rospy.spin()
    
if __name__ == "__main__":
    rectangle_area_server()