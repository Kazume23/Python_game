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
    Weapon("Sword", 8, "Melee", 1, 50),
    Weapon("Axe", 9, "Melee", 0.75, 60),
    Weapon("Halberd", 10, "Melee", 0.50, 90)
]

archer_weapons = [
    Weapon("Bow", 6, "Ranged", 1.75, 20),
    Weapon("Crossbow", 7, "Ranged", 1.5, 60),
    Weapon("Flintlock pistol", 8, "Ranged", 1.1, 110)
]

berserk_weapons = [
    Weapon("Axe", 8, "Melee", 0.90, 60)
]

vampire_weapon = [
    Weapon("Teeth", 3, "Magic", 1.20, 0)
]

mage_weapon = [
    Weapon("Magician's staff", 4, "Magic", 1.2, 200),
    Weapon("Stick called Jeff", 8, "Melee", 1.6, 2137)
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

berserk_armor = [
    Armor("Chest", 0, "Light", 10, 0)
]

vampire_armor = [
    Armor("Coat", 1, "Light", 25, 0)
]

mage_armor = [
    Armor("Mage's robe", 1, "Light", 15, 20)
]

mage_spell = [
    Spell("Fireball", 6, 20),
    Spell("Ice nova", 2, 10),
    Spell("Power up", 0, 40),
    Spell("Greater heal", 4, 30)
]
