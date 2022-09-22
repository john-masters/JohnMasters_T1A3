import game_classes as gc
import random

hero = gc.Character(input("Please enter your name: "))

enemy1 = gc.Enemy(
    "Enemy1",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
)
enemy2 = gc.Enemy(
    "Enemy2",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )
enemy3 = gc.Enemy(
    "Enemy3",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )
enemy4 = gc.Enemy(
    "Enemy4",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )
enemy5 = gc.Enemy(
    "Enemy5",(random.randint((hero.level - 2), (hero.level + 2))), (random.randint(5, 11))
    )

enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5]
