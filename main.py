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

        print(f"hp {player.name}: {player.hp}")
        print(f"hp {enemy.name}: {enemy.hp}")

    else:
        enemy.action(player)
        if player.hp == 0:
            print(f"Player {enemy.name} win!!!")
            break

        player.action(enemy)
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
# 7. Możliwosc wyboru klas przez graczy                                             DONE
# 8. Dodanie spelli dla maga na dmg/heal                                            DONE
# 9. Rework combat'u  (more action)                                                 DONE
# 10.Rozróżnienie klas potaci a nazw postaci
# 11.Dodanie ograniczonych liczb potek
# 12.Cos zrobic odnosnie wyboru eq/armoru (wiekszy wybor)

# Fixes

# 1.  Naprawić mechanikę dodge bo się psuje(cos z matma)                            DONE
# 2.  I znowu zjebałem gita lets goooooooooo                                        DONE
# 3.  Refactoring na angielski                                                      DONE
# 4.  Nadawać nazwy graczy do wybieranych klas
# 5.  Przy mirror klasach mają te same HP


# Balance
# 1.  Potestować balans postaci i balans maga
