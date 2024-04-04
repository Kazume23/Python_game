from item import *
import random
from item import *


class Character:
    def __init__(self, name: str, hp: int, crit: int, dodge: int, armor: str, weapon: str, weapons: list):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.armor = armor
        self.weapon = weapon
        self.weapons = weapons

        self.crit = crit
        self.dodge = dodge

        self.weapon_index = 0
        self.armor_index = 0

    def attack(self, target) -> None:
        for weapon in self.weapons:
            for _ in range(int(weapon.speed)):
                if random.randint(1, 100) >= target.dodge:
                    if random.randint(0, 100) <= self.crit:
                        target.hp -= max(0, (self.weapon.dmg * 2) - target.armor.protection)
                        target.hp = max(target.hp, 0)
                        print(
                            f"{self.name} JEBNĄŁ KRYTA {self.weapon.dmg * 2}dmg {self.name} bijąc {max(0, (self.weapon.dmg * 2) - target.armor.protection)} z {self.weapon.name}")

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

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} założył {self.weapon.name}")

    def outfit(self, armor) -> None:
        self.armor = armor
        print(f"{self.name} założył {self.armor.name}")


class Warrior(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=140, crit=5, dodge=0, armor=armor, weapon=weapon, weapons=warrior_weapons)


class Archer(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=80, crit=30, dodge=30, armor=armor, weapon=weapon, weapons=archer_weapons)
