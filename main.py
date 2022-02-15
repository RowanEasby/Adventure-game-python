from room import Room
from character import Enemy
from character import Character
from character import Friend
from rpginfo import RPGInfo
from item import Item
dead = False
bag = []

#Intro
RPGInfo.info()
full_title = RPGInfo("Mark's Manor")
full_title.welcome()

RPGInfo.author = "me"
RPGInfo.credits()



#Room creation
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_room = Room("Dining Hall")
dining_room.set_description("A large room with ornate golden decorations on each wall.")
ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")
bathroom = Room("bathroom")
bathroom.set_description("A large bathroom for one person. Everything is covered in dust")
entrance_hall = Room("Entrance hall")
entrance_hall.set_description("A once lavish entrance hall. Now the ceiling is caving in")
main_hall = Room("Main hall")
main_hall.set_description("The main hall of the manor. The wooden floor is rotting in places")
hallway = Room("Hallway")
hallway.set_description("A long hallway. some of the rooms to the sides are blocked by rubble")


#room linking
entrance_hall.link_room(main_hall, "west")

main_hall.link_room(entrance_hall, "east")
main_hall.link_room(bathroom, "south")
main_hall.link_room(hallway, "west")
main_hall.link_room(dining_room, "north")
                        
bathroom.link_room(main_hall, "north")

ballroom.link_room(hallway, "north")
                        
hallway.link_room(ballroom, "south")
hallway.link_room(main_hall, "east")

dining_room.link_room(main_hall, "south")
dining_room.link_room(kitchen, "west")

kitchen.link_room(dining_room, "east")


#Room count
print("\n")
print("There are " +str(Room.number_of_rooms) + " rooms to explore")



#Enemy creation and location
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_room.set_character(dave)


#Friend creation and location
mark = Friend("Mark", "Everyones favourite cable guy!")
mark.set_conversation("I'm going to lose it")
ballroom.set_character(mark)

#Item creation and location
cheese = Item("cheese", "You don't know what kind of cheese it is, but it seems ok to eat.")
kitchen.set_item(cheese)

print("To win, you must kill all enemies")
print("Enemies remaining: " +str(Enemy.number_of_enemies))

current_room = entrance_hall      

#Begins user input command loop
while dead == False:
    print("\n")         
    current_room.get_details()

    #Checks for a character
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        print("\n")
        inhabitant.describe()

    room_item = current_room.get_item()
    if room_item is not None:
        print("\n")
        room_item.describe()

    #user input    
    command = input("> ")
    print("\n")
    #Check if the command is a direction
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    #Checks if the commands is "talk"
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is nobody to talk to here. Go find some friends.")



    #Checks if the command is "fight"
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            print(bag)
            fight_with = input()
            
        #Does the user have the item in their bag?
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("You won the fight")
                    current_room.set_character(None)
                    Enemy.number_of_enemies = Enemy.number_of_enemies - 1
                    print("Enemies remaining: " +str(Enemy.number_of_enemies))
                    if Enemy.number_of_enemies <=0:
                        print("You have successfully beaten all enemies. Congratulations!")
                        dead = True
                else:
                    print("You lost the fight")
                    print("\n")
                    print("GAME OVER")
                    dead = True
            else:
                print("\n")
                print("You don't have that item")
        else:
            print("\n")
            print("There is nobody to fight here. Don't be so violent")




    #Checks of the commands is "hug"
    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("\n")
                print("You hug " + inhabitant.name + " and they crush your throat")
                print("\n")
                print("GAME OVER")
                dead = True
            else:
                inhabitant.hug()
        else:
            print("\n")
            print("Who are you trying to hug?")


    #Commands to take the item in the current room
    elif command == "take":
        if room_item is not None:
            bag.append(room_item.name)
            current_room.set_item(None)


    #Command to check the users inventory
    elif command == "bag":
        print(bag)


    #If the command isn't recognised
    else:
        print("You can't do that here")


                
