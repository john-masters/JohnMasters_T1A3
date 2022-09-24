import random
import sys
import time

class Character:
    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def __str__(self):
        return f'Name: {self.name}\nLevel: {self.level}\n'

class Enemy(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

class Boss(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

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
\nName: {self.name}\nLevel: {self.level}\n
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
        enemyx = Enemy(f'{name_list[x].capitalize()} enemy', (random.randint((hero.level - 4), (hero.level + 4))))
        enemy_list.append(enemyx)

def fight(self, other):
    if self.level >= other.level:
        self.level += other.level
        enemy_list.remove(other)
        print(f'{self.name} defeated {other.name.capitalize()}! You\'re now level {self.level}.')
    else:
        print(f'{self.name} attacks {other.name.capitalize()} and loses...')
        sys.exit("Thank you for playing. Better luck next time!")

def boss_fight(self, other):
    if self.level >= other.level:
        self.level += other.level
        print(f'{self.name} defeated {other.name.capitalize()}! You\'re now level {self.level}.')
        del other
        enemy_list.clear()
    else:
        print(f'{self.name} attacks {other.name.capitalize()} and loses...')
        sys.exit("Thank you for playing. Better luck next time!")

def battle_area():
    while enemy_list != []:
        for index, enemy in enumerate(enemy_list):
            print(f'\n{index + 1}.\n {str(enemy)}')
        battle_choice = int(input(f'Choose your opponent(1-{len(enemy_list)}): '))
        fight(hero, enemy_list[battle_choice - 1])
    print(f'You beat the enemies, and a {boss.name} appears...\n{str(boss)}')
    boss_fight(hero, boss)

def game():
    # time1 = time.time()
    # print(f'Welcome to the game, {hero.name}!')
    # input('Hit enter to continue')
    # for i in range(3):
    #     boss_gen(i + 1)
    #     enemy_gen()
    #     while enemy_list != []:
    #         action = input('Please enter one of the following commands (battle, stats or scores): ')
    #         if action == 'battle':
    #             battle_area()
    #         elif action == 'stats':
    #             print(hero)
    #         elif action == 'scores':
    #             with open('docs/scores.txt', 'r') as file:
    #                 print(file.read())
    #         else:
    #             action = 'Please enter one of the following (battle, stats or scores): '
    # time_result = round((time.time()) - time1)
    # with open('docs/scores.txt', 'a') as file:
    #     file.write(f'{hero.name}: {time_result}\n')
    # print(f'Congratulations, {hero.name}! You won in {time_result} seconds!')
    with open('docs/scores.txt', 'r') as file:
        data = file.read()
        print(data)
        data_list = (data.split('\n'))
        data_list.pop()
        new_list = []
        for data in data_list:
            new_list.append(data.split(': '))
        sorted_list = sorted(new_list, key = lambda x: x[1])
        print(sorted_list)


game()
