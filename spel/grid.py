class GridTile:
    def __init__(self, xCoordinate: int, yCoordinate: int, terrain: str):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.terrain = terrain
        self.unit = None
        self.marking = None
