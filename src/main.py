import random
import sys
import time
import csv
import os

class QuitError(Exception):
    pass

class Character:
    def __init__(self, name, level=5):
        self.name = name.title()
        self.level = level

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}"

class Enemy(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

class Boss(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

    def __str__(self):
        return f"""
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
        """

# Creates a boss character which is the equivalent of 6 times the player's level"
def boss_gen(x):
    global boss
    if x == 1:
        level = "bronze"
    elif x == 2:
        level = "silver"
    elif x == 3:
        level = "gold"
    boss = Boss((level + " devil"), hero.level * 6)

def terminal_clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_input(prompt):
    input_value = input(prompt)
    if input_value == "quit":
        raise QuitError
    return input_value

# Create a list of 5 enemies, with levels around player's level and adds them to list for reference
def enemy_gen():
    for x in range(5):
        name_list = ["red", "green", "yellow", "blue", "purple"]
        enemy_name = (name_list[x] + " enemy")
        enemyx = Enemy(enemy_name, (random.randint((hero.level - 4), (hero.level + 4))))
        enemy_list.append(enemyx)

# Method for fighting with regular enemies
# If you win, the enemy level is added to yours and the enemy is removed from list.
# If you lose, game over
def fight(self, other):
    if self.level >= other.level:
        self.level += other.level
        enemy_list.remove(other)
        print(f"{self.name} defeated the {other.name}! You're now level {self.level}.")
    else:
        print(f"{self.name} attacks the {other.name} and loses...")
        sys.exit("Thank you for playing. Better luck next time!")

# Method for fighting the bosses
# If you win, the enemy level is added to yours, boss is deleted, and the enemy list is cleared.
# If you lose, game over
def boss_fight(self, other):
    if self.level >= other.level:
        self.level += other.level
        print(f"{self.name} defeated the {other.name}! You're now level {self.level}.")
        del other
        enemy_list.clear()
    else:
        print(f"{self.name} attacks the {other.name} and loses...")
        sys.exit("Thank you for playing. Better luck next time!")

# Area where the enemy list is printed and the player chooses who to fight.
# Once the enemies are defeated, the player will fight the boss
def battle_area():
    print("--- BATTLE ARENA ---")
    while enemy_list != []:
        for index, enemy in enumerate(enemy_list):
            print(f"{index + 1}.\n {str(enemy)}\n")
        print("--------------------")
        try:
            battle_choice = get_input(f"Choose your opponent(1-{len(enemy_list)}): ")
        except QuitError:
            terminal_clear()
            sys.exit("Thank you for playing. See you next time!")
        else:
            terminal_clear()
            try:
                fight(hero, enemy_list[int(battle_choice) - 1])
            except (ValueError, IndexError):
                print(
f"""INVALID INPUT:
Please enter a number from 1-{len(enemy_list)}, or 'quit' to exit the game\n"""
                )
                print("--- BATTLE ARENA ---")
    print(f"You beat the enemies, and a {boss.name} appears...\n{str(boss)}")
    time.sleep(3)
    terminal_clear()
    boss_fight(hero, boss)

# The main game function.
# The player chooses between battling, checking their stats, or checking the high scores
def game():
    terminal_clear()
    time1 = time.time()
    print(
f"""Welcome to the game, {hero.name}! You're level {hero.level}. Good luck!
(Enter 'quit' at any time to exit the game)"""
    )
    time.sleep(3)
    terminal_clear()
    for i in range(3):
        boss_gen(i + 1)
        enemy_gen()
        while enemy_list != []:
            # terminal_clear()
            try:
                action = get_input(
"""--- COMMANDS ---
1 - battle
2 - stats
3 - scores
----------------
Please enter a command (1 - 3):
""")
            except QuitError:
                terminal_clear()
                sys.exit("Thank you for playing. See you next time!")
            else:
                try:
                    action = int(action)
                except ValueError:
                    terminal_clear()
                    print(
"""INVALID INPUT:
Please enter a number from 1-3, or 'quit' to exit the game\n"""
                    )
                else:
                    if action in range(1, 4):
                        if action == 1:
                            terminal_clear()
                            battle_area()
                        elif action == 2:
                            terminal_clear()
                            print("--- YOUR STATS ---")
                            print(hero)
                            print("------------------")
                            time.sleep(3)
                            terminal_clear()
                        elif action == 3:
                            terminal_clear()
                            with open ("../docs/scores.csv") as file:
                                reader = csv.reader(file)
                                print("--- TOP 5 SCORES ---")
                                reader.__next__()
                                for key, row in enumerate(reader):
                                    if key != 5:
                                        print(f"{key + 1}. {row[0]} won game in {row[1]} seconds")
                                print("--------------------")
                                time.sleep(3)
                                terminal_clear()
                    else:
                        terminal_clear()
                        print(
"""INVALID INPUT:
Please enter a number from 1-3, or 'quit' to exit the game\n"""
                        )
    time_result = round((time.time()) - time1)
    # Appends player's score to score list CSV
    with open("../docs/scores.csv", "a", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow([hero.name,time_result])
    print(f"Congratulations, {hero.name}! You won in {time_result} seconds!")
    # Sort scores list CSV
    with open("../docs/scores.csv") as file:
        reader = csv.reader(file)
        reader.__next__() # Skip the first row (the column names)
        data = sorted(csv.reader(file), key = lambda x: x[1])
    # Writes the sorted scores to the list CSV
    with open("../docs/scores.csv", "w", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow(["name","score"])
        writer.writerows(data)

if __name__ == "__main__":
    terminal_clear()
    boss = None
    enemy_list = []
    hero = Character(input("Please enter your name: "))
    game()
