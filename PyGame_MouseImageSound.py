# Install pip:
#   Download get-pip.py
#   Then run $python get-pip.py

# Install pygame:
#   Run $pip install pygame --user
#   Test it by running $python -m pygame.examples.aliens

import pygame
import sys

pygame.init()
pygame.mixer.init()

windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)


helloWorld = pygame.image.load("assets/images/arrow.png")
helloWorldSize = helloWorld.get_size()

sound = pygame.mixer.Sound("assets/sounds/hit.wav")

pygame.mouse.set_visible(0)

x, y = 0, 0
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
    x, y = mousePosition

    if (x + helloWorldSize[0] > 800) or (x <= 0):
        x = 800 - helloWorldSize[0]
        sound.stop()
        sound.play()

    if (y + helloWorldSize[1] > 600) or (y <= 0):
        y = 600 - helloWorldSize[1]
        sound.stop()
        sound.play()

    pygame.display.update()
