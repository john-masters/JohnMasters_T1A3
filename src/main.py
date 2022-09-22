import random
import game_classes as gc

# class Character:
#     def __init__(self, name, level=5, coins=0):
#         self.name = name
#         self.level = level
#         self.coins = coins

# def fight(self, other):
#     if self.level >= other.level:
#         self.level += other.level
#         self.coins += other.coins
#         print(f'{self.name} defeated {other.name}! You\'re now level {self.level} and you receive {other.coins} coins for winning.')
#         del other
#         enemy_list.remove(other)
#     else:
#         print(f'{self.name} attacks {other.name} and loses...')

# def show_stats(self):
#     print(f'Your level is {self.level} and you have {self.coins} coins')

# class Enemy(Character):
#     def __init__(self, name, level, coins):
#         super().__init__(name, level, coins)

#     def __str__(self):
#         return f'Name: {self.name}\nLevel: {self.level}\nCoins:{self.coins}\n'

hero = gc.Character("Hero")

enemy1 = gc.Enemy("Enemy1",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))
enemy2 = gc.Enemy("Enemy2",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))
enemy3 = gc.Enemy("Enemy3",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))
enemy4 = gc.Enemy("Enemy4",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))
enemy5 = gc.Enemy("Enemy5",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11)))

enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5]

# def battle_area():
#     for enemy in enemy_list:
#         print(enemy.__str__())
#     while enemy_list != []:
#         battle_choice = input('Choose your opponent(1-5): ')
#         if battle_choice == 1:
#             fight(hero, enemy1)
#         elif battle_choice == 2:
#             fight(hero, enemy2)
#         elif battle_choice == 3:
#             fight(hero, enemy3)
#         elif battle_choice == 4:
#             fight(hero, enemy4)
#         else:
#             fight(hero, enemy5)

gc.battle_area()
