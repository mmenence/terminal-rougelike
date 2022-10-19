#Joseph Paul Crowley
#121384736

import random
from random import randint






#for testing purposes, replace later
level = 0

###         player code         ###

#player class, called by create_player_random and create_player_custom to generate a new character
class Player:
    def __init__(self, **kwargs):
        #setting strength, dexterity, constitution, intelligence, wisdom and charisma stats 
        self.Str = kwargs["Str"]
        self.Dex = kwargs["Dex"]
        self.Con = kwargs["Con"]
        self.Int = kwargs["Int"]
        self.Wis = kwargs["Wis"]
        self.Cha = kwargs["Cha"]

        #setting equipment
        self.weapon = kwargs["weapon"]
        self.magic = kwargs["magic"]
        self.armour = kwargs["armour"]

        #setting up inventory
        self.potions = {"health potion":1, "mana potion":1} #starts with one of each


        #setting health and magic
        self.health = 10 + int(self.Con)/2 - 5
        self.mana = 10 + int(self.Wis)/2 - 5




#custom-generate a player character
def create_player_custom():
    try:
        #get their stats
        Str = int(input("Strength: "))
        Dex = int(input("Dexterity: "))
        Con = int(input("Constitution: "))
        Int = int(input("Intelligence: "))
        Wis = int(input("Wisdom: "))
        Cha = int(input("Charisma: "))

        #equipment
        
        #weapon
        weapon = input("Weapon (Mace, Sword or Spear?): ").lower()
        if not (weapon == "mace" or weapon == "sword" or weapon == "spear"):
            raise Exception("Not one of the acceptable weapons")

        #magic
        magic = input("Spell (Fireball, Lightning bolt or Magic quake?): ").lower()
        if not (magic == "fireball" or magic == "lightning bolt" or magic == "magic quake"):
            raise Exception("Not one of the acceptable spells")

        #armour 
        armour = input("Armour (Leather, Breastplate or Plate?): ").lower()
        if not (armour == "leather" or armour == "breastplate" or armour == "plate"):
            raise Exception("Not one of the acceptable armour sets")
        

        #creating the player object
        player = Player(Str = Str, Dex = Dex, Con = Con, Int = Int, Wis = Wis, Cha = Cha, weapon = weapon, magic = magic, armour = armour )
        
        
    except ValueError:
        print("Please enter a valid non-fraction number")
    except Exception:
        print("please check your input and try again")


#creating a player with random stats
def create_player_random():
    player = Player(
        Str = randint(3, 19), 
        Dex = randint(3, 19), 
        Con = randint(3, 19), 
        Int = randint(3, 19), 
        Wis = randint(3, 19), 
        Cha = randint(3, 19), 
        weapon = random.choice(["mace","sword", "spear" ]), 
        magic = random.choice(["fireball", "lightning bolt", "magic quake"]), 
        armour = random.choice(["leather", "breastplate", "plate" ]) )
    









###         enemy code          ###

#enemy class
class enemy:
    def __init__(self, **kwargs) -> None:
        #setting up their basic stats
        self.health = kwargs["health"] + level
        self.ac = kwargs["ac"] + level
        self.damage = kwargs["damage"] #level scaling is added when calculating damage
        self.resistances = kwargs["resistances"]
        self.weaknesses = kwargs["weaknesses"]

    #letting the monster take damage and checking if its still alive
    def take_damage(self, damage) -> bool:
        self.health -= damage
        if self.health > 0:
            return True
        else:
            return False




###       enemy subclasses      ###

#skeleton subclass
class skeleton(enemy):
    def __init__(self, **kwargs) -> None:
        kwargs["health"]= 4
        kwargs["ac"]= 3
        kwargs["damage"]= "1d2"
        kwargs["resistances"] = ["spear", "fireball"]
        kwargs["weaknesses"] = ["mace", "magic quake"]
        super().__init__(**kwargs)

#goblin subclass
class goblin(enemy):
    def __init__(self, **kwargs) -> None:
        kwargs["health"]= 2
        kwargs["ac"]= 5
        kwargs["damage"]= "1d2"
        kwargs["resistances"] = ["mace", "lightning bolt"]
        kwargs["weaknesses"] = ["sword", "fireball"]
        super().__init__(**kwargs)


#living armour subclass
class living_armour(enemy):
    def __init__(self, **kwargs) -> None:
        kwargs["health"]= 6
        kwargs["ac"]= 8
        kwargs["damage"]= "1"
        kwargs["resistances"] = ["sword", "magic quake"]
        kwargs["weaknesses"] = ["pierce", "fireball"]
        super().__init__(**kwargs)


#slime boss subclass
class slime(enemy):
    def __init__(self, **kwargs) -> None:
        kwargs["health"]= 10
        kwargs["ac"]= 5
        kwargs["damage"]= "1d4"
        kwargs["resistances"] = ["mace", "magic quake"]
        kwargs["weaknesses"] = ["pierce", "lightning bolt"]
        super().__init__(**kwargs)


#golem boss subclass
class golem(enemy):
    def __init__(self, **kwargs) -> None:
        kwargs["health"]= 14
        kwargs["ac"]= 8
        kwargs["damage"]= "1d6"
        kwargs["resistances"] = ["sword", "fireball"]
        kwargs["weaknesses"] = ["pierce", "lightning bolt"]
        super().__init__(**kwargs)

#treant subclass
class treant(enemy):
    def __init__(self, **kwargs) -> None:
        kwargs["health"]= 12
        kwargs["ac"]= 7
        kwargs["damage"]= "1d5"
        kwargs["resistances"] = ["spear", "lightning bolt"]
        kwargs["weaknesses"] = ["sword", "fireball"]
        super().__init__(**kwargs)





#room class
class room:
    def __init__(self, **kwargs) -> None:

        #co_ordinates
        self.co_ords = kwargs["co_ords"]

        #room type for spells
        self.room_type = random.choice(["wooden", "crumbling", "wet"])

        #setting up enemies
        self.enemies = []
        #if not a special room, populate with 1-3 normal enemies, if its a boss, populate with a boss. if its a special room but not a boss, leave empty
        if kwargs["special_room"] is None:
            for i in range (randint(0,3)):
                self.enemies.append(random.choice([skeleton(), goblin(), living_armour()]))
                self.special_room = None
        elif kwargs["special_room"] == "boss":
            self.enemies.append(random.choice([slime(), treant(), golem()]))
            self.special_room = kwargs["special_room"]
        else:
            self.special_room = kwargs["special_room"]
        
        
        
