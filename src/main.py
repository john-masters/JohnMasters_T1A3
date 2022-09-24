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

class Boss(Character):
    def __init__(self, name, level, coins=50):
        super().__init__(name, level, coins)

    def __str__(self):
        return f'''
     ,     ,
    (\____/)
     (_oo_)
       (O)
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\\
(\   /____\\
\nName: {self.name}\nLevel: {self.level}\nCoins: {self.coins}\n
        '''

boss = None

def boss_gen(x):
    global boss
    if x == 1:
        level = 'bronze'
    elif x == 2:
        level = 'silver'
    elif x == 3:
        level = 'gold'
    boss = Boss((level + ' devil').title(), hero.level * 6)

hero = Character(input("Please enter your name: ").capitalize())

enemy_list = []

def enemy_gen():
    for x in range(5):
        name_list = ['red', 'green', 'yellow', 'blue', 'purple']
        enemyx = Enemy(f'{name_list[x].capitalize()} enemy', (random.randint((hero.level - 4), (hero.level + 4))), random.randint(5, 11))
        enemy_list.append(enemyx)

def fight(self, other):
    if self.level >= other.level:
        self.level += other.level
        self.coins += other.coins
        if other in enemy_list:
            enemy_list.remove(other)
        print(f'{self.name} defeated {other.name.capitalize()}! You\'re now level {self.level} and you receive {other.coins} coins for winning.')
    else:
        print(f'{self.name} attacks {other.name.capitalize()} and loses...')
        self.level = 5
        self.coins = 0
        enemy_list.clear()
        enemy_gen()

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
    print(f'You beat the enemies, and the boss appears...\n{str(boss)}')
    fight(hero, boss)

# TODO: Add a for loop that will move the boss attr forward by 1 each time, and only loop 3 times and then you win
def game():
    loop_num = 0
    for i in range(3):
        enemy_gen()
        boss_gen(loop_num + 1)
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
        loop_num += 1

game()
