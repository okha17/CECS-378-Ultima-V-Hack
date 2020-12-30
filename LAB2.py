# Open save file from Ultima V allows use to read and write for a binary file
save_file = open("SAVED.GAM", "r+b")


# Function that retrieves character's strength using seek function and allows us to alter it
def strength(character):
    print("Change strength of character")
    # Gets the offset where the strength value is located for each character
    # Located in the same offset for every 32 bits for all 16 characters
    save_file.seek(0x0E + character)
    # User enters new strength value for character between 0-99
    new_strength = int(input("Enter new strength between 0-99: "))
    if 99 >= new_strength >= 0:
        # prints out the new hex value that is being placed at the offset for strength
        print("New hex value " + hex(new_strength))
        # to_bytes converts the new strength value into a byte value in little endian to place in the save file
        new_strength = new_strength.to_bytes(1, byteorder="little")
        # Write the new strength into the save file
        print("Strength has been updated!")
        save_file.write(new_strength)
    else:
        print("Invalid Strength value inputted!\nReturning to Menu...")


# Function that retrieves character's intelligence using seek function and allows us to alter it
def intelligence(character):
    print("Change intelligence of character")
    # Gets the offset where the strength value is located for each character
    # Located in the same offset for every 32 bits for all 16 characters
    save_file.seek(0x10 + character)
    # User enters new intelligence value for character between 0-99
    new_int = int(input("Enter new intelligence between 0-99: "))
    if 99 >= new_int >= 0:
        # prints out the new hex value that is being placed at the offset for intelligence
        print("New hex value " + hex(new_int))
        # to_bytes converts the new intelligence value into a byte value in little endian to place in the save file
        new_int = new_int.to_bytes(1, byteorder="little")
        # Write the new intelligence into the save file
        print("Intelligence has been updated!")
        save_file.write(new_int)
    else:
        print("Invalid Intelligence value inputted!\nReturning to Menu...")


# Function that retrieves character's intelligence using seek function and allows us to alter it
def dexterity(character):
    print("Change intelligence of character")
    # Gets the offset where the dexterity value is located for each character
    # Located in the same offset for every 32 bits for all 16 characters
    save_file.seek(0x1F + character)
    # User enters new dexterity value for character between 0-99
    new_dex = int(input("Enter new dexterity between 0-99: "))
    if 99 >= new_dex >= 0:
        # prints out the new hex value that is being placed at the offset for dexterity
        print("New hex value " + hex(new_dex))
        # to_bytes converts the new dex value into a byte value in little endian to place in the save file
        new_dex = new_dex.to_bytes(1, byteorder="little")
        # Write the new dexterity into the save file
        print("Dexterity has been updated!")
        save_file.write(new_dex)
    else:
        print("Invalid Dexterity value inputted!\nReturning to Menu...")


# Function that retrieves character's health points using seek function and allows us to alter it
def health_p(character):
    print("Change health of character")
    # Gets the offset where the health point value is located for each character
    # Located in the same offset for every 32 bits for all 16 characters
    save_file.seek(0x12 + character)
    # User enters new health point value for character between 0-999
    new_health = int(input("Enter new health points between 0-999: "))
    if 999 >= new_health >= 0:
        # prints out the new hex value that is being placed at the offset for health points
        print("New hex value " + hex(new_health))
        # to_bytes converts the new health point value into a word value in little endian to place in the save file
        new_health = new_health.to_bytes(2, byteorder="little")
        # Write the new health points into the save file
        print("Health points has been updated!")
        save_file.write(new_health)
    else:
        print("Invalid Health points value inputted!\nReturning to Menu...")


# Function that retrieves character's max health value using seek function and allows us to alter it
def health_max(character):
    print("Change health of character")
    # Gets the offset where the max health value is located for each character
    # Located in the same offset for every 32 bits for all 16 characters
    save_file.seek(0x14 + character)
    # User enters new max health value for character between 0-999
    new_health = int(input("Enter new max health between 0-999: "))
    if 999 >= new_health >= 0:
        # prints out the new hex value that is being placed at the offset for max health
        print("New hex value " + hex(new_health))
        # to_bytes converts the new max health value into a word value in little endian to placed in save file
        new_health = new_health.to_bytes(2, byteorder="little")
        # Write the new max health into save file
        print("Max Health has been updated!")
        save_file.write(new_health)
    else:
        print("Invalid Max Health value inputted!\nReturning to Menu...")


# Function that retrieves character's experience value using seek function and allows us to alter it
def experience(character):
    print("Change experience of character")
    # Gets the offset where the experience value is located for each character
    # Located in the same offset for every 32 bits for all 16 characters
    save_file.seek(0x16 + character)
    # User enters new experience value for character between 0-9999
    new_exp = int(input("Enter new experience between 0-99: "))
    if 9999 >= new_exp >= 0:
        # prints out the new hex value that is being placed at the offset for experience
        print("New hex value " + hex(new_exp))
        # to_bytes converts the new experience value into a word value in little endian to placed in save file
        new_exp = new_exp.to_bytes(2, byteorder="little")
        # Write the new experience into save file
        print("Experience has been updated!")
        save_file.write(new_exp)
    else:
        print("Invalid Experience value inputted!\nReturning to Menu...")


# Function that retrieves character's magic value using seek function and allows us to alter it
def magic(character):
    print("Change magic of character")
    # Gets the offset where the magic value is located for each character
    # Located in the same offset for every 32 bits for all 16 characters
    save_file.seek(0x11 + character)
    # User enters new magic value for character between 0-99
    new_mag = int(input("Enter new magic between 0-99: "))
    if 99 >= new_mag >= 0:
        # prints out the new hex value that is being placed at the offset for magic
        print("New hex value " + hex(new_mag))
        # to_bytes converts the new magic value into a byte value in little endian to placed in save file
        new_mag = new_mag.to_bytes(1, byteorder="little")
        # Write the new magic into save file
        print("Magic has been updated!")
        save_file.write(new_mag)
    else:
        print("Invalid Magic value inputted!\nReturning to Menu...")


# Function that retrieves gold value using seek function and allows us to alter it
def gold():
    print("Change gold amount")
    # Gets offset where gold value is located in save file
    save_file.seek(0x204)
    # User enters new gold value between 0-9999
    new_gold = int(input("Enter new gold between 0-9999: "))
    if 9999 >= new_gold >= 0:
        print("New hex value " + hex(new_gold))
        # to_bytes converts the new gold value into a word value in little endian to placed in save file
        new_gold = new_gold.to_bytes(2, byteorder="little")
        # Write new gold value into file
        print("Gold value has been updated!")
        save_file.write(new_gold)
    else:
        print("Invalid Gold value inputted!\nReturning to Menu...")


# Function that retrieves key value using seek function and allows us to alter it
def keys():
    print("Change amount of keys")
    # Gets offset where key value is located in save file
    save_file.seek(0x206)
    # User enters new key value between 0-100
    new_key = int(input("Enter new key amount between 0-100: "))
    if 100 >= new_key >= 0:
        print("New hex value " + hex(new_key))
        # to_bytes converts the new key value into a byte value in little endian to placed in save file
        new_key = new_key.to_bytes(1, byteorder="little")
        # Write new key value into file
        print("Key value has been updated!")
        save_file.write(new_key)
    else:
        print("Invalid Key value inputted!\nReturning to Menu...")


# Function that retrieves key value using seek function and allows us to alter it
def skull_keys():
    print("Change amount of skull keys")
    # Gets offset where key value is located in save file
    save_file.seek(0x20B)
    # User enters new key value between 0-100
    new_key = int(input("Enter new skull key amount between 0-100: "))
    if 100 >= new_key >= 0:
        print("New hex value " + hex(new_key))
        # to_bytes converts the new key value into a byte value in little endian to placed in save file
        new_key = new_key.to_bytes(1, byteorder="little")
        # Write new key value into file
        print("Skull Key value has been updated!")
        save_file.write(new_key)
    else:
        print("Invalid Skull Key value inputted!\nReturning to Menu...")


# Function that retrieves gem value using seek function and allows us to alter it
def gems():
    print("Change amount of gems")
    # Gets offset where key value is located in save file
    save_file.seek(0x206)
    # User enters new gem value between 0-100
    new_gem = int(input("Enter new gem amount between 0-100: "))
    if 100 >= new_gem >= 0:
        print("New hex value " + hex(new_gem))
        # to_bytes converts the new gem value into a byte value in little endian to placed in save file
        new_gem = new_gem.to_bytes(1, byteorder="little")
        # Write new gem value into file
        print("Gem value has been updated!")
        save_file.write(new_gem)
    else:
        print("Invalid Gem value inputted!\nReturning to Menu...")


# Function that retrieves black badge value using seek function and allows us to alter it
def black_badge():
    print("Add or remove Black Badge from inventory")
    # Gets offset where badge value is located in save file
    save_file.seek(0x218)
    # this item is either in the user's inventory or not so we let the user decide to add or remove it
    option = int(input("Enter 1 to have black badge and 0 to remove black badge: "))
    # if the user wants to remove the badge it is set to 0
    if option == 0:
        print("Black Badge removed from inventory!")
        print("New hex value " + hex(option))
        option = option.to_bytes(1, byteorder="little")
        save_file.write(option)
    # if the user wants to add the badge it is set to 255
    elif option == 1:
        # 255 value sets the badge to be in inventory
        value = 255
        print("Black Badge added to inventory!")
        print("New hex value " + hex(value))
        option = value.to_bytes(1, byteorder="little")
        save_file.write(option)
    else:
        print("Incorrect option picked!\nReturning to Menu...")


# Function that retrieves gem value using seek function and allows us to alter it
def magic_carpet():
    print("Change amount of magic carpets in inventory")
    # Gets offset where mag carpet value is located in save file
    save_file.seek(0x20A)
    # User enters new carpet value
    new_car = int(input("Enter new  magic carpet amount between 0-100: "))
    if 100 >= new_car >= 0:
        print("New hex value " + hex(new_car))
        # to_bytes converts the new carpet value into a byte value in little endian to placed in save file
        new_car = new_car.to_bytes(1, byteorder="little")
        # Write new carpet value into save file
        print("Magic Carpet value has been updated!")
        save_file.write(new_car)
    else:
        print("Invalid Magic Carpet value inputted!\nReturning to Menu...")


# Function that retrieves magic axe value using seek function and allows us to alter it
def magic_axe():
    print("Change amount of magic axes in inventory")
    # Gets offset where magic axe value is located in save file
    save_file.seek(0x240)
    # user enters new axe value
    new_axe = int(input("Enter new  magic carpet amount between 0-99: "))
    if 100 >= new_axe >= 0:
        print("New hex value " + hex(new_axe))
        # to_bytes converts the new axe value into a byte value in little endian to placed in save file
        new_axe = new_axe.to_bytes(1, byteorder="little")
        # Write new axe value into save file
        print("Magic Axe value has been updated!")
        save_file.write(new_axe)
    else:
        print("Invalid Magic Axe value inputted!\nReturning to Menu...")


# Function that displays the characters that you can edit in the save file
def player_menu():
    print("\nPlayer Characters:")
    print("1) Main Character")
    print("2) Shamino ")
    print("3) Iolo")
    print("4) Mariah")
    print("5) Geoffery")
    print("6) Janna")
    print("7) Julia")
    print("8) Dupre")
    print("9) Katrina")
    print("10) Sentri")
    print("11) Gwenno")
    print("12) Johne")
    print("13) Gorn")
    print("14) Maxwell")
    print("15) Toshi")
    print("16) Sadju\n")

    # Allows user to select which character they would like to edit each character starts at
    # the next 32 bit value
    choice = int(input("Enter the number for which character's stats you want to edit: "))

    if choice == 1:
        print("Editing Player Character's stats")
        return 0
    elif choice == 2:
        print("Editing Shamino's stats")
        return 32
    elif choice == 3:
        print("Editing Iolo's stats")
        return 64
    elif choice == 4:
        print("Editing Mariah's stats")
        return 96
    elif choice == 5:
        print("Editing Geoffery's stats")
        return 128
    elif choice == 6:
        print("Editing Janna's stats")
        return 160
    elif choice == 7:
        print("Editing Julia's stats")
        return 192
    elif choice == 8:
        print("Editing Dupre's stats")
        return 224
    elif choice == 9:
        print("Editing Katrina's stats")
        return 256
    elif choice == 10:
        print("Editing Sentri's stats")
        return 288
    elif choice == 11:
        print("Editing Gwenno's stats")
        return 320
    elif choice == 12:
        print("Editing Johne's stats")
        return 352
    elif choice == 13:
        print("Editing Gorn's stats")
        return 384
    elif choice == 14:
        print("Editing Maxwell's stats")
        return 416
    elif choice == 15:
        print("Editing Toshi's stats")
        return 448
    elif choice == 16:
        print("Editing Sadju's stats")
        return 480
    else:
        print("Incorrect number inputted!\n")


# Function that allows the user to select which skill they would like to edit of the user
# passes in the player_menu() function that retrieves which character is being edited
def skill_menu(player):
    print("\nPlayer Stats:")
    print("1) Strength ")
    print("2) Intelligence")
    print("3) Dexterity")
    print("4) Health points")
    print("5) Max Health")
    print("6) Experience")
    print("7) Magic\n")

    # The selected stat for a specific character is changed through user choice and the call to stat functions
    choice = int(input("Enter which stat you would like to change for the selected character: "))

    if choice == 1:
        strength(player)
    elif choice == 2:
        intelligence(player)
    elif choice == 3:
        dexterity(player)
    elif choice == 4:
        health_p(player)
    elif choice == 5:
        health_max(player)
    elif choice == 6:
        experience(player)
    elif choice == 7:
        magic(player)
    else:
        print("Incorrect option inputted!\n")


# Main menu that the program starts from where the user can select which aspects of the game they would like to edit
user_choice = 0
while user_choice != 9:
    print("\nItem and Character Stat Changer for Ultima V")
    print("Select what you would like to edit:")
    print("1) Select Player to edit")
    print("2) Change amount of Gold in inventory")
    print("3) Change amount of Keys in inventory")
    print("4) Change amount of Skull Keys in inventory")
    print("5) Change amount of Gems in inventory")
    print("6) Add or remove Black Badge to inventory")
    print("7) Change amount of Magic Carpets in inventory")
    print("8) Change amount of Magic Axes ")
    print("9) Quit Game")

    user_choice = int(input("Enter your choice: \n"))
    if user_choice == 1:
        skill_menu(player_menu())  # For editing character's stats
    elif user_choice == 2:
        gold()
    elif user_choice == 3:
        keys()
    elif user_choice == 4:
        skull_keys()
    elif user_choice == 5:
        gems()
    elif user_choice == 6:
        black_badge()
    elif user_choice == 7:
        magic_carpet()
    elif user_choice == 8:
        magic_axe()
    elif user_choice == 9:
        print("Quitting Program!")
        # Close the save file
        save_file.close()
        break
    else:
        print("\nNot a valid choice! \nTry Again")
