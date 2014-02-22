import Leap, sys
from Leap import SwipeGesture
import pygame

class SwipeListener(Leap.Listener):

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):

        print "Exited"

    def on_frame(self, controller):
    	frame = controller.frame()
    	#print frame

    	if not frame.hands.is_empty:
    		for gesture in frame.gestures():
    			if gesture.type == Leap.Gesture.TYPE_SWIPE:
    				swipe = SwipeGesture(gesture)
    				print "Swipe direction was: ", swipe.direction

    	

def main():
    # Create a sample listener and controller
    listener = SwipeListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    sys.stdin.readline()

    # Remove the sample listener when done
    controller.remove_listener(listener)

main()
