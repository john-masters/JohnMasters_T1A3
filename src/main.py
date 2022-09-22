import game_classes as gc

def game():
    action = input(
        f'Welcome to the game, {gc.hero.name}!\nPlease choose one of the following (battle, shop, stats or scores): '
        )
    if action == 'battle':
        gc.battle_area()
    elif action == 'shop':
        pass
    elif action == 'stats':
        print(gc.hero)
    elif action == 'scores':
        pass
    else:
        action = 'Please enter one of the following (battle, shop, stats or scores): '

game()
