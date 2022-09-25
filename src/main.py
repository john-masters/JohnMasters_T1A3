import random
import sys
import time
import csv
import os

class Character:
    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def __str__(self):
        return f'Name: {self.name}\nLevel: {self.level}'

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
\nName: {self.name}\nLevel: {self.level}
        '''

boss = None

# Creates a boss character which is the equivalent of 6 times the player's level'
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

# Create a list of 5 enemies, with levels relative to player level and adds them to list for reference
def enemy_gen():
    for x in range(5):
        name_list = ['red', 'green', 'yellow', 'blue', 'purple']
        enemyx = Enemy((name_list[x] + ' enemy').title(), (random.randint((hero.level - 4), (hero.level + 4))))
        enemy_list.append(enemyx)

# Method for fighting with regular enemies 
# If you win, the enemy level is added to yours and the enemy is removed from list. 
# If you lose, game over
def fight(self, other):
    if self.level >= other.level:
        self.level += other.level
        enemy_list.remove(other)
        print(f'{self.name} defeated {other.name.capitalize()}! You\'re now level {self.level}.')
    else:
        print(f'{self.name} attacks {other.name.capitalize()} and loses...')
        sys.exit("Thank you for playing. Better luck next time!")

# Method for fighting the bosses
# If you win, the enemy level is added to yours and the boss is deleted, and the enemy list is cleared.
# If you lose, game over
def boss_fight(self, other):
    if self.level >= other.level:
        self.level += other.level
        print(f'{self.name} defeated the {other.name}! You\'re now level {self.level}.')
        del other
        enemy_list.clear()
    else:
        print(f'{self.name} attacks the {other.name} and loses...')
        sys.exit("Thank you for playing. Better luck next time!")

# Area where the enemy list is printed and the player chooses who to fight.
# Once the enemies are defeated, the player will fight the boss
def battle_area():
    print('--- BATTLE ARENA ---')
    while enemy_list != []:
        for index, enemy in enumerate(enemy_list):
            print(f'{index + 1}.\n {str(enemy)}\n')
        battle_choice = int(input(f'Choose your opponent(1-{len(enemy_list)}): '))
        os.system('cls' if os.name == 'nt' else 'clear')
        fight(hero, enemy_list[battle_choice - 1])
    print(f'You beat the enemies, and a {boss.name} appears...\n{str(boss)}')
    boss_fight(hero, boss)

# The main game function. The player chooses between battling, checking their stats, or checking the high scores
def game():
    time1 = time.time()
    print(f'Welcome to the game, {hero.name}! You\'re level {hero.level}. Good luck!')
    for i in range(3):
        boss_gen(i + 1)
        enemy_gen()
        while enemy_list != []:
            action = input('Please enter one of the following commands (battle, stats or scores): ')
            if action == 'battle':
                os.system('cls' if os.name == 'nt' else 'clear')
                battle_area()
            elif action == 'stats':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--- YOUR STATS ---')
                print(hero)
            elif action == 'scores':
                os.system('cls' if os.name == 'nt' else 'clear')
                with open ('docs/scores.csv') as file:
                    reader = csv.reader(file)
                    print('--- TOP 5 SCORES ---')
                    reader.__next__()
                    counter = 0
                    for row in reader:
                        if counter != 5:
                            print(f'{row[0]} beat the game in {row[1]} seconds')
                            counter += 1
                        else:
                            break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                action = 'Please enter one of the following (battle, stats or scores): '
    time_result = round((time.time()) - time1)
    # Writes score to score list CSV
    with open('docs/scores.csv', 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([hero.name,time_result])
    print(f'Congratulations, {hero.name}! You won in {time_result} seconds!')
    # Sort scores list CSV
    with open('docs/scores.csv') as file:
        reader = csv.reader(file)
        reader.__next__() # Skip the first row (the column names)
        data = sorted(csv.reader(file), key = lambda x: x[1])
    # Writes the sorted scores to the list CSV
    with open('docs/scores.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(['name','score'])
        writer.writerows(data)

game()
