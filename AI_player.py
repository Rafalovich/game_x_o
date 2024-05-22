import random

class AIPlayer:

    def __init__(self, value):
        self.value = value

    def get_move(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return (row, col)