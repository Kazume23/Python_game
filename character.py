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
        global spell_choice
        if isinstance(self, Mage):
            action_list = ["Attack", "Heal", "Cast spell"]
        else:
            action_list = ["Attack", "Heal"]
        print()
        print(f"What do you want to do {self.name}?")
        for i, action in enumerate(action_list, start=1):
            print(f"{i}. {action}")

        while True:
            try:
                choice = int(input(f"{self.name} Choose action"))
                if 0 < choice <= len(action_list):
                    if choice == 1:
                        self.attack(target)
                        break
                    elif choice == 2:
                        self.potion(target)
                        break
                    elif choice == 3 and isinstance(self, Mage):
                        while True:
                            try:
                                print(f"{self.name} have currently {self.mana} left")
                                print("Choose spell to cast:")
                                for i, spell in enumerate(mage_spell, start=1):
                                    print(f"{i}. {spell.name} ({spell.mana} mana)")
                                print()
                                spell_choice = int(input(f"{self.name} choose spell to cast")) - 1
                                if 0 <= spell_choice < len(mage_spell):
                                    self.cast_spell(target, mage_spell[spell_choice])
                                    break
                                else:
                                    print()
                                    print("Wrong number, choose again")
                            except ValueError:
                                print()
                                print("Please enter a number")
                        break
                    else:
                        print()
                        print("Your class cannot cast spells")
                else:
                    print()
                    print("Wrong number, choose again")
            except ValueError:
                print()
                print("Please enter a number")


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

    def cast_spell(self, target, spell):
        if self.mana >= spell.mana:
            self.mana -= spell.mana
            if spell_choice == 2:
                self.cast_power_up(spell)
            elif spell_choice == 3:
                self.cast_greater_heal(spell)
            else:
                self.cast_damage_spell(target, spell)
        else:
            print(f"{self.name}, you don't have enough mana")
            Character.action(self, target)

    def cast_power_up(self, spell):
        rand = random.randint(1, 2)
        self.weapon.dmg += spell.dmg + rand
        print(f"{self.name} cast {spell.name} powering himself for {spell.dmg + rand}")

    def cast_greater_heal(self, spell):
        rand = random.randint(4, 14)
        self.hp += spell.dmg + rand
        print(f"{self.name} cast {spell.name} healing himself for {spell.dmg}")

    def cast_damage_spell(self, target, spell):
        if random.randint(1, 100) <= self.crit:
            critChance = True
        else:
            critChance = False
        rand = random.randint(0, 9) if spell.name == "Fireball" else random.randint(0, 5)
        dmg = (spell.dmg + rand) * 2 if critChance else spell.dmg + rand
        target.hp -= max(0, dmg)
        print(f"{self.name} cast {spell.name} {'DEALING CRITICAL ' if critChance else 'dealing'} {dmg}dmg")


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
