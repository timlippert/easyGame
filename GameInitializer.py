import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEMOTION
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
clock = pygame.time.Clock()
player_pos = pygame.Vector2(player.topleft)
dt = 0
running = True
while running:
    dt = clock.tick(60) / 1000
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player_pos.x -= 300 * dt

    elif key[pygame.K_d]:
        player_pos.x += 300 * dt

    if key[pygame.K_w]:
        player_pos.y -= 300 * dt

    if key[pygame.K_s]:
        player_pos.y += 300 * dt

    player.topleft = (int(player_pos.x), int(player_pos.y))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            player_pos.x = pos[0]
            player_pos.y = pos[1]
            #print(pos)
        if event.type == MOUSEBUTTONDOWN:
            holding = True
            if event.type == MOUSEMOTION:
                while holding:
                    pos = pygame.mouse.get_pos()
                    player_pos.x = pos[0]
                    player_pos.y = pos[1]
                    if event.type != MOUSEMOTION:
                        holding = False
            pos = pygame.mouse.get_pos()
            player_pos.x = pos[0]
            player_pos.y = pos[1]
        #if event.type == MOUSEMOTION:
         #   pos = pygame.mouse.get_pos()
          #  player_pos.x = pos[0]
           # player_pos.y = pos[1]
        if event.type == pygame.QUIT:
            running = False 
    pygame.display.update()
pygame.quit()



