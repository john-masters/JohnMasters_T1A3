import random

class Character:
    def __init__(self, name, level=5, coins=0):
        self.name = name
        self.level = level
        self.coins = coins

    def __str__(self):
        return f'Name: {self.name}\nLevel: {self.level}\nCoins: {self.coins}\n'

class Enemy(Character):
    def __init__(self, name, level, coins):
        super().__init__(name, level, coins)

hero = Character(input("Please enter your name: "))

enemy_list = []

for x in range(5):
    enemyx = Enemy(f'Enemy{x+1}', (random.randint((hero.level - 2), (hero.level + 2))), random.randint(5, 10))
    enemy_list.append(enemyx)

# for x in range(len(enemy_list)):
#     print(enemy_list[x])

print(enemy_list[0])
