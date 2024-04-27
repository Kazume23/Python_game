from character import Warrior, Archer, Mage
import character
from item import *
import random

characters = ["Warrior", "Archer", "Mage"]

classes = {
    "Warrior": Warrior(name="Warrior", armor=random.choice(warrior_armor), weapon=random.choice(warrior_weapons)),
    "Archer": Archer(name="Archer", armor=random.choice(archer_armor), weapon=random.choice(archer_weapons)),
    "Mage": Mage(name="Mage", armor=random.choice(mage_armor), weapon=random.choice(mage_weapon), spell=mage_spell)
}
player_choose = character.chosen_character("Player 1", characters)
player = classes.get(player_choose)

enemy_choose = character.chosen_character("Player 2", characters)
enemy = classes.get(enemy_choose)

while True:
    if player.weapon.speed > enemy.weapon.speed:
        player.action(enemy)
        if enemy.hp == 0:
            print(f"Player {player.name} win!!!")
            break

        enemy.action(player)
        if player.hp == 0:
            print(f"Player {enemy.name} win!!!")
            break

    else:
        enemy.action(player)
        if player.hp == 0:
            print(f"Player {enemy.name} win!!!")
            break

        player.action(enemy)
        if enemy.hp == 0:
            print(f"Player {player.name} win!!!")
            break

    print()
    print(f"hp {player.name}: {player.hp}")
    print(f"hp {enemy.name}: {enemy.hp}")

    input()

print()

#           FOR LATER TESTING
# if enemy.hp == 0:
#     print(f"{player.weapon.name} 1 - 0 {enemy.weapon.name}  {player.hp}:{enemy.hp}")
# else:
#     print(f"{player.weapon.name} 0 - 1 {enemy.weapon.name}  {player.hp}:{enemy.hp}")