import instances as ins

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
            ins.enemy_list.remove(other)
        else:
            print(f'{self.name} attacks {other.name} and loses...')

class Enemy(Character):
    def __init__(self, name, level, coins):
        super().__init__(name, level, coins)

    def __str__(self):
        return f'Name: {self.name}\nLevel: {self.level}\nCoins:{self.coins}\n'

def battle_area():
    for enemy in ins.enemy_list:
        print(enemy.__str__())
    battle_choice = input('Choose your opponent(1-5): ')
    if battle_choice == 1:
        Character.fight(ins.hero, ins.enemy1)
    elif battle_choice == 2:
        Character.fight(ins.hero, ins.enemy2)
    elif battle_choice == 3:
        Character.fight(ins.hero, ins.enemy3)
    elif battle_choice == 4:
        Character.fight(ins.hero, ins.enemy4)
    else:
        Character.fight(ins.hero, ins.enemy5)
