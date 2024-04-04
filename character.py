import item
from item import fists
from item import cloth
import random


class Character:
    def __init__(self, name: str, hp: int, crit: int, dodge: int, armor: str, weapon: str):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.armor = armor
        self.weapon = weapon

        self.crit = crit
        self.dodge = dodge

    def attack(self, target) -> None:
        if random.randint(0, 100) <= self.dodge:
            if random.randint(0, 100) <= self.crit:
                target.hp -= max(0, (self.weapon.dmg * 2) - target.armor.protection)
                target.hp = max(target.hp, 0)
                print(
                    f"{self.name} JEBNĄŁ KRYTA {self.weapon.dmg * 2}dmg {self.weapon.damage_type} {self.name} bijąc {max(0, (self.weapon.dmg * 2) - target.armor.protection)} z {self.weapon.name}")

            else:
                target.hp -= max(0, self.weapon.dmg - target.armor.protection)
                target.hp = max(target.hp, 0)
                print(
                    f"{self.name} zadał {self.weapon.dmg}dmg {self.weapon.damage_type} {self.name} bijąc {max(0, self.weapon.dmg - target.armor.protection)} z {self.weapon.name}")
        else:
            print(
                f"{self.name} nie trafił przeciwnika")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} założył {self.weapon.name}")

    def outfit(self, armor) -> None:
        self.armor = armor
        print(f"{self.name} założył {self.armor.name}")

    def drop(self) -> None:
        self.weapon = fists
        print(f"{self.name} upuscił broń")


class Player(Character):
    def __init__(self, name: str, hp: int, crit: int, dodge: int, armor: str, weapon: str) -> None:
        super().__init__(name=name, hp=hp, crit=crit, dodge=dodge, armor=armor, weapon=weapon)


class Enemy(Character):
    def __init__(self, name: str, hp: int, crit: int, dodge: int, armor: str, weapon: str) -> None:
        super().__init__(name=name, hp=hp, crit=crit, dodge=dodge, armor=armor, weapon=weapon)

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equip {self.weapon.name}")

    def outfit(self, armor) -> None:
        self.armor = armor
        print(f"{self.name} equip {self.armor.name}")
