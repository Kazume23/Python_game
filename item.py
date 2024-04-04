class Weapon:
    def __init__(self, name: str, dmg: int, weapon_type: str, damage_type: str, value: int) -> None:
        self.name = name
        self.dmg = dmg
        self.weapon_type = weapon_type
        self.damage_type = damage_type
        self.value = value


sword = Weapon(name="Iron sword",
               dmg=5,
               weapon_type="melee",
               damage_type="slashing",
               value=30)

bow = Weapon(name="Short bow",
             dmg=4,
             weapon_type="ranged",
             damage_type="piercing",
             value=10)

fists = Weapon(name="Fists",
               dmg=2,
               weapon_type="ranged",
               damage_type="blunt",
               value=0)

weapon_list = [sword, bow, fists]


class Armor:
    def __init__(self, name: str, protection: int, armor_type: str, value: int) -> None:
        self.name = name
        self.protection = protection
        self.armor_type = armor_type
        self.value = value


chestplate = Armor(name="Iron Chestplate",
                   protection=2,
                   armor_type="iron",
                   value=200)

leather = Armor(name="Leather armor",
                protection=1,
                armor_type="leather",
                value=50)

cloth = Armor(name="Clothing",
              protection=0,
              armor_type="trash",
              value=0)

armor_list = [chestplate, leather, cloth]
