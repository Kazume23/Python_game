from character import Warrior, Archer, Mage
from item import *
import random
import pygame

pygame.init()

warrior = Warrior(name="Warrior", armor=random.choice(warrior_armor), weapon=random.choice(warrior_weapons))
archer = Archer(name="Archer", armor=random.choice(archer_armor), weapon=random.choice(archer_weapons))
mage = Mage(name="Mage", armor=random.choice(mage_armor), weapon=random.choice(mage_weapon))

player = warrior
enemy = mage

while True:
    if player.weapon.speed > enemy.weapon.speed:
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

    else:
        enemy.attack(player)
        if player.hp == 0:
            print(f"Player {enemy.name} win!!!")
            break

        player.attack(enemy)
        if enemy.hp == 0:
            print(f"Player {player.name} win!!!")
            break

        print(f"Hp {enemy.name}: {enemy.hp}")
        print(f"Hp {player.name}: {player.hp}")

    input()

# CO MA PROJEKT ROBIĆ

# 0,5. Losować staty i eq dla przeciwnika                                           DONE
# 1. Ma zakładać różne rodzai zbroi (łucznik nie może zakładać ironu etc)           DONE
# 2. Mechanika dodge i kryta                                                        DONE
# 3. Kiedy ktos umrzes to umrze i sie wyswietla wynik                               DONE
# 4. Jak wszystko skoncze to później zrobić klasy postaci z doborem eq i danym dmg  DONE
# 5. Dodac maga i inne przeliczniki na mage dmg                                     DONE
# 6. Refactoring kodu na przejrzysty                                                DONE
# 7. Pobieranie nazw graczy
# 8. Możliwosc wyboru klas przez graczy


# PYGAME

# 1. Wrzucic Pygame aby sie wyswietlalo okno z dwoma postaciami


# Fixes

# 1.  Naprawić mechanikę dodge bo się psuje(cos z matma)                             Done
# 2.  I znowu zjebałem gita lets goooooooooo                                         Done


# Balance
# 1.  Cos zrobic odnosnie dmg broni co do jego speeda (wiecej dmg nie ma penalty (more dmg = win))
