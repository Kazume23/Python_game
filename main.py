from character import Warrior, Archer
from item import *
import random
import pygame
import time

pygame.init()

warrior = Warrior(name="", armor=random.choice(warrior_armor), weapon=random.choice(warrior_weapons))
archer = Archer(name="", armor=random.choice(archer_armor), weapon=random.choice(archer_weapons))

player = warrior
enemy = archer

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
# 6. Refactoring kodu na przejrzysty


# PYGAME

# 1. Wrzucic Pygame aby sie wyswietlalo okno z dwoma postaciami


# Fixes

# 1.  Naprawić mechanikę dodge bo się psuje(cos z matma)
# 2.  I znowu zjebałem gita lets goooooooooo                                         Done
