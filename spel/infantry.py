from unit import Unit


class Infantry(Unit):
    def __init__(self, allegiance: str):
        self.maxMovement = 2
        super().__init__(self.maxMovement, allegiance)
