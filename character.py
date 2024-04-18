import random
from item import *


class Character:
    def __init__(self, name: str, hp: int, crit: int, armor: str, weapon: str, mana: int):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.armor = armor
        self.weapon = weapon

        self.crit = crit
        self.mana = mana

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

    def potion(self) -> None:
        healed = int(random.randint(1, 8))
        self.hp += healed
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
                        self.potion()
                        break
                    elif choice == 3:
                        if isinstance(self, Mage):
                            self.cast_spell(target)
                            break
                        else:
                            print("Your class cannot cast spells")
            except ValueError:
                print("Wrong number choose again")


class Warrior(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=110, crit=5, armor=armor, weapon=weapon, mana=0)


class Archer(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=80, crit=30, armor=armor, weapon=weapon, mana=0)


class Mage(Character):
    def __init__(self, name: str, armor: str, weapon: str, spell: Spell) -> None:
        super().__init__(name=name, hp=70, crit=20, armor=armor, weapon=weapon, mana=100)
        self.spell = spell

    def cast_spell(self, target):
        spell_list = ["Fireball", "Ice nova", "Power up", "Greater heal"]
        if self.mana <= 0:
            print(f"{self.name} you have no mana")
        else:
            for i, spell in enumerate(spell_list, start=1):
                print(f"{i}.  {spell}")

            while True:
                try:
                    choice = int(input(f"{self.name} choose spell to cast"))
                    if 0 < choice <= len(spell_list):
                        print("UDANE ZAKLECIE")
                        return spell_list[choice]
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
