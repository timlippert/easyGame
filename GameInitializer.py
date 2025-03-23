import pygame
from pygame.examples.grid import Player
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
player = pygame.Rect((300,250,50,50))
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
running = True
while running:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)

    elif key[pygame.K_d]:
            player.move_ip(1, 0)

    if key[pygame.K_w]:
        player.move_ip(0, -1)

    if key[pygame.K_s]:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.display.update()
pygame.quit()



