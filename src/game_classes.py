import random

class Character:
    def __init__(self, name, level=5, coins=0):
        self.name = name
        self.level = level
        self.coins = coins

    def __str__(self):
        return f'Name: {self.name}\nLevel: {self.level}\nCoins:{self.coins}\n'

    def fight(self, other):
        if self.level >= other.level:
            self.level += other.level
            self.coins += other.coins
            print(f'{self.name} defeated {other.name}! You\'re now level {self.level} and you receive {other.coins} coins for winning.')
            del other
            enemy_list.remove(other)
        else:
            print(f'{self.name} attacks {other.name} and loses...')

class Enemy(Character):
    def __init__(self, name, level, coins):
        super().__init__(name, level, coins)

    def __str__(self):
        return f'Name: {self.name}\nLevel: {self.level}\nCoins:{self.coins}\n'


hero = Character(input("Please enter your name: "))

enemy1 = Enemy(
    "Enemy1",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
)
enemy2 = Enemy(
    "Enemy2",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )
enemy3 = Enemy(
    "Enemy3",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )
enemy4 = Enemy(
    "Enemy4",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )
enemy5 = Enemy(
    "Enemy5",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )

enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5]

def battle_area():
    for enemy in enemy_list:
        print(enemy.__str__())
    battle_choice = input('Choose your opponent(1-5): ')
    if battle_choice == 1:
        Character.fight(hero, enemy1)
    elif battle_choice == 2:
        Character.fight(hero, enemy2)
    elif battle_choice == 3:
        Character.fight(hero, enemy3)
    elif battle_choice == 4:
        Character.fight(hero, enemy4)
    else:
        Character.fight(hero, enemy5)
