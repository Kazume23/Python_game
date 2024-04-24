import random
from item import *


class Character:
    def __init__(self, name: str, hp: int, crit: int, armor: str, weapon: str, mana: int, pot: int):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.armor = armor
        self.weapon = weapon

        self.crit = crit
        self.mana = mana
        self.pot = pot

    def attack(self, target) -> None:
        if random.randint(1, 100) >= target.armor.dodge:
            if random.randint(0, 100) <= self.crit:
                if self.weapon.weapon_type == "Magic":
                    target.hp -= max(0, (self.weapon.dmg * 2))
                    target.hp = max(target.hp, 0)
                    print(
                        f"{self.name} dealt CRITICAL {self.weapon.dmg * 2}dmg {self.name} inflicting {max(0, (self.weapon.dmg * 2))} z {self.weapon.name}")

                else:
                    target.hp -= max(0, (self.weapon.dmg * 2) - target.armor.protection)
                    target.hp = max(target.hp, 0)
                    print(
                        f"{self.name} dealt CRITICAL {self.weapon.dmg * 2}dmg {self.name} inflicting {max(0, (self.weapon.dmg * 2) - target.armor.protection)} z {self.weapon.name}")

            else:
                if self.weapon.weapon_type == "Magic":
                    target.hp -= max(0, self.weapon.dmg)
                    target.hp = max(target.hp, 0)
                    print(
                        f"{self.name} dealt {self.weapon.dmg}dmg {self.name} inflicting {max(0, self.weapon.dmg)} with {self.weapon.name}")
                else:
                    target.hp -= max(0, self.weapon.dmg - target.armor.protection)
                    target.hp = max(target.hp, 0)
                    print(
                        f"{self.name} dealt {self.weapon.dmg}dmg {self.name} inflicting {max(0, self.weapon.dmg - target.armor.protection)} with {self.weapon.name}")
        else:
            print(
                f"{self.name} miss the target")

    def potion(self, target) -> None:
        print(f"{self.name} have currently {self.pot} potions left")
        if self.pot <= 0:
            print(f"{self.name} do not have any left potions. Choose another action")
            self.action(target)
        else:
            healed = int(random.randint(1, 8))
            self.hp += healed
            self.pot -= 1
            print(f"{self.name} used potion and heal {healed} and now have {self.hp}HP")

    def action(self, target):
        action_list = ["Attack", "Heal", "Cast spell"]
        print(f"What do you want to do {self.name}?")
        for i, actions in enumerate(action_list, start=1):
            print(f"{i}.  {actions}")
        while True:
            try:
                choice = int(input(f"{self.name} Choose action"))
                print(choice)
                if 0 < choice <= len(action_list):
                    if choice == 1:
                        self.attack(target)
                        break
                    elif choice == 2:
                        self.potion(target)
                        break
                    elif choice == 3:
                        if isinstance(self, Mage):
                            Mage.cast_spell(self, target)
                            break
                        else:
                            print("Your class cannot cast spells")
            except ValueError:
                print("Wrong number choose again")


class Warrior(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=110, crit=5, armor=armor, weapon=weapon, mana=0, pot=3)


class Archer(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=80, crit=30, armor=armor, weapon=weapon, mana=0, pot=3)


class Mage(Character):
    def __init__(self, name: str, armor: str, weapon: str, spell: str) -> None:
        super().__init__(name=name, hp=70, crit=20, armor=armor, weapon=weapon, mana=100, pot=0)
        self.spell = spell

    def cast_spell(self, target):
        if random.randint(0, 100) <= self.crit:
            crit = True
        else:
            crit = False

        spell_list = [f"{self.spell[0].name}            {self.spell[0].mana}",
                      f"{self.spell[1].name}            {self.spell[1].mana}",
                      f"{self.spell[2].name}            {self.spell[2].mana}",
                      f"{self.spell[3].name}        {self.spell[3].mana}"]
        print(f"{self.name} you currently have {self.mana} mana")
        if self.mana <= 0:
            print(f"{self.name} you have no mana")
        else:
            for i, spells in enumerate(spell_list, start=1):
                print(f"{i}.  {spells}")

            while True:
                try:
                    choice = int(input(f"{self.name} choose spell to cast")) - 1
                    if 0 <= choice <= len(spell_list) - 1:
                        if choice == 0 and self.mana >= self.spell[choice].mana:  # Fireball
                            rand = random.randint(0, 9)
                            if crit:
                                target.hp -= max(0, ((self.spell[choice].dmg + rand) * 2))
                                target.hp = max(target.hp, 0)
                                self.mana -= self.spell[choice].mana
                                print(
                                    f"{self.name} cast {self.spell[choice].name} DEALING CRITICAL {(self.spell[choice].dmg + rand) * 2}DMG")
                            else:
                                target.hp -= max(0, (self.spell[choice].dmg + rand))
                                target.hp = max(target.hp, 0)
                                self.mana -= self.spell[choice].mana
                                print(
                                    f"{self.name} cast {self.spell[choice].name} dealing {self.spell[choice].dmg + rand}dmg")
                            break
                        elif choice == 1 and self.mana >= self.spell[choice].mana:  # Ice Nova
                            rand = random.randint(0, 5)
                            if crit:
                                target.hp -= max(0, ((self.spell[choice].dmg + rand) * 2))
                                target.hp = max(target.hp, 0)
                                self.mana -= self.spell[choice].mana
                                print(
                                    f"{self.name} cast {self.spell[choice].name} DEALING CRITICAL {(self.spell[choice].dmg + rand) * 2}DMG")
                            else:
                                target.hp -= max(0, (self.spell[choice].dmg + rand))
                                target.hp = max(target.hp, 0)
                                self.mana -= self.spell[choice].mana
                                print(
                                    f"{self.name} cast {self.spell[choice].name} dealing {self.spell[choice].dmg + rand}dmg")
                            break
                        elif choice == 2 and self.mana >= self.spell[choice].mana:  # Power Up
                            rand = random.randint(1, 3)
                            self.weapon.dmg += self.spell[choice].dmg + rand
                            self.mana -= self.spell[choice].mana
                            print(
                                f"{self.name} cast {self.spell[choice].name} powering himself for {self.spell[choice].dmg + rand}")
                            break
                        elif choice == 3 and self.mana >= self.spell[choice].mana:  # Greater Heal
                            rand = random.randint(4, 14)
                            self.hp += self.spell[choice].dmg + rand
                            self.mana -= self.spell[choice].mana
                            print(
                                f"{self.name} cast {self.spell[choice].name} healing himself for {self.spell[choice].dmg}")
                            break
                        else:
                            print(f"{self.name} you don't have mana")
                            Character.action(self, target)
                            break

                    else:
                        print("Wrong number choose again")
                except ValueError:
                    print("Please enter a number")


def chosen_character(player_name, characters: list):
    for i, character in enumerate(characters, start=1):
        print(f"{i}.  {character}")

    while True:
        try:
            choice = int(input(f"{player_name} choose your character")) - 1
            if 0 <= choice < len(characters):
                return characters[choice]
            else:
                print("Wrong number choose again")
        except ValueError:
            print("Please enter a number")
