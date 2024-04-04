class Armor:
    def __init__(self, name: str, protection: int, armor_type: str, speed: float, value: int) -> None:
        self.name = name
        self.protection = protection
        self.armor_type = armor_type
        self.speed = speed
        self.value = value
        self.armor_index = 0


class Weapon:
    def __init__(self, name: str, dmg: int, weapon_type: str, speed: float, value: int) -> None:
        self.name = name
        self.dmg = dmg
        self.weapon_type = weapon_type
        self.speed = speed
        self.value = value


warrior_weapons = [
    Weapon("Miecz", 4, "Melee", 1, 50),
    Weapon("Topór", 5, "Melee", 0.75, 60),
    Weapon("Halabarda", 5, "Melee", 0.50, 90)
]

archer_weapons = [
    Weapon("Łuk", 3, "Ranged", 1.75, 20),
    Weapon("Kusza", 4, "Ranged", 1.3, 60),
    Weapon("Pistolet", 5, "Ranged", 0.85, 110)
]

warrior_armor = [
    Armor("Kolczuga", 2, "Medium", 0.8, 100),
    Armor("Płytówka", 3, "Medium", 0.5, 180),
    Armor("Pantalony", 4, "Heavy", 0.20, 300)
]

archer_armor = [
    Armor("Klata", 0, "Light", 2.25, 0),
    Armor("Kaptur", 1, "Light", 1.5, 20),
    Armor("Skórzany kaftan", 2, "Light", 1, 40)
]
