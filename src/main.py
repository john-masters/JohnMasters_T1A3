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
        enemy_list.remove(other.name)
        print(f'{self.name} defeated {other.name.capitalize()}! You\'re now level {self.level} and you receive {other.coins} coins for winning.')
    else:
        print(f'{self.name} attacks {other.name.capitalize()} and loses...')

class Enemy(Character):
    def __init__(self, name, level, coins):
        super().__init__(name, level, coins)

    def __str__(self):
        return f'Name: {self.name.capitalize()}\nLevel: {self.level}\nCoins:{self.coins}\n'

def battle_area():
    for enemy in enemy_list:
        print(str(enemy))
    battle_choice = input('Choose your opponent(1-5): ')
    if battle_choice == 1:
        fight(hero, enemy1)
    elif battle_choice == 2:
        fight(hero, enemy2)
    elif battle_choice == 3:
        fight(hero, enemy3)
    elif battle_choice == 4:
        fight(hero, enemy4)
    else:
        fight(hero, enemy5)

hero = Character(input("Please enter your name: "))

enemy1 = Enemy(
    "enemy1",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
)
enemy2 = Enemy(
    "enemy2",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )
enemy3 = Enemy(
    "enemy3",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )
enemy4 = Enemy(
    "enemy4",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )
enemy5 = Enemy(
    "enemy5",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )

enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5]

def game():
    print(f'Welcome to the game, {hero.name}!')
    won = False
    while won is False:
        action = input('Please enter one of the following commands (battle, shop, stats or scores): ')
        if action == 'battle':
            battle_area()
        elif action == 'shop':
            pass
        elif action == 'stats':
            print(hero)
        elif action == 'scores':
            pass
        else:
            action = 'Please enter one of the following (battle, shop, stats or scores): '

game()
