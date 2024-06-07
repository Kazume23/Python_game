import random

from item import *


class Character:
    def __init__(self, class_name: str, name: str, hp: int, crit: int, armor: str, weapon: str, mana: int, pot: int):
        self.class_name = class_name
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.armor = armor
        self.weapon = weapon

        self.crit = crit
        self.mana = mana
        self.pot = pot

    def attack(self, target) -> None:
        if self.hit_target(target):
            if self.is_critical_hit():
                self.deal_damage(target, critical=True)
            else:
                self.deal_damage(target, critical=False)
        else:
            self.miss_attack(target)

    def hit_target(self, target) -> bool:
        return random.randint(1, 100) >= target.armor.dodge

    def is_critical_hit(self) -> bool:
        return random.randint(0, 100) <= self.crit

    def deal_damage(self, target, critical: bool) -> None:
        weapon = self.weapon
        if critical:
            if isinstance(self, Berserk):
                base_damage = weapon.dmg
                crit_text = ""
            else:
                base_damage = weapon.dmg * 2
                crit_text = "CRITICAL "
        else:
            base_damage = weapon.dmg
            crit_text = ""

        if weapon.weapon_type == "Magic":
            inflicted_damage = base_damage
        else:
            inflicted_damage = max(0, base_damage - target.armor.protection)

        target.hp = max(target.hp - inflicted_damage, 0)
        print(
            f"{self.name} {self.class_name} dealt {crit_text}{base_damage}dmg inflicting {inflicted_damage} with {weapon.name}")

        if isinstance(self, Berserk) and critical:
            print(f"{self.name} {self.class_name} attacked again!")
            self.attack(target)

    def miss_attack(self, target) -> None:
        print(f"{self.name} {self.class_name} missed the target")

    def potion(self, target) -> None:
        print(f"{self.name} {self.class_name} have currently {self.pot} potions left")
        if self.pot <= 0:
            print(f"{self.name} {self.class_name} do not have any left potions. Choose another action")
            self.action(target)
        else:
            healed = int(random.randint(4, 12))
            self.hp += healed
            self.pot -= 1
            print(f"{self.name} {self.class_name} used potion and heal {healed} and now have {self.hp}HP")

    def action(self, target):
        global spell_choice
        if isinstance(self, Mage):
            action_list = ["Attack", "Heal", "Cast spell"]
        else:
            action_list = ["Attack", "Heal"]
        print()
        print(f"What do you want to do {self.name} {self.class_name}?")
        for i, action in enumerate(action_list, start=1):
            print(f"{i}. {action}")

        while True:
            try:
                choice = int(input(f"{self.name} {self.class_name} Choose action"))
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
                                print(f"{self.name} {self.class_name} have currently {self.mana} left")
                                print("Choose spell to cast:")
                                for i, spell in enumerate(mage_spell, start=1):
                                    print(f"{i}. {spell.name} ({spell.mana} mana)")
                                print()
                                spell_choice = int(input(f"{self.class_name} choose spell to cast")) - 1
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
    def __init__(self, class_name: str, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(class_name=class_name, name=name, hp=110, crit=5, armor=armor, weapon=weapon, mana=0, pot=3)


class Archer(Character):
    def __init__(self, class_name: str, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(class_name=class_name, name=name, hp=80, crit=30, armor=armor, weapon=weapon, mana=0, pot=3)


class Berserk(Character):
    def __init__(self, class_name: str, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(class_name=class_name, name=name, hp=100, crit=30, armor=armor, weapon=weapon, mana=0, pot=0)

class Vampire(Character):
    def __init__(self, class_name: str, name: str, armor: str, weapon: str, ) -> None:
        super().__init__(class_name=class_name, name=name, hp=100, crit=30, armor=armor, weapon=weapon, mana=0, pot=0)

class Mage(Character):
    def __init__(self, class_name: str, name: str, armor: str, weapon: str, spell: str) -> None:
        super().__init__(class_name=class_name, name=name, hp=70, crit=20, armor=armor, weapon=weapon, mana=150, pot=0)
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
        rand = random.randint(1, 3)
        self.weapon.dmg += spell.dmg + rand
        print(f"{self.name} {self.name} cast {spell.name} powering himself for {spell.dmg + rand}")

    def cast_greater_heal(self, spell):
        rand = random.randint(6, 20)
        self.hp += spell.dmg + rand
        print(f"{self.name} {self.name} cast {spell.name} healing himself for {spell.dmg + rand}")

    def cast_damage_spell(self, target, spell):
        if random.randint(1, 100) <= self.crit:
            critChance = True
        else:
            critChance = False
        rand = random.randint(0, 12) if spell.name == "Fireball" else random.randint(2, 8)
        dmg = (spell.dmg + rand) * 2 if critChance else spell.dmg + rand
        target.hp -= max(0, dmg)
        print(
            f"{self.name} {self.name} cast {spell.name} {'DEALING CRITICAL ' if critChance else 'dealing'} {dmg}dmg")


def chosen_character(player_name, characters: list):
    print(f"0.  Class description")
    for i, character_class in enumerate(characters, start=1):
        print(f"{i}.  {character_class.__name__}")

    while True:
        try:
            choice = int(input(f"{player_name} choose your character"))
            if choice == 0:
                description()
            elif 0 <= choice < len(characters):
                if characters[choice] == Warrior:
                    return Warrior(class_name="Warrior", armor=random.choice(warrior_armor),
                                   weapon=random.choice(warrior_weapons), name=player_name)
                elif characters[choice] == Archer:
                    return Archer(class_name="Archer", armor=random.choice(archer_armor),
                                  weapon=random.choice(archer_weapons), name=player_name)
                elif characters[choice] == Mage:
                    return Mage(class_name="Mage", armor=random.choice(mage_armor), weapon=random.choice(mage_weapon),
                                spell=random.choice(mage_spell), name=player_name)
                elif characters[choice] == Berserk:
                    return Berserk(class_name="Berserk", armor=random.choice(berserk_armor),
                                   weapon=random.choice(berserk_weapons), name=player_name)
            else:
                print("Wrong number choose again")
        except ValueError:
            print("Please enter a number")

def description():
    print("Warrior - High damage tank with more armor and less dodge chance")
    print("Archer - Medium damage ranger with high dodge chance and almost zero armor")
    print("Mage - Low base damage but have powerful arsenal of spells, low survivability")
    print("Berserk - High damage and have a chance to attack many times, low armor and dodge chance")
    print("Vampire - Medium damage and survivability but can steal life from enemy")

