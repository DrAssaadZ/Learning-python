from ClassesBattle.game import Person
import random

magic = [{'name': 'Fire', 'cost': 10, 'damage': 100},
         {'name': 'Thunder', 'cost': 10, 'damage': 150},
         {'name': 'Blizzard', 'cost': 10, 'damage': 120}]

player = Person(460, 65, 60, 34, magic)

enemy = Person(900, 0, 60, 12, magic)

running = True

print('Enemy attacks')

while running:
    player.choose_action()
    choice = int(input()) - 1

    if choice == 0:
        enemy.take_dmg(player.generate_dmg())
        print("Enemy's HP :" + str(enemy.get_hp()))
    elif choice == 1:
        player.choose_spell()
        magic_choice = int(input()) - 1

        if player.get_mp() > player.get_spell_mp_cost(magic_choice):
            enemy.take_dmg(player.generate_spell_dmg(magic_choice))
            player.reduce_mp(player.get_spell_mp_cost(magic_choice))
            print("Enemy's HP :" + str(enemy.get_hp()))
            print("Your MP:" + str(player.get_mp()))
        else:
            print("FAILED to cast spell, no enough magic power")
            continue
    else:
        print("Enter a proper choice")
        continue

    player.take_dmg(enemy.generate_dmg())

    print("Enemy attacked, your HP:" + str(player.hp))

    if player.get_hp() == 0:
        print("You LOSE!!!!")
        running = False
    elif enemy.get_hp() == 0:
        print("You WIN!!!!")
        running = False

