import random
class Character:
    def __init__(self, name, level=5, coins=0):
        self.name = name
        self.level = level
        self.coins = coins

def fight(self, other):
    if self.level >= other.level:
        self.level += other.level
        self.coins += other.coins
        print(f'{self.name} defeated {other.name}! You\'re now level {self.level} and you receive {other.coins} coins for winning.')
        del other
    else:
        print(f'{self.name} attacks {other.name} and loses...')

def show_stats(self):
    print(f'Your level is {self.level} and you have {self.coins} coins')

class Enemy(Character):
    def __init__(self, name, level, coins):
        super().__init__(name, level, coins)

hero = Character("Hero")

enemy1 = Enemy("Enemy1",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))
enemy2 = Enemy("Enemy2",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))
enemy3 = Enemy("Enemy3",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))
enemy4 = Enemy("Enemy4",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))
enemy5 = Enemy("Enemy5",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))

def battle_area():
    for enemy in (enemy1, enemy2, enemy3, enemy4, enemy5):
        print(f'Name: {enemy.name}\nLevel: {enemy.level}\nCoins:{enemy.coins}\n')

battle_area()
