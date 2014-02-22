import pygame
import random
import math
from pygame.locals import *
import Leap, sys
from Leap import SwipeGesture

pygame.init()
controller = Leap.Controller()
controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

#run game at 60 frames per second
FPS = 60
FPSCLOCK = pygame.time.Clock()

#set up display
display = pygame.display.set_mode((800,800),0,32)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

playing = True
score = 0

shot_v = 10
shot_x = 400
shot_y = 700
has_shot = False
target_x = 200
target_y = 200
pygame.draw.rect(display, RED, (400, 700, 50, 50))

while playing:
  frame = controller.frame()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  if not frame.hands.is_empty:
  	fingers = frame.fingers
  	x_pos = 400+(1.8*fingers[0].tip_position[0])
  	y_pos = 850-(1.8*fingers[0].tip_position[1])
  
  else:
  	x_pos = 400
  	y_pos = 700

  dx=shot_x - (target_x + 50)
  dy=shot_y - (target_y + 50)
  distance=math.sqrt(dx**2+dy**2)
  if distance < 40:
 	print "BOOM!"
 	shot_x = -1
 	shot_y = -1
 	target_x = -1
 	target_y = -1

  display.fill(BLACK)
  pygame.draw.rect(display, RED, (x_pos, y_pos, 50, 50))
  if shot_y > 0:
	shot_y -= shot_v
  else:
    shot_y = y_pos
    shot_x = x_pos+30
  pygame.draw.rect(display, BLUE, (shot_x, shot_y, 10, 10))
  
  if target_x < 0  or target_y < 0:
  	target_x = random.randint(10,750)
  	target_y = random.randint(0, 600)

  pygame.draw.rect(display, WHITE, (target_x, target_y, 50, 50))

  
  pygame.display.update()
  FPSCLOCK.tick(FPS)

