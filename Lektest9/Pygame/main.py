import pygame
import matplotlib as plot

from movingObject import MovingObject

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.Info()

windowWidth = display.current_w
windowHeight = display.current_h

centerX = windowWidth / 2
centerY = windowHeight / 2

playerSpeed = 5

window = pygame.display.set_mode((windowWidth, windowHeight))

player = MovingObject(centerX, centerY, (0, 0), (255, 255, 255), 20, window)


def init():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q:
                        return
                    case pygame.K_w:
                        player.velocity[1] -= playerSpeed
                    case pygame.K_a:
                        player.velocity[0] -= playerSpeed
                    case pygame.K_s:
                        player.velocity[1] += playerSpeed
                    case pygame.K_d:
                        player.velocity[0] += playerSpeed

            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_w:
                        player.velocity[1] += playerSpeed
                    case pygame.K_a:
                        player.velocity[0] += playerSpeed
                    case pygame.K_s:
                        player.velocity[1] -= playerSpeed
                    case pygame.K_d:
                        player.velocity[0] -= playerSpeed

        window.fill((0, 0, 0))

        player.update()

        pygame.display.update()

        clock.tick(60)


init()
