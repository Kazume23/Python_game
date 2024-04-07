import random
from item import *


class Character:
    def __init__(self, name: str, hp: int, crit: int, armor: str, weapon: str):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.armor = armor
        self.weapon = weapon

        self.crit = crit

        self.weapon_index = 0
        self.armor_index = 0

    def attack(self, target) -> None:
        if random.randint(1, 100) >= target.armor.dodge:
            if random.randint(0, 100) <= self.crit:
                if self.weapon.weapon_type == "Magic":
                    target.hp -= max(0, (self.weapon.dmg * 2))
                    target.hp = max(target.hp, 0)
                    print(
                        f"{self.name} JEBNĄŁ KRYTA {self.weapon.dmg * 2}dmg {self.name} bijąc {max(0, (self.weapon.dmg * 2))} z {self.weapon.name}")

                else:
                    target.hp -= max(0, (self.weapon.dmg * 2) - target.armor.protection)
                    target.hp = max(target.hp, 0)
                    print(
                        f"{self.name} JEBNĄŁ KRYTA {self.weapon.dmg * 2}dmg {self.name} bijąc {max(0, (self.weapon.dmg * 2) - target.armor.protection)} z {self.weapon.name}")

            else:
                if self.weapon.weapon_type == "Magic":
                    target.hp -= max(0, self.weapon.dmg)
                    target.hp = max(target.hp, 0)
                    print(
                        f"{self.name} zadał {self.weapon.dmg}dmg {self.name} bijąc {max(0, self.weapon.dmg)} z {self.weapon.name}")
                else:
                    target.hp -= max(0, self.weapon.dmg - target.armor.protection)
                    target.hp = max(target.hp, 0)
                    print(
                        f"{self.name} zadał {self.weapon.dmg}dmg {self.name} bijąc {max(0, self.weapon.dmg - target.armor.protection)} z {self.weapon.name}")
        else:
            print(
                f"{self.name} nie trafił przeciwnika")

    def current_weapon(self):
        return self.weapon[self.weapon_index]


class Warrior(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=110, crit=5, armor=armor, weapon=weapon)


class Archer(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=80, crit=30, armor=armor, weapon=weapon)


class Mage(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=70, crit=20, armor=armor, weapon=weapon)
