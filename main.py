from character import Warrior, Archer, Mage, Berserk, Vampire
import character

characters = [Warrior, Archer, Mage, Berserk, Vampire]

player = character.chosen_character("Player 1", characters)
enemy = character.chosen_character("Player 2", characters)

while True:
    if player.weapon.speed > enemy.weapon.speed:
        player.action(enemy)
        if enemy.hp == 0:
            print(f"{player.name} {player.class_name} win!!!")
            break

        enemy.action(player)
        if player.hp == 0:
            print(f"{enemy.name} {enemy.class_name} win!!!")
            break

    else:
        enemy.action(player)
        if player.hp == 0:
            print(f"{enemy.name} {enemy.class_name} win!!!")
            break

        player.action(enemy)
        if enemy.hp == 0:
            print(f"{player.name} {player.class_name} win!!!")
            break

    print()
    print(f"HP {player.name} {player.class_name}: {round(player.hp,1)}")
    print(f"HP {enemy.name} {enemy.class_name}: {round(enemy.hp,1)}")

    input()

print()

#           FOR LATER TESTING
# if enemy.hp == 0:
#     print(f"{player.weapon.name} 1 - 0 {enemy.weapon.name}  {player.hp}:{enemy.hp}")
# else:
#     print(f"{player.weapon.name} 0 - 1 {enemy.weapon.name}  {player.hp}:{enemy.hp}")