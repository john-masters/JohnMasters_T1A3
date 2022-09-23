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

hero = Character(input("Please enter your name: ").capitalize())

enemy_list = []

def enemy_gen():
    for x in range(5):
        name_list = ['red', 'green', 'yellow', 'blue', 'purple']
        enemyx = Enemy(f'{name_list[x].capitalize()} enemy', (random.randint((hero.level - 2), (hero.level + 2))), random.randint(5, 10))
        enemy_list.append(enemyx)

def fight(self, other):
    if self.level >= other.level:
        self.level += other.level
        self.coins += other.coins
        enemy_list.remove(other)
        print(f'{self.name} defeated {other.name.capitalize()}! You\'re now level {self.level} and you receive {other.coins} coins for winning.')
    else:
        print(f'{self.name} attacks {other.name.capitalize()} and loses...')
        self.level = 5
        self.coins = 0
        enemy_list.clear()
        enemy_gen()

def boss_battle():
    print('''
     ,     ,
    (\____/)
     (_oo_)
       (O)
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\\
(\   /____\\
    ''')
    input = 

def battle_area():
    while enemy_list != []:
        for index, enemy in enumerate(enemy_list):
            print(f'\n{index + 1}.\n {str(enemy)}')
        battle_choice = int(input(f'Choose your opponent(1-{len(enemy_list)}): '))
        if battle_choice == 1:
            fight(hero, enemy_list[0])
        elif battle_choice == 2:
            fight(hero, enemy_list[1])
        elif battle_choice == 3:
            fight(hero, enemy_list[2])
        elif battle_choice == 4:
            fight(hero, enemy_list[3])
        else:
            fight(hero, enemy_list[4])
    print('You beat the enemies')
    enemy_gen()
    print('New enemies generated')

def game():
    enemy_gen()
    print(f'Welcome to the game, {hero.name}!')
    # boss_battle()
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
