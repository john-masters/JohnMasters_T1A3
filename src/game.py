import random

class Player:
    def __init__(self, name, level=5, coins=0):
        self.name = name
        self.level = level
        self.coins = coins

    def fight(self, other):
        if self.level >= other.level:
            self.level += other.level
            self.coins += other.coins
        else:
            pass

class Enemy(Player):
    def __init__(self, name, level, coins=5):
        super().__init__(name, level, coins)

class Boss(Player):
    def __init__(self, name, level, coins=50):
        super().__init__(name, level, coins)

def game():
   hero = Player(input("Please enter your name:"))