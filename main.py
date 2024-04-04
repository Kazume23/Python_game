from character import Enemy, Player
from item import *
import item
import random

random_weapon = random.randint(1, len(weapon_list)) - 1
random_outfit = random.randint(1, len(armor_list)) - 1

warrior = Player(name="", hp=140, crit=5, dodge=100, armor=armor_list[1], weapon=weapon_list[1])
ranger = Player(name="", hp=70, crit=40, dodge=10, armor=armor_list[2], weapon=weapon_list[2])



player = warrior
enemy = ranger

print(
    f"Zmierzą się {player.name} i {enemy.name} w walce na życie i smierc \n Wybierz broń dla {player.name} z arsenału")
for i, weapon in enumerate(item.weapon_list, start=1):
    print(f"{i}. {weapon.name}")
weapon_choice = int(input()) - 1

if 0 <= weapon_choice < len(weapon_list):
    selected_weapon = weapon_list[weapon_choice]
    player.equip(selected_weapon)

else:
    print("Nie ma takiej broni")

while True:

    player.attack(enemy)
    if enemy.hp == 0:
        print(f"Player {player.name} win!!!")
        break

    enemy.attack(player)
    if player.hp == 0:
        print(f"Player {enemy.name} win!!!")
        break

    print(f"hp {player.name}: {player.hp}")
    print(f"hp {enemy.name}: {enemy.hp}")

    input()

# CO MA PROJEKT ROBIĆ

# 0,5. Losować staty i eq dla przeciwnika                                           DONE
# 1. Ma zakładać różne rodzai zbroi (łucznik nie może zakładać ironu etc)           1/2 DONE
# 2. Mechanika dodge i kryta                                                        DONE
# 3. Kiedy ktos umrzes to umrze i sie wyswietla wynik                               DONE
# 4. Jak wszystko skoncze to później zrobić klasy postaci z doborem eq i danym dmg  1/2
# 5. Dodac maga i inne przeliczniki na mage dmg
# ?. Ma być listener i ma wykonywać komendy podczas walki

#Fixes

#1.  Naprawić mechanikę dodge bo się psuje(cos z matma)
#2.  I znowu zjebałem gita lets gooooooooooaaa

