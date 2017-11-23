# Install pip:
#   Download get-pip.py
#   Then run $python get-pip.py

# Install pygame:
#   Run $pip install pygame --user
#   Test it by running $python -m pygame.examples.aliens

import pygame
import sys

pygame.init()

windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)
helloWorld = myriadProFont.render("Hello World!", 1, (255, 0, 255), (255, 255, 255))
helloWorldSize = helloWorld.get_size()

x = 10
y = 10
directionX = 1
directionY = 1
clock = pygame.time.Clock()

while 1:
    # run 40 frames per second
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(helloWorld, (x, y))

    mousePosition = pygame.mouse.get_pos()
    x , y = mousePosition

    if (x + helloWorldSize[0] > 800) or (x <= 0):
        x = 800 - helloWorldSize[0]

    if (y + helloWorldSize[1] > 600) or (y <= 0):
        y = 600 - helloWorldSize[1]

    pygame.display.update()
