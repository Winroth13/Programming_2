import pygame


class MovingObject:
    def __init__(self, posX, posY, velocity, colour, radius, window):
        self.posX = posX
        self.posY = posY
        self.velocity = list(velocity)
        self.colour = colour
        self.radius = radius
        self.window = window

    def update(self):
        self.posX += self.velocity[0]
        self.posY += self.velocity[1]

        pygame.draw.circle(
            self.window, self.colour, (self.posX, self.posY), self.radius
        )
