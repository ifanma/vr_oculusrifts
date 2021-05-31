#!/usr/bin/python

import rospy
import Xlib
import Xlib.display

rospy.init_node("relocate_resize_window")

display = Xlib.display.Display()
root = display.screen().root

screen_width = rospy.get_param('relocate_resize_window/current_screen_width', 3840)
cam_w = rospy.get_param('relocate_resize_window/window_config_width', 2146)
cam_h = rospy.get_param('relocate_resize_window/window_config_height', 1062)
openhmd_label = rospy.get_param('relocate_resize_window/window_name', '/openhmd/stereo')

print(openhmd_label)
while True:
	windowIDs = root.get_full_property(display.intern_atom('_NET_CLIENT_LIST'), Xlib.X.AnyPropertyType).value

	found = False
	for windowID in windowIDs:
		window = display.create_resource_object('window', windowID)
		name = window.get_wm_name()
		# print(name)
		pid = window.get_full_property(display.intern_atom('_NET_WM_PID'), Xlib.X.AnyPropertyType) # PID
		if name == openhmd_label:
			found = True
			print(screen_width)
			print(cam_w)
			print(cam_h)

			print("[DEBUG]: Window with label %s found!" %openhmd_label)
			window.configure(x=1920, y=0, width=cam_w, height=cam_h)
			display.sync()
			wdata = window.get_geometry()._data
			print("[DEBUG]: Window config" ) 
			print(wdata)

	if not found:
		print('[ERROR]: Window with label %s was not found.'%openhmd_label)
	else:
		break