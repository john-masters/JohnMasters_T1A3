# T1A3 - Terminal Application

## R3 - Sources

- Trello board available [here](https://trello.com/invite/b/0atoXcqa/6fe6d7da1695821e87bcea4adfca18d1/t1a3-fight-game)

- Devil ascii art available [here](https://www.asciiart.eu/electronics/robots)

- Presentation available on YouTube [here](https://youtu.be/3Ne2Uf5Pjzs)

## R4 - Link to source control repository

- [Github](https://github.com/john-masters/JohnMasters_T1A3)

## R5 - Style guide or styling conventions

- The style guide I will be adhering to is PEP8.

## R6 - Features

### 1. Can fight opponents in battle area and increase your level

- In the battle area, there will be 5 unique opponents with randomised levels relative to the player's level.

- There will be a prompt asking player to choose which opponent to fight.

- Player chooses enemy, and if player level higher than enemy, player adds enemies level to theirs.

- If you lose a fight, then the game ends.

### 2. Three different bosses after you defeat all the opponents in the battle area

- Once the 5 opponents are finished, there will be a boss. Which the player will fight. If you lose the battle, the game ends.

- There are three different bosses which appear after all the opponents are finished, and each has a unique name and level.

- After all bosses have been defeated, the game ends.

### 3. A high score list, stored in an external file

- When the game starts, a timer begins, and the timer ends when the last boss is defeated.
- The player's score is added to an external file. The score list can be accessed in the main navigation area.

## R7 - Implementation plan

Original plan:

- Create class for player character
- Create class for opponents/bosses
- Create fight method
- Create marketplace and method for buying armour/how it modifies player character
- Create time keeping method for adding to score
- Create way to keep track of high scores

I used Trello for planning and tracking my implementation plan. You can view the board [here](https://trello.com/invite/b/0atoXcqa/6fe6d7da1695821e87bcea4adfca18d1/t1a3-fight-game).

## R8 - Help documentation

### Requirements

- Python 3

### Setup instructions

1. My Github Repository for this project is available [here](https://github.com/john-masters/JohnMasters_T1A3). If you wish to run the application you can run the following command in your terminal:

```sh
git clone https://github.com/john-masters/JohnMasters_T1A3.git
```

2. Once you have a copy of my terminal app, open to the main folder 'JohnMasters_T1A3'. Once you're there, enter into the virtual environment to the run the application. You can do that by entering the following command in your terminal. You will know it's working as '(.ven)' will appear on the left side in your terminal line.

```sh
source .venv/bin/activate
```

3. Once you have done this, enter the following command to enter into the folder containing the source code:

```sh
cd src
```

4. Next enter the following command in your terminal to start the game. This process will start the game, but it will first check to make sure you have Python 3 installed on your computer:

```sh
./game.sh
```

5. If you have Python 3 installed, the game will now begin! Aside from entering your name at the start of the game, the navigation is done by entering corresponding numbers for the actions you wish to perform. If you wish to exit the game, you can simply enter quit at any time.
