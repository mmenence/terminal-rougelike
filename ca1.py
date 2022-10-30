#Joseph Paul Crowley
#121384736


from operator import le
import random
from random import randint

from requests import patch













#for testing purposes, replace later
depth = 0
player = None


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
        self.inventory = {"health potion":1, "mana potion":1, "map":False, "key": False} #starts with one of each


        #setting health and magic
        self.health = 10 + int(self.Con/2 - 5)
        self.mana = 10 + int(self.Wis/2 - 5)

        self.co_ords = [0,0]
        self.gold = 0


    #prints stats to screen
    def display_stats(self):

        print("health:" , self.health)
        print("mana:" , self.mana)
        print("gold:" , self.gold)


        print("")

        print("Strength:" , self.Str)
        print("Dexterity:" , self.Dex)
        print("Constitution:" , self.Con)
        print("Intelligence:" , self.Int)
        print("Wisdom:" , self.Wis)
        print("Charisma:" , self.Cha)

        print("")

        print("Weapon:" , self.weapon)
        print("magic:" , self.magic)
        print("armour:" , self.armour)
        





#custom-generate a player character  --DELETE LATER
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


#creating a player with random stats --DELETE LATER
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
        self.health = kwargs["health"] + depth
        self.ac = kwargs["ac"] + depth
        self.damage = kwargs["damage"] #level scaling is added when calculating damage
        self.resistances = kwargs["resistances"]
        self.weaknesses = kwargs["weaknesses"]

    #letting the monster take damage and checking if its still alive
    def take_damage(self, weapon) -> bool:

        if randint(1, 21) > self.ac:
            #determining type and amount of damage
            if weapon == "mace":
                damage = randint(1,9) + (player.Str // 2 -5)
            elif weapon == "sword":
                damage = randint(1,7) + (player.Str // 2 -5)
            elif weapon == "spear":
                damage = randint(1,5) + (player.Str // 2 -5)
            elif weapon == "fireball":
                damage = randint(1,12) + (player.Int // 2 -5)
            elif weapon == "lightning bolt":
                damage = randint(1,8) + (player.Int // 2 -5)
            elif weapon == "magic quake":
                damage = randint(1,6) + (player.Int // 2 -5)

            #in case damage is negative or less than zero
            if damage < 0:
                damage = 1

            #reistance and weaknesses
            if weapon in self.resistances:
                damage /= 2
                print("The enemy is resistant to your " + str(weapon) + "! It takes " + str(int(damage)) + " damage!")

            elif weapon in self.weaknesses:
                damage *= 2
                print("The enemy is weak to your " + str(weapon) + "! It takes " + str(int(damage)) + " damage!")

            else:
                print("The enemy takes " + str(damage) + " damage!")


            self.health -= int(damage)
            if int(self.health) > 0:
                return True
            else:
                #money
                money = randint(1, 3) + depth
                if self.name == "treant" or self.name == "slime" or self.name == "golem":
                    money += 10 + randint(1 ,5*depth + 5) + randint(depth, depth *10)
                
                player.gold += money
                print(self.name, "dropped", money, "gold!")

                return False


        else:
            print(random.choice(["The enemy nimbly dodges away from your attack!", "The enemy slips through your attack!", "Your attack is stopped by its armour!"]))
            return True


    def deal_damage(self):
        #determining players ac
        if player.armour == "plate":
            ac = 16
        elif player.armour == "leather":
            ac = int(player.Dex / 2 -5) + 12
        else:
            ac = int((player.Dex / 2 -5) / 2) + 14 # 14 + half dex mod

        if randint(1, 20) > ac:
            if self.damage == "1d2":
                dmg = randint(1,2)
                print("The", self.name, "attacks, dealing", dmg+depth, "damage!")
                player.health -=  + depth
            else:
                print("The", self.name, "attacks, dealing", 1+depth, "damage!")
                player.health -= 1 + depth

        else:
            print(random.choice([("you nimbly dodge out of the way of the "+ str(self.name) +"'s attack!") , ("The "+ str(self.name) +"'s attack bounces off your armour!"), ("You slip through the "+ str(self.name) +"'s attack!" )]))



###       enemy subclasses      ###

#skeleton subclass
class skeleton(enemy):
    def __init__(self, **kwargs) -> None:
        self.name = "skeleton"
        kwargs["health"]= 4
        kwargs["ac"]= 3
        kwargs["damage"]= "1d2"
        kwargs["resistances"] = ["spear", "fireball"]
        kwargs["weaknesses"] = ["mace", "magic quake"]
        super().__init__(**kwargs)

#goblin subclass
class goblin(enemy):
    def __init__(self, **kwargs) -> None:
        self.name = "goblin"
        kwargs["health"]= 2
        kwargs["ac"]= 5
        kwargs["damage"]= "1d2"
        kwargs["resistances"] = ["mace", "lightning bolt"]
        kwargs["weaknesses"] = ["sword", "fireball"]
        super().__init__(**kwargs)


#living armour subclass
class living_armour(enemy):
    def __init__(self, **kwargs) -> None:
        self.name = "living armour"
        kwargs["health"]= 6
        kwargs["ac"]= 8
        kwargs["damage"]= "1"
        kwargs["resistances"] = ["sword", "magic quake"]
        kwargs["weaknesses"] = ["pierce", "lightning bolt"]
        super().__init__(**kwargs)


#slime boss subclass
class slime(enemy):
    def __init__(self, **kwargs) -> None:
        self.name = "slime"
        kwargs["health"]= 10
        kwargs["ac"]= 5
        kwargs["damage"]= "1d4"
        kwargs["resistances"] = ["mace", "magic quake"]
        kwargs["weaknesses"] = ["pierce", "lightning bolt"]
        super().__init__(**kwargs)


#golem boss subclass
class golem(enemy):
    def __init__(self, **kwargs) -> None:
        self.name = "golem"
        kwargs["health"]= 14
        kwargs["ac"]= 8
        kwargs["damage"]= "1d6"
        kwargs["resistances"] = ["sword", "fireball"]
        kwargs["weaknesses"] = ["pierce", "lightning bolt"]
        super().__init__(**kwargs)

#treant subclass
class treant(enemy):
    def __init__(self, **kwargs) -> None:
        self.name = "treant"
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
            for i in range (randint(1,3)):
                self.enemies.append(random.choice([skeleton(), goblin(), living_armour()]))
                self.special_room = None
        elif kwargs["special_room"] == "boss":
            self.enemies.append(random.choice([slime(), treant(), golem()]))
            self.special_room = kwargs["special_room"]
        else:
            self.special_room = kwargs["special_room"]

        #setting the inventory of a shop
        if self.special_room == "shop":
            self.inventory = {
                random.choice(["mace", "sword", "spear"]): 15*(depth+1),
                random.choice(["fireball", "lightning bolt", "magic quake"]): 15*(depth+1),
                random.choice(["leather", "breastplate", "plate"]): 15*(depth+1),
                "map": 12*(depth+1),
                "health potion": 10*(depth+1), 
                "mana potion": 10*(depth+1)}
        
    


            ###         level class         ###

#level class
class Level:



                ###         generating the level            ###

    # was this the most legible or line-efficient method for writhing this out?
    # absolutely not. but it was definitely the most time efficient.
    # skip to line ~593 if you cant be bothered reading through it all
    # (its mostly copy-pasted with minor changes)

    # explanation for function is:
    # randomly decide room adjacent to current (first starts from 0,0)
    # if room space is occupied, choose a random non-special room and attempt to build off of that
    # if room is unoccupied create a new instance of a room and add to relavent lists
    # if it is time for a special room, generate that instead (boss, key, fountain, shop)

    def __init__(self) -> None:

        self.rooms = [room(co_ords = [0,0], special_room = None)]

        #list of rooms so program doesnt have to go into every instance of a room later
        self.occupied_rooms = [[0,0]]
        self.special_rooms = []

        #for level generation
        self.current_room = [0,0]
        self.next_room = [0,0]

        
        #generating the level
        while len(self.rooms) < 5:

            locat_int = randint(0, 4)

            #up
            if locat_int == 0:
                self.next_room = [self.next_room[0], self.next_room[1]+1]
            #down
            elif locat_int == 1:
                self.next_room = [self.next_room[0], self.next_room[1]-1]
            #left
            elif locat_int == 2:
                self.next_room = [self.next_room[0]-1, self.next_room[1]]
            #right
            elif locat_int == 3:
                self.next_room = [self.next_room[0]+1, self.next_room[1]]
            
            #checking if space is occupied, if not create a room. if so, try to build off another room
            if self.next_room not in self.occupied_rooms:
                self.rooms.append(room(co_ords = self.next_room, special_room = None))
                self.current_room = self.next_room
                self.occupied_rooms.append(self.current_room)
            else:
                self.next_room = random.choice(self.occupied_rooms)

        #generating boss room
        while len(self.special_rooms) == 0:

            locat_int = randint(0, 4)

            #up
            if locat_int == 0:
                self.next_room = [self.next_room[0], self.next_room[1]+1]
            #down
            elif locat_int == 1:
                self.next_room = [self.next_room[0], self.next_room[1]-1]
            #left
            elif locat_int == 2:
                self.next_room = [self.next_room[0]-1, self.next_room[1]]
            #right
            elif locat_int == 3:
                self.next_room = [self.next_room[0]+1, self.next_room[1]]
            
            #checking if space is occupied, if not create a room. if so, try to build off another room
            if self.next_room not in self.occupied_rooms and self.next_room not in self.special_rooms:
                self.rooms.append(room(co_ords = self.next_room, special_room = "boss"))
                self.current_room = [0,0]
                self.special_rooms.append(self.next_room)
                
            
            self.next_room = random.choice(self.occupied_rooms)


        #more rooms
        while len(self.rooms) < 8:

            locat_int = randint(0, 4)

            #up
            if locat_int == 0:
                self.next_room = [self.next_room[0], self.next_room[1]+1]
            #down
            elif locat_int == 1:
                self.next_room = [self.next_room[0], self.next_room[1]-1]
            #left
            elif locat_int == 2:
                self.next_room = [self.next_room[0]-1, self.next_room[1]]
            #right
            elif locat_int == 3:
                self.next_room = [self.next_room[0]+1, self.next_room[1]]
            
            #checking if space is occupied, if not create a room. if so, try to build off another room
            if self.next_room not in self.occupied_rooms and self.next_room not in self.special_rooms:
                self.rooms.append(room(co_ords = self.next_room, special_room = None))
                self.current_room = self.next_room
                self.occupied_rooms.append(self.current_room)
            else:
                self.next_room = random.choice(self.occupied_rooms)

        
        #generating key room
        while len(self.special_rooms) == 1:

            locat_int = randint(0, 4)

            #up
            if locat_int == 0:
                self.next_room = [self.next_room[0], self.next_room[1]+1]
            #down
            elif locat_int == 1:
                self.next_room = [self.next_room[0], self.next_room[1]-1]
            #left
            elif locat_int == 2:
                self.next_room = [self.next_room[0]-1, self.next_room[1]]
            #right
            elif locat_int == 3:
                self.next_room = [self.next_room[0]+1, self.next_room[1]]
            
            #checking if space is occupied, if not create a room. if so, try to build off another room
            if self.next_room not in self.occupied_rooms and self.next_room not in self.special_rooms:
                self.rooms.append(room(co_ords = self.next_room, special_room = "key"))
                self.current_room = [0,0]
                self.special_rooms.append(self.next_room)

            self.next_room = random.choice(self.occupied_rooms)

        
        #more rooms
        while len(self.rooms) < 11:

            locat_int = randint(0, 4)

            #up
            if locat_int == 0:
                self.next_room = [self.next_room[0], self.next_room[1]+1]
            #down
            elif locat_int == 1:
                self.next_room = [self.next_room[0], self.next_room[1]-1]
            #left
            elif locat_int == 2:
                self.next_room = [self.next_room[0]-1, self.next_room[1]]
            #right
            elif locat_int == 3:
                self.next_room = [self.next_room[0]+1, self.next_room[1]]
            
            #checking if space is occupied, if not create a room. if so, try to build off another room
            if self.next_room not in self.occupied_rooms and self.next_room not in self.special_rooms:
                self.rooms.append(room(co_ords = self.next_room, special_room = None))
                self.current_room = self.next_room
                self.occupied_rooms.append(self.current_room)
            else:
                self.next_room = random.choice(self.occupied_rooms)

        
        #generating fountain room
        while len(self.special_rooms) == 2:

            locat_int = randint(0, 4)

            #up
            if locat_int == 0:
                self.next_room = [self.next_room[0], self.next_room[1]+1]
            #down
            elif locat_int == 1:
                self.next_room = [self.next_room[0], self.next_room[1]-1]
            #left
            elif locat_int == 2:
                self.next_room = [self.next_room[0]-1, self.next_room[1]]
            #right
            elif locat_int == 3:
                self.next_room = [self.next_room[0]+1, self.next_room[1]]
            
            #checking if space is occupied, if not create a room. if so, try to build off another room
            if self.next_room not in self.occupied_rooms and self.next_room not in self.special_rooms:
                self.rooms.append(room(co_ords = self.next_room, special_room = "fountain"))
                current_room = [0,0]
                self.special_rooms.append(self.next_room)
            
            self.next_room = random.choice(self.occupied_rooms)

        #more rooms
        while len(self.rooms) > 13:

            locat_int = randint(0, 4)

            #up
            if locat_int == 0:
                self.next_room = [self.next_room[0], self.next_room[1]+1]
            #down
            elif locat_int == 1:
                self.next_room = [self.next_room[0], self.next_room[1]-1]
            #left
            elif locat_int == 2:
                self.next_room = [self.next_room[0]-1, self.next_room[1]]
            #right
            elif locat_int == 3:
                self.next_room = [self.next_room[0]+1, self.next_room[1]]
            
            #checking if space is occupied, if not create a room. if so, try to build off another room
            if self.next_room not in self.occupied_rooms and self.next_room not in self.special_rooms:
                self.rooms.append(room(co_ords = self.next_room, special_room = None))
                self.current_room = self.next_room
                self.occupied_rooms.append(self.current_room)
            else:
                self.next_room = random.choice(self.occupied_rooms)

        
        #generating shop room
        while len(self.special_rooms) == 3:

            locat_int = randint(0, 4)

            #up
            if locat_int == 0:
                self.next_room = [self.next_room[0], self.next_room[1]+1]
            #down
            elif locat_int == 1:
                self.next_room = [self.next_room[0], self.next_room[1]-1]
            #left
            elif locat_int == 2:
                self.next_room = [self.next_room[0]-1, self.next_room[1]]
            #right
            elif locat_int == 3:
                self.next_room = [self.next_room[0]+1, self.next_room[1]]
            
            #checking if space is occupied, if not create a room. if so, try to build off another room
            if self.next_room not in self.occupied_rooms and self.next_room not in self.special_rooms:
                self.rooms.append(room(co_ords = self.next_room, special_room = "shop"))
                self.current_room = [0,0]
                self.special_rooms.append(self.next_room)
           
            self.next_room = random.choice(self.occupied_rooms)




















            ###         GAME LOOP           ###


#initialising the game -simple loop to keep the game running no matter what
while True:

#character creation

    #custom input
    if input('To create custom character, type "custom", to use a randomly generated character, enter any other input\n') == "custom":
 
        print("Warning: the game is balanced around stats of 3-18. While I have left it possible to have enough strength to bench press alaska or so little constitution that you die upon starting the game, this is not the intended balance. if you simply wish to destroy everything in the game with little effort however, feel free to do so")
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
            
            #display stats at end of both statement so if an error with custom stats occurs, it will not run without the instance of player
            player.display_stats()
        
        except ValueError:
            print("Please enter a valid non-fraction number")
        except Exception:
            print("please check your input and try again")


    #random character generator
    else:
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

    #making the first level
    level = Level()


    for i in level.rooms:
                if i.co_ords == player.co_ords:
                    if not None in i.enemies:
                        print("You are attacked by a group of monsters!")
                        
                        for e in i.enemies:
                            print("Monster" , i.enemies.index(e) + 1, ": a", e.name )
    

    #while player is not none, player is set to none on game over so the loop is broken
    while player != None:



        #taking the input and treating it
        #putting the input into lowercase, removing excess spaces, then splitting it into words for easier processing
        player_input = input().lower().strip().split()

        #small check to avoid errors
        if player_input == []:
            player_input = [" "]
        


                    ###         asessing input          ###


        #help command
        if player_input[0] == "help":
            if player_input[-1] == "combat":
                print("-Melee weapon command is: attack [enemy number] with weapon OR attack [enemy number] weapon")
                print("-Cast spell command is: attack [enemy number] with magic OR attack [enemy number] magic")

            elif player_input[-1] == "movement":
                print("-Movement command is: move [north, east, south or west]")

            elif player_input[-1] == "shop":
                print("-Buy item command is: buy [Name of item]")

            elif player_input[-1] == "check":
                print("-Display inventory command is: check bag")
                print("-Display map command is: check map")
                print("-Examine room command is: check room")
                print("-Display status command is: check status")

            elif player_input[-1] == "misc":
                print("-Drink potion command is: drink [Potion type]")
                print("-Drink from fountain command is: drink from fountain OR drink fountain")
            
            else:
                print("Help commands are:")
                print("-help combat")
                print("-help movement")
                print("-help shop")
                print("-help check")
                print("-help misc")


        #attacking command
        elif player_input[0] == "attack":

            #getting the room the player is in
            for i in level.rooms:
                if i.co_ords == player.co_ords:

                    #determining which side goes first
                    if int(player.Dex/2-5) + randint(1,20) > randint(1,20) + depth:
                        print("\nThe enemy side attacks!")
                        for e in i.enemies:
                            if e is not None:
                                e.deal_damage()
                    else:
                        print("\nYou're too fast for the enemy to attack!")
                    
                    print("\nYour turn")
                    try:
                        
                        #melee weapon

                        #getting index of enemy in room.enemies
                        if player_input[-1] == "weapon":
                            if player_input[1] == "1" or player_input[1] == "one":
                                e_index = 0
                            elif player_input[1] == "2" or player_input[1] == "two":
                                e_index = 1
                            elif player_input[1] == "3" or player_input[1] == "three":
                                e_index = 2
                            else:
                                #in case index provided is false
                                raise IndexError 

                            #if enemy has not been defeated yet
                            if i.enemies[e_index] is not None:
                                #making the enemy take damage and checking if its dead
                                if not i.enemies[e_index].take_damage(player.weapon):

                                    #getting the index of the current room, putting that into the list of rooms, getting the current room class and changing the first enemy to None
                                    level.rooms[level.rooms.index(i)].enemies[e_index] = None

                                    #if there is no enemies left, end battle
                                    if i.enemies == [None] or i.enemies == [None, None] or i.enemies == [None, None, None]:
                                        print("All enemies have been defeated!")
                                    else:
                                        print("The enemy has been defeated!")

                            #if enemy does not exist or has been defeated
                            else:
                                print("That enemy does not exist")

                        
                        #magic 
                        elif player_input[-1] == "magic":

                            #checking if they have the mana to cast the spell
                            if (player.magic == "magic quake" and player.mana >= 5) or (player.magic == "fireball" and player.mana >= 4) or (player.magic == "lightning bolt" and player.mana >= 3):

                                #removing mana 
                                if player.magic == "magic quake":
                                    player.mana -= 5
                                elif player.magic == "fireball":
                                    player.mana -= 4
                                else:
                                    player.mana -= 3    


                                if player_input[1] == "1" or player_input[1] == "one":
                                    e_index = 0
                                elif player_input[1] == "2" or player_input[1] == "two":
                                    e_index = 1
                                elif player_input[1] == "3" or player_input[1] == "three":
                                    e_index = 2
                                else:
                                    #in case index provided is false
                                    raise IndexError

                                #if its magic quake
                                if player.magic == "magic quake":
                                    #setting the e_index to each enemy 
                                    for e_index in range(len(i.enemies)):
                                        if i.enemies[e_index] is not None:
                                        #making the enemy take damage and checking if its dead
                                            if not i.enemies[e_index].take_damage(player.magic):
                                                #getting the index of the current room, putting that into the list of rooms, getting the current room class and changing the first enemy to None
                                                level.rooms[level.rooms.index(i)].enemies[e_index] = None
                                                print("enemy "+ player_input[1]+" has been defeated!")

                                                if i.enemies == [None] or i.enemies == [None, None] or i.enemies == [None, None, None]:
                                                    print("All enemies have been defeated!")
                                                

                                #if its any other magic
                                else:
                                    #if enemy has not been defeated yet
                                    if i.enemies[e_index] is not None:
                                        #making the enemy take damage and checking if its dead
                                        if not i.enemies[e_index].take_damage(player.magic):
                                            #getting the index of the current room, putting that into the list of rooms, getting the current room class and changing the first enemy to None
                                            level.rooms[level.rooms.index(i)].enemies[e_index] = None
                                            if i.enemies == [None] or i.enemies == [None, None] or i.enemies == [None, None, None]:
                                                print("All enemies have been defeated!")
                                            else:
                                                print("The enemy has been defeated!")

                                    #if enemy does not exist or has been defeated
                                    else:
                                        print("That enemy does not exist")
                            else:
                                print("The spell failed because you ran out of mana!")

                        #in case they didnt type weapon or magic
                        else:
                            print("Please check input and try again")
                            

                    except IndexError:
                        print("That enemy does not exist")

                    except :
                        print("Please check input and try again")
                    
                    




        elif player_input[0] == "check":

            #checking the room
            if player_input[-1] == "room":

                adjacent_rooms = []
                #north
                if [player.co_ords[0], player.co_ords[1]+1] in (level.occupied_rooms+level.special_rooms):
                    adjacent_rooms.append("north")
                
                #south
                if [player.co_ords[0], player.co_ords[1]-1] in (level.occupied_rooms+level.special_rooms):
                    adjacent_rooms.append("south")

                #east
                if [player.co_ords[0]+1, player.co_ords[1]] in (level.occupied_rooms+level.special_rooms):
                    adjacent_rooms.append("east")
                
                #west
                if [player.co_ords[0]-1, player.co_ords[1]] in (level.occupied_rooms+level.special_rooms):
                    adjacent_rooms.append("west")


                #getting room condition
                for i in level.rooms:
                    if i.co_ords == player.co_ords:
                        condition = i.room_type
                
                #print number of doors
                if len(adjacent_rooms) == 1:
                    print("A ", condition, "square room, with a door to the ", end="")
                else:
                    print("A ", condition, "square room, with doors to the ", end="")

                for i in adjacent_rooms[:-1]:
                    print(i, end=", ")
                print(adjacent_rooms[-1])

                print(player.co_ords, level.occupied_rooms, level.special_rooms)

            
            elif player_input[-1] == "status":
                player.display_stats()

            
            #check whats in player.inventory
            elif player_input[-1] == "bag":

                print("You have:")
                for key in player.inventory.keys():

                    if player.inventory[key] is not False:
                        print(key, ":",  player.inventory[key])
                    elif key is True:
                        print(key)

            #checking the map
            elif player_input[-1] == "map":

                #if player has bought the map
                if player.inventory["map"] == True:

                    #getting the limits of the map
                    limits = [[0,0], [0,0]]
                    for i in (level.occupied_rooms + level.special_rooms):

                        #if x is greater than the max x
                        if i[0] > limits[0][0]:
                            limits[0][0] = i[0]

                        #if x is less than the min x
                        elif i[0] < limits[0][1]:
                            limits[0][1] = i[0]

                        #if y is greater than the max y
                        if i[1] > limits[1][0]:
                            limits[1][0] = i[1]

                        #if y is less than the min y
                        elif i[1] < limits[1][1]:
                            limits[1][1] = i[1]

                    # print out the map, starting from the largest y down
                    for y in range(limits[1][0], limits[1][1] - 1, -1):

                        #the x, starting from min  and going to max
                        for x in range(limits[0][1], limits[0][0] + 1):
                            if [x,y] in level.special_rooms:
                                #boss
                                if [x,y] == level.special_rooms[0]:
                                    print("B", end="")
                                #key
                                elif [x,y] == level.special_rooms[1]:
                                    print("K", end = "")
                                #shop
                                elif [x,y] == level.special_rooms[-1]:
                                    print("S", end = "")
                                #fountain
                                else:
                                    print("F", end = "")

                            #if in occupied rooms, print character
                            elif [x,y] in level.occupied_rooms:
                                print("□", end = "")
                            
                            #if not a room
                            else:
                                print(" ", end = "")

                        #newline to denote y change
                        print("")
                    
                    #newline for visual cleanness
                    print("")

                else:
                    print("Dont have a map for this floor!")

            else:
                print("Perhaps you should check your input before you try and check whatever you just put in.")




            #FINISH CHECK
            #remember to add an else in case of wrong input 

        
        #movement command
        elif player_input[0] == "move":
            
            #making sure the function does not attempt to move twice
            move_patch = False

            #checking the actual room object
            for i in level.rooms:
                if i.co_ords ==player.co_ords and not move_patch:

                    #if no enemies are present
                    if i.enemies == [] or i.enemies == [None] or i.enemies == [None, None] or i.enemies == [None, None, None]:

                        #north
                        if player_input[-1] == "north":
                            #checks if room is there (looks in occupied_rooms and special_rooms) or if its a boss room and they have a key
                            if [player.co_ords[0], player.co_ords[1]+1 ] in level.occupied_rooms or [player.co_ords[0], player.co_ords[1]+1 ] in level.special_rooms[1:] or ([player.co_ords[0], player.co_ords[1]+1 ] == level.special_rooms[0] and player.inventory["key"]):
                                player.co_ords = [player.co_ords[0], player.co_ords[1]+1 ]
                                move_patch = True
                            

                            #in case its a boss door
                            elif ([player.co_ords[0], player.co_ords[1]+1 ] == level.special_rooms[0] and not player.inventory["key"]):
                                print("That door requires a key")

                            else:
                                print("that room does not exist")
                        #south
                        elif player_input[-1] == "south":
                            #checks if room is there (looks in occupied_rooms and special_rooms) or if its a boss room and they have a key
                            if [player.co_ords[0], player.co_ords[1]-1 ] in level.occupied_rooms or [player.co_ords[0], player.co_ords[1]-1 ] in level.special_rooms[1:] or ([player.co_ords[0], player.co_ords[1]-1 ] == level.special_rooms[0] and player.inventory["key"]):
                                player.co_ords = [player.co_ords[0], player.co_ords[1]-1 ]
                                move_patch = True

                            #in case its a boss door
                            elif ([player.co_ords[0], player.co_ords[1]-1 ] == level.special_rooms[0] and not player.inventory["key"]):
                                print("That door requires a key")

                            else:
                                print("that room does not exist")
                        
                        #east
                        elif player_input[-1] == "east":
                            #checks if room is there (looks in occupied_rooms and special_rooms) or if its a boss room and they have a key
                            if [player.co_ords[0]+1, player.co_ords[1] ] in level.occupied_rooms or [player.co_ords[0]+1, player.co_ords[1] ] in level.special_rooms[1:] or ([player.co_ords[0]+1, player.co_ords[1] ] == level.special_rooms[0] and player.inventory["key"]):
                                player.co_ords = [player.co_ords[0]+1, player.co_ords[1]]
                                move_patch = True

                            #in case its a boss door
                            elif ([player.co_ords[0]+1, player.co_ords[1] ] == level.special_rooms[0] and not player.inventory["key"]):
                                print("That door requires a key")

                            else:
                                print("that room does not exist")
                        
                        #west
                        elif player_input[-1] == "west":
                            #checks if room is there (looks in occupied_rooms and special_rooms) or if its a boss room and they have a key
                            if [player.co_ords[0]-1, player.co_ords[1] ] in level.occupied_rooms or [player.co_ords[0]-1, player.co_ords[1] ] in level.special_rooms[1:] or ([player.co_ords[0]-1, player.co_ords[1] ] == level.special_rooms[0] and player.inventory["key"]):
                                player.co_ords = [player.co_ords[0]-1, player.co_ords[1]]
                                move_patch = True

                            #in case its a boss door
                            elif ([player.co_ords[0]-1, player.co_ords[1] ] == level.special_rooms[0] and not player.inventory["key"]):
                                print("That door requires a key")

                            else:
                                print("That room does not exist")
                        
                        else:
                            print("Please enter a valid direction")

                        for i in level.rooms:
                            if i.co_ords == player.co_ords:
                                if not None in i.enemies and i.enemies != []:
                                    print("You are attacked by monsters!")
                                    
                                    for e in i.enemies:
                                        print("Monster" , i.enemies.index(e) + 1, ": a", e.name )
                                
                                #key room
                                elif i.co_ords == level.special_rooms[1]:
                                    if player.inventory["key"] == False:
                                        print("The room contains a key! \nYou place the key in your pocket")
                                    else:
                                        print("You've already taken the key from here!")
                                    player.inventory["key"] = True
                                
                                #fountain
                                elif i.co_ords == level.special_rooms[2]:
                                    print("Inside the room lays a large fountain, glowing with magic.\nIt looks safe to drink")
                                
                                #shop
                                elif i.co_ords == level.special_rooms[-1]:
                                    print("While you can't help but wonder why there is a shop in a dungeon, it is there nonetheless\nThe shopkeeper motions for you to buy something")
                                    print("For sale is:")
                                    for key in i.inventory.keys():
                                        print(key, i.inventory[key])


                    else:
                        print("You cannot leave the room while being attacked!")
        

        #buy command
        elif player_input[0] == "buy":

            #checking to see if player is in shop room
            if level.special_rooms[-1] == player.co_ords:

                #getting the actual shop object
                for i in level.rooms:
                    if i.co_ords == player.co_ords:

                        #checking if what they entered was correct
                        if player_input[-1] in i.inventory.keys(): 
                            
                            #checking if they have enough gold
                            if player.gold >= i.inventory[player_input[-1]] :

                                #taking away that gold and changing equipment
                                player.gold -= i.inventory[player_input[-1]]

                                #weapon
                                if player_input[-1] in ["mace", "spear", "sword"]:
                                    player.weapon = player_input[-1]

                                #magic
                                elif player_input[-1] in ["fireball", "lightning bolt", "magic quake"]:
                                    player.weapon = player_input[-1]
                                
                                #armour
                                elif player_input[-1] in ["leather", "breastplate", "plate"]:
                                    player.weapon = player_input[-1]
                                
                                #map
                                else:
                                    player.inventory["map"] = True


                                #removing the item from the shops inventory
                                level.rooms[level.rooms.index(i)].inventory.pop(player_input[-1])

                                print("The shopkeeper grunts in approval and hands over the goods")

                            else:
                                print("You'd want heavier pockets before eyeing that one! (Not enough gold!)" )



                        elif player_input == ["buy", "health", "potion"] or player_input == ["buy", "mana", "potion"]:
                             #checking if they have enough gold
                            if player.gold >= 10*(depth+1) :
                                player.inventory[(player_input[1], player_input[2])] += 1


                        else:
                            print("Whatever you're asking for, we dont sell that here")


            else:
                print("You have to be in a shop to buy something")


        #drinking from fountains and potions
        elif player_input[0] == "drink":
            
            #potions
            if player_input[-1] == "potion":

                if "health" in player_input and player.inventory["health potion"] > 0:
                    player.health = 10 + int(player.Con/2 -5)
                    print("Drank health potion, health fully recovered!")

                elif "mana" in player_input and player.inventory["mana potion"] > 0:
                    player.mana = 10 + int(player.Wis/2 -5)
                    print("Drank mana potion, mana fully recovered!")

                else:
                    print("Not enough potions of that type!")
            
            #fountain
            elif player_input[-1] == "fountain":
                if level.special_rooms[-2] == player.co_ords:
                    
                    #restoring health and mana
                    player.health = 10 + int(player.Con/2 -5)
                    player.mana = 10 + int(player.Wis/2 -5)

                    #removing the special qualities form the room
                    level.special_rooms.remove(player.co_ords)
                    level.occupied_rooms.append(player.co_ords)

                    print("The fountain crumbles to dust as you feel your body recovering. Health and mana have been restored!")

                else:
                    print("There is no fountain to drink from")

            else:
                print("Drink what now?")


        elif player_input[0] == "descend":

            #if player in boss room
            if player.co_ords == level.special_rooms[0]:
                for i in level.rooms:
                    #if there are no enemies
                    if player.co_ords ==i.co_ords and i.enemies == [None]:
                    
                        #restoring hp and mana
                        player.health = 10 + int(player.Con/2 -5)
                        player.mana = 10 + int(player.Wis/2 -5)
                        player.inventory["key"] = False
                        player.inventory["map"] = False

                        #resetting the level and increasing depth
                        depth += 1
                        player.co_ords = [0,0]
                        level = Level()

                        #next level message
                        print("You descend the ladder, exiting in a room of monsters!")

                        for i in level.rooms:
                            if i.co_ords == player.co_ords:
                                if not None in i.enemies and i.enemies != []:
                                    print("You are attacked by monsters!")
                                    
                                    for e in i.enemies:
                                        print("Monster" , i.enemies.index(e) + 1, ": a", e.name )
                    

            else:
                print("Only the boss room has a ladder!")

        #if input does not match any command
        else:
            print("Please check input and try again")
