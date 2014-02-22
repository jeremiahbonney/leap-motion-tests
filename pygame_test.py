import pygame
import random
import math
from pygame.locals import *
import Leap, sys
from Leap import SwipeGesture

pygame.init()
controller = Leap.Controller()
controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

#run game at 30 frames per second
FPS = 30
FPSCLOCK = pygame.time.Clock()

#set up display
display = pygame.display.set_mode((400,400),0,32)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

playing=True

#define game state
#object coordinates
obj_x = 100
obj_y = 100

#object velocity
obj_vx = 3
obj_vy = 0

#object acceleration 
obj_ax = 0
obj_ay = 1

player_x=200
player_y=350

score=0
while playing==True:
 score+=0.12368231
 frame = controller.frame()
 #handle events
 for event in pygame.event.get():
  if event.type==QUIT:
   playing=False

 if not frame.hands.is_empty:
 	fingers = frame.fingers
 	position_x = fingers[0].tip_position[0]
 	position_y = fingers[0].tip_position[1]
 	print position_y
 	player_x = 200 + position_x
 	player_y = 500 - position_y
    # for gesture in frame.gestures():
    # 	if gesture.type == Leap.Gesture.TYPE_SWIPE:
    # 		swipe = SwipeGesture(gesture)
    # 		print swipe.direction
    # 		if swipe.direction[0] < 0:
    # 			player_x-=20
    # 		else:
    # 			player_x+=20
 #print "TEST!"
 #update state
 obj_x+=obj_vx
 obj_y+=obj_vy
 
 obj_vx+=obj_ax
 obj_vy+=obj_ay
 
 if (obj_x>350 or obj_x<10):
  obj_vx = -obj_vx

 if(obj_y>380):
  obj_x=random.randint(10,350)
  obj_vx=random.randint(-3,3)
  obj_y=0
  obj_vy=0

 dx=obj_x-player_x
 dy=obj_y-player_y
 distance=math.sqrt(dx**2+dy**2)
 if(distance<=40):
  print "nice try sucker"
  playing=False
 
 #display
 display.fill(BLACK)
 pygame.draw.circle(display,WHITE,(int(obj_x),int(obj_y)),20) 

 pygame.draw.circle(display,RED,(int(player_x),int(player_y)),20) 

 pygame.display.update()
 FPSCLOCK.tick(FPS)

print "YOUR SCORE WAS ", score
pygame.quit()
sys.exit()