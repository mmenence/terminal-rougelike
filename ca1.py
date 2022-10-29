#Joseph Paul Crowley
#121384736


import random
from random import randint













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


    #prints stats to screen
    def display_stats(self):

        print("health:" , self.health)
        print("mana:" , self.mana)

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
                damage = randint(1,8) + (player.Int // 2 -5)
            elif weapon == "lightning bolt":
                damage = randint(1,8) + (player.Int // 2 -5)
            elif weapon == "magic quake":
                damage = randint(1,8) + (player.Int // 2 -5)

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
        kwargs["weaknesses"] = ["pierce", "fireball"]
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
        
    


            ###         level class         ###

#level class
class Level:



                ###         generating the level            ###

    # was this the most legible or line-efficient method for writhing this out?
    # absolutely not. but it was definitely the most time efficient.
    # skip to line ~461 if you cant be bothered reading through it all
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
                self.current_room = random.choice(self.occupied_rooms)

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
                
            
            self.current_room = random.choice(self.occupied_rooms)


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
                self.current_room = random.choice(self.occupied_rooms)

        
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

            self.current_room = random.choice(self.occupied_rooms)

        
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
                self.current_room = random.choice(self.occupied_rooms)

        
        #generating key room
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
            
            self.current_room = random.choice(self.occupied_rooms)

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
                self.current_room = random.choice(self.occupied_rooms)

        
        #generating key room
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
           
            self.current_room = random.choice(self.occupied_rooms)




















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


    print(level.rooms[0].enemies)           #REPLACE -showing enemies in current room, replace with actual description

    #while player is not none, player is set to none on game over so the loop is broken
    while player != None:



        #taking the input and treating it
        #putting the input into lowercase, removing excess spaces, then splitting it into words for easier processing
        player_input = input().lower().strip().split()
        


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
                                    print("The enemy has been defeated!")

                            #if enemy does not exist or has been defeated
                            else:
                                print("That enemy does not exist")

                        
                        #magic 
                        elif player_input[-1] == "magic":


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

                            #if its any other magic
                            else:
                                #if enemy has not been defeated yet
                                if i.enemies[e_index] is not None:
                                    #making the enemy take damage and checking if its dead
                                    if not i.enemies[e_index].take_damage(player.magic):
                                        #getting the index of the current room, putting that into the list of rooms, getting the current room class and changing the first enemy to None
                                        level.rooms[level.rooms.index(i)].enemies[e_index] = None
                                        print("The enemy has been defeated!")

                                #if enemy does not exist or has been defeated
                                else:
                                    print("That enemy does not exist")

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
                if [player.co_ords[0], player.co_ords[1]+1] in level.occupied_rooms:
                    adjacent_rooms.append("north")
                
                #south
                if [player.co_ords[0], player.co_ords[1]-1] in level.occupied_rooms:
                    adjacent_rooms.append("south")

                #east
                if [player.co_ords[0]+1, player.co_ords[1]] in level.occupied_rooms:
                    adjacent_rooms.append("east")
                
                #west
                if [player.co_ords[0]-1, player.co_ords[1]] in level.occupied_rooms:
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

            
            elif player_input[-1] == "stats":
                player.display_stats()

            

            #FINISH CHECK
            #remember to add an else in case of wrong input 

        
        #movement command
        elif player_input[0] == "move":

            #north
            if player_input[-1] == "north":
                #checks if room is there (looks in occupied_rooms and special_rooms) or if its a boss room and they have a key
                if [player.co_ords[0], player.co_ords[1]+1 ] in level.occupied_rooms or [player.co_ords[0], player.co_ords[1]+1 ] in level.special_rooms[1:] or ([player.co_ords[0], player.co_ords[1]+1 ] == level.special_rooms[0] and player.inventory["key"]):
                    player.co_ords = [player.co_ords[0], player.co_ords[1]+1 ]

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

                #in case its a boss door
                elif ([player.co_ords[0]-1, player.co_ords[1] ] == level.special_rooms[0] and not player.inventory["key"]):
                    print("That door requires a key")

                else:
                    print("that room does not exist")
            
            else:
                print("Please enter a valid direction")

            

                


                    




                

    
    
    




