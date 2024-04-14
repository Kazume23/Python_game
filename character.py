import random


class Character:
    def __init__(self, name: str, hp: int, crit: int, armor: str, weapon: str):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.armor = armor
        self.weapon = weapon

        self.crit = crit

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


class Warrior(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=110, crit=5, armor=armor, weapon=weapon)


class Archer(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=80, crit=30, armor=armor, weapon=weapon)


class Mage(Character):
    def __init__(self, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(name=name, hp=70, crit=20, armor=armor, weapon=weapon)

    def cast_spell(self, target):
        print("test")


def chosen_character(player_name, characters: list):
    print(characters)
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
