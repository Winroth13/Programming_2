import pygame


class Unit:
    def __init__(self, maxMovement: int, allegiance: str):
        print("New unit created.")
        self.currentMovement = 0
        self.allegiance = allegiance

    def draw(self, window, xPos, yPos, tileWidth, tileHeight, allegiances):
        pygame.draw.rect(
            window,
            allegiances[self.allegiance],
            [xPos + 5, yPos + 5, tileWidth - 10, tileHeight - 10],
        )
