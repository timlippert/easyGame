import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
)

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))
player_pos = pygame.Vector2(player.topleft)
player2_pos = pygame.Vector2(400, 300)  # Initial position of the circle

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
dt = 0
running = True

while running:
    screen.fill("green")
    pygame.draw.line(screen, "blue", (0, 60), (800, 60), 5)
    dt = clock.tick(60) / 1000
    pygame.draw.rect(screen, "blue", player)
    pygame.draw.circle(screen, "blue", (int(player2_pos.x), int(player2_pos.y)), 50, 1)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player_pos.x -= 300 * dt
        player2_pos.x -= 100 * dt

    elif key[pygame.K_d]:
        player_pos.x += 300 * dt
        player2_pos.x += 100 * dt

    if key[pygame.K_w]:
        player_pos.y -= 300 * dt
        player2_pos.y -= 100 * dt

    if key[pygame.K_s]:
        player_pos.y += 300 * dt
        player2_pos.y += 100 * dt

    player.topleft = (int(player_pos.x), int(player_pos.y))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            player_pos.x = pos[0]
            player_pos.y = pos[1]
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
        if pygame.mouse.get_pressed()[2]:
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                player_pos.x = pos[0]
                player_pos.y = pos[1]
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()