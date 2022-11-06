import random


class Player:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Dice:

    @staticmethod
    def roll_dice():
        return random.randrange(1, 7)


d = Dice()
print(d.roll_dice())
