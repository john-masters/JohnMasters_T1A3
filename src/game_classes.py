import main

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
        main.enemy_list.remove(other)
    else:
        print(f'{self.name} attacks {other.name} and loses...')

def show_stats(self):
    print(f'Your level is {self.level} and you have {self.coins} coins')

class Enemy(Character):
    def __init__(self, name, level, coins):
        super().__init__(name, level, coins)

    def __str__(self):
        return f'Name: {self.name}\nLevel: {self.level}\nCoins:{self.coins}\n'

def battle_area():
    for enemy in main.enemy_list:
        print(enemy.__str__())
    battle_choice = input('Choose your opponent(1-5): ')
    if battle_choice == 1:
        fight(main.hero, main.enemy1)
    elif battle_choice == 2:
        fight(main.hero, main.enemy2)
    elif battle_choice == 3:
        fight(main.hero, main.enemy3)
    elif battle_choice == 4:
        fight(main.hero, main.enemy4)
    else:
        fight(main.hero, main.enemy5)
