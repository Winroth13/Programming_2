import pygame
import math

from grid import GridTile
from infantry import Infantry

pygame.init()

mapWidth = 500
windowHeight = 500
numberOfTilesX = 10
numberOfTilesY = 10
innerMargin = 1

menuWidth = 200
buttonWidth = 150
buttonHeight = 40

textFont = pygame.font.SysFont("monoscape", 50)

mouseClicked = False

buttons = []

windowWidth = mapWidth + menuWidth

allegiances = {"blufor": (0, 0, 175), "opfor": (175, 0, 0)}

# Terrain and marking colous
terrainTiles = {
    "open": {"colour": (0, 175, 0), "passable": True},
    "mountain": {"colour": (125, 125, 125), "passable": True},
    "water": {"colour": (0, 0, 255), "passable": False},
}
markingColour = {
    "selected": (255, 255, 0),
    "move": (0, 0, 150),
    "attack": (255, 0, 0),
}

# Creating all map tiles
grid = []
for Y in range(numberOfTilesY):
    for X in range(numberOfTilesX):
        if Y == 0 or Y == numberOfTilesY - 1 or X == 0 or X == numberOfTilesX - 1:
            terrain = "water"
        else:
            terrain = "open"
        grid.append(GridTile(X, Y, terrain))

# The width and height of the map tiles
tileWidth = math.floor((mapWidth - innerMargin * (numberOfTilesX + 1)) / numberOfTilesX)
tileHeight = math.floor(
    (windowHeight - innerMargin * (numberOfTilesY + 1)) / numberOfTilesY
)

# The margins around the tile map
outerMarginX = (
    mapWidth - (numberOfTilesX * tileWidth + (numberOfTilesX - 1) * innerMargin)
) / 2
outerMarginY = (
    windowHeight - (numberOfTilesY * tileHeight + (numberOfTilesY - 1) * innerMargin)
) / 2


# Calculates a grid tile's index
def gridByCoordinates(x: int, y: int):
    return grid[x + y * numberOfTilesX]


# Calculates the coordinates of the top left corner of a tile
def gridTopLeft(xCoordinate: int, yCoordinate: int) -> float:
    xPos = (tileWidth + innerMargin) * xCoordinate + outerMarginX
    yPos = (tileHeight + innerMargin) * yCoordinate + outerMarginY
    return (xPos, yPos)


# Updating grid markings
def updateGridMarkings():
    # Runs through all grid tiles
    for gridTile in grid:
        gridTile.marking = None

        # Sets the marked tile
        if mouseX == gridTile.xCoordinate and mouseY == gridTile.yCoordinate:
            gridTile.marking = "selected"

        # Generating movememnt when unit is selected
        if selectedSquare.unit != None:
            if (
                abs(mouseX - gridTile.xCoordinate) + abs(mouseY - gridTile.yCoordinate)
                <= selectedSquare.unit.currentMovement
            ):
                if (
                    gridTile.xCoordinate != mouseX or gridTile.yCoordinate != mouseY
                ) and terrainTiles[gridTile.terrain]["passable"] == True:
                    if gridTile.unit == None:
                        gridTile.marking = "move"
                    elif gridTile.unit.allegiance != selectedSquare.unit.allegiance:
                        gridTile.marking = "attack"
                print(gridTile.xCoordinate, gridTile.yCoordinate)


# Mouse clicks
def onMouseDown():
    # Gets the position of the mouse
    mousePos = pygame.mouse.get_pos()

    mousePosX = mousePos[0]
    mousePosY = mousePos[1]

    if mousePosX <= mapWidth:
        clickOnMap(mousePosX, mousePosY)
    else:
        clickOnSidemenu(mousePosX, mousePosY)


def clickOnMap(mousePosX: int, mousePosY: int):
    global selectedSquare
    global mouseX
    global mouseY

    # The outer margin was clicked
    if (
        mousePosX <= outerMarginX
        or mousePosX >= mapWidth - outerMarginX
        or mousePosY <= outerMarginY
        or mousePosY >= windowHeight - outerMarginY
    ):
        return

    mouseX = int(mousePosX // (tileWidth + innerMargin))
    mouseY = int(mousePosY // (tileHeight + innerMargin))

    # When there is no selected unit
    if selectedSquare == None or selectedSquare.unit == None:
        selectedSquare = gridByCoordinates(mouseX, mouseY)
        print("New selected square")
    # When there is a selected unit
    else:
        newSelectedSquare = gridByCoordinates(mouseX, mouseY)

        # If you can move to selected tile
        match newSelectedSquare.marking:
            case "move":
                selectedSquare.unit.currentMovement -= abs(
                    selectedSquare.xCoordinate - newSelectedSquare.xCoordinate
                ) + abs(selectedSquare.yCoordinate - newSelectedSquare.yCoordinate)

                newSelectedSquare.unit = selectedSquare.unit
                selectedSquare.unit = None
            case "attack":
                selectedSquare.unit.currentMovement = 0

                newSelectedSquare.unit = selectedSquare.unit
                selectedSquare.unit = None

        selectedSquare = newSelectedSquare

    updateGridMarkings()


def clickOnSidemenu(mousePosX: int, mousePosY: int):
    for button in buttons:
        if (
            mousePosX >= button["RectValue"][0]
            and mousePosX <= button["RectValue"][0] + button["RectValue"][2]
            and mousePosY >= button["RectValue"][1]
            and mousePosY <= button["RectValue"][1] + button["RectValue"][3]
        ):
            exec(button["Function"])


def updateMap():
    global selectedSquare

    window.fill((0, 0, 0))

    for gridTile in grid:
        pygame.draw.rect(
            window,
            terrainTiles[gridTile.terrain]["colour"],
            [
                (tileWidth + innerMargin) * gridTile.xCoordinate + outerMarginX,
                (tileHeight + innerMargin) * gridTile.yCoordinate + outerMarginY,
                tileWidth,
                tileHeight,
            ],
        )
        if gridTile.marking != None:
            pygame.draw.rect(
                window,
                markingColour[gridTile.marking],
                [
                    (tileWidth + innerMargin) * gridTile.xCoordinate + outerMarginX,
                    (tileHeight + innerMargin) * gridTile.yCoordinate + outerMarginY,
                    tileWidth,
                    tileHeight,
                ],
                3,
            )
        if gridTile.unit != None:
            coordinates = gridTopLeft(gridTile.xCoordinate, gridTile.yCoordinate)
            gridTile.unit.draw(
                window,
                coordinates[0],
                coordinates[1],
                tileWidth,
                tileHeight,
                allegiances,
            )

    drawSideMenu()

    pygame.display.update()


def generateMap():
    # Creating terrain
    gridByCoordinates(6, 6).terrain = "mountain"
    gridByCoordinates(6, 5).terrain = "water"


def generateUnits():
    gridByCoordinates(1, 5).unit = Infantry("blufor")
    gridByCoordinates(1, 6).unit = Infantry("blufor")

    gridByCoordinates(numberOfTilesX - 2, 5).unit = Infantry("opfor")
    gridByCoordinates(numberOfTilesX - 2, 6).unit = Infantry("opfor")


def drawText(text: str, leftX: int, topY: int):
    textString = textFont.render(str(text), 1, (0, 0, 0))

    window.blit(textString, (leftX, topY))


def addButton(text: str, RectValue: int, function: str):
    pygame.draw.rect(window, (255, 255, 255), RectValue)

    buttons.append(
        {
            "RectValue": RectValue,
            "Function": function,
        }
    )

    drawText("End turn", RectValue[0], RectValue[1])


def drawSideMenu():
    global buttons

    buttons = []

    buttonLeftX = mapWidth + (menuWidth - buttonWidth) / 2
    buttonTopY = windowHeight - 20 - buttonHeight

    addButton(
        "End Turn",
        [
            buttonLeftX,
            buttonTopY,
            buttonWidth,
            buttonHeight,
        ],
        "endTurn()",
    )


def endTurn():
    print("New turn")

    global currentPlayer
    global selectedSquare

    currentPlayerIndex = list(allegiances).index(currentPlayer)
    selectedSquare = None

    if currentPlayerIndex != len(allegiances) - 1:
        currentPlayer = list(allegiances)[currentPlayerIndex + 1]
    else:
        currentPlayer = list(allegiances)[0]

    for gridTile in grid:
        if gridTile.unit != None:
            if gridTile.unit.allegiance == currentPlayer:
                gridTile.unit.currentMovement = gridTile.unit.maxMovement
            else:
                gridTile.unit.currentMovement = 0


def init():
    global currentPlayer
    global mouseClicked

    generateMap()
    generateUnits()

    currentPlayer = list(allegiances)[-1]

    endTurn()
    updateMap()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                onMouseDown()
                updateMap()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return
                elif event.key == pygame.K_SPACE:
                    endTurn()
                    updateMap()


window = pygame.display.set_mode((windowWidth, windowHeight))

init()
