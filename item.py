import random


class Armor:
    def __init__(self, name: str, protection: int, armor_type: str, dodge: int, value: int) -> None:
        self.name = name
        self.protection = protection
        self.armor_type = armor_type
        self.dodge = dodge
        self.value = value
        self.armor_index = 0


class Weapon:
    def __init__(self, name: str, dmg: int, weapon_type: str, speed: float, value: int) -> None:
        self.name = name
        self.dmg = dmg
        self.weapon_type = weapon_type
        self.speed = speed
        self.value = value


class Spell:
    def __init__(self, name: str, dmg: int, mana: int):
        self.name = name
        self.dmg = dmg
        self.mana = mana


warrior_weapons = [
    Weapon("Sword", 4, "Melee", 1, 50),
    Weapon("Axe", 5, "Melee", 0.75, 60),
    Weapon("Halberd", 6, "Melee", 0.50, 90)
]

archer_weapons = [
    Weapon("Bow", 3, "Ranged", 1.75, 20),
    Weapon("Crossbow", 4, "Ranged", 1.3, 60),
    Weapon("Flintlock pistol", 5, "Ranged", 1.1, 110)
]

mage_weapon = [
    Weapon("Magician's staff", 2, "Magic", 1.2, 200)
]

warrior_armor = [
    Armor("Chainmail", 2, "Medium", 10, 100),
    Armor("Chain armor", 3, "Medium", 5, 180),
    Armor("Plate armor", 4, "Heavy", 1, 300)
]

archer_armor = [
    Armor("Chest", 0, "Light", 60, 0),
    Armor("Hood", 1, "Light", 50, 20),
    Armor("Leather caftan", 2, "Light", 40, 40)
]

mage_armor = [
    Armor("Mage's robe", 1, "Light", 15, 20)
]

mage_spell = [
    Spell("Fireball", random.randint(3, 12), 25),
    Spell("Ice nova", random.randint(3, 7), 20),
    Spell("Power up", random.randint(1, 2), 25),
    Spell("Greater heal", random.randint(4, 16), 25)
]
