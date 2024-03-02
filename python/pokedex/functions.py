import sys
import lists

# default values
user_action = 0
name = ""
pokemon_name = ""
pokemon_id = 0

def body():
    intro()
    main_menu()

def intro():
    print("Welcome to PyPokedex!\nPlease note that is only supports Gen 1 Pokemon list.\n")
    global name
    name = input("Please provide your name: ")
    print(f"Hello, {name}!")

def main_menu():
    global user_action
    print("\nAvailable actions:\n1. List of all Generation 1 Pokemon.\n2. Search Pokemon by PyPokedex ID.\n3. Check Pokemon's PyPokedex ID.\n4. List of all Pokemon caught.\n5. Add Pokemon to the caught list.\n6. List of all Pokemon yet to be caught.\n7. Check Pokemon details (name, PyPokedex ID, if caught).\n8. Check your stats.\n\nIf you want to exit PyPokedex, please type in 2137.\n\n")
    user_action = int(input("Please type the number of an option you want to go to. "))
    action()

def action():
    global user_action
    global pokemon_id
    global pokemon_name

    if user_action == 1:
        all_pokemon_list()

    elif user_action == 2:
        search_by_id()

    elif user_action == 3:
        search_by_name()

    elif user_action == 4:
        caught_pokemon_list()

    elif user_action == 5:
        add_pokemon()

    elif user_action == 6:
        remaining_pokemon_list()

    elif user_action == 7:
        pokemon_details()

    elif user_action == 8:
        stats()

    elif user_action == 2137:
        input("\n\nPress any key to confirm.")
        sys.exit()

    else:
        print("\n\n!!! Incorrect number. Please use a number of a corresponding option above. !!!\n\n")
        user_action = int(input("Please type the number of an option you want to go to. "))
        action()


def search_by_id():
    global pokemon_id
    global pokemon_name

    print("This section allows you to search Pokemon's name by their PyPokedex ID. Please note that after displaying the name PyPokedex will go back to main menu.\n")
    pokemon_id = int(input("\nType in PyPokedex ID of Pokemon you are looking for: "))

    for key, value in lists.pokemon_list.items():
        if value == pokemon_id:
            pokemon_name = key
            print(f"\nPokemon that has Pokedex ID {pokemon_id} is: {pokemon_name}.\n")
    
    input("\nPress any button go to back to main menu.")
    main_menu()

def search_by_name():
    global pokemon_id
    global pokemon_name

    print("This section allows you to search Pokemon's ID by their name. Please note that after displaying the value PyPokedex will go back to main menu.\n")
    pokemon_name = input("\nType in name of Pokemon you are looking for: ")

    pokemon_id = lists.pokemon_list[pokemon_name]
    print(f"\nPokedex ID of {pokemon_name} is: {pokemon_id}.")
    
    input("\nPress any button go to back to main menu.")
    main_menu()

def all_pokemon_list():
    global pokemon_id

    print("\nFull list of all Generation 1 Pokemon:\n\n")

    for pokemon in lists.pokemon_list:
        pokemon_id = lists.pokemon_list[pokemon]
        print(f"{pokemon_id}. {pokemon}")
        pokemon_id += 1

    input("\nPress any button go to back to main menu.")
    main_menu()

def caught_pokemon_list():
    global pokemon_id

    if not lists.caught_pokemon_list:
        print("\nYou have not caught any Pokemon yet.")

    else:
        print("\nFull list of all Generation 1 Pokemon that you have caught:\n\n")

        for pokemon in lists.caught_pokemon_list:
            pokemon_id = lists.caught_pokemon_list[pokemon]
            print(f"{pokemon_id}. {pokemon}")
            pokemon_id += 1

    input("\nPress any button go to back to main menu.")
    main_menu()

def remaining_pokemon_list():
    global pokemon_id

    if not lists.caught_pokemon_list:
        print("\nYou have caught all Pokemon, congratulations!")

    else:
        print("\nFull list of all Generation 1 Pokemon that you have not yet caught:\n\n")

        for pokemon in lists.remaining_pokemon_list:
            pokemon_id = lists.remaining_pokemon_list[pokemon]
            print(f"{pokemon_id}. {pokemon}")
            pokemon_id += 1

    input("\nPress any button go to back to main menu.")
    main_menu()

def pokemon_details():
    global pokemon_id
    global pokemon_name
    global name

    choice = input("\nDo you want to search by NAME or ID? (Please use all caps) ").upper()


    if choice == "NAME":
        pokemon_name = input("\nType in name of Pokemon you are looking for: ")

        if pokemon_name in lists.pokemon_list.keys():
            pokemon_id = lists.pokemon_list[pokemon_name]

            caught_check = pokemon_name

            if caught_check in lists.caught_pokemon_list.keys():
                print(f"\nPokemon name: {pokemon_name}\nPokemon ID: {pokemon_id}\nPokemon has been caught by {name}.")
            
            else:
                print(f"\nPokemon name: {pokemon_name}\nPokemon ID: {pokemon_id}\nPokemon hasn't been caught.")

        else:
                print("\n\n!!! Incorrect value. Please use a correct value (either Pokemon ID or Pokemon's name). !!!\n\n")
                pokemon_details()
    
    elif choice == "ID":
        pokemon_id = int(input("\nType in ID of Pokemon you are looking for: "))

        if pokemon_id in lists.pokemon_list.values():
            
            for key, value in lists.pokemon_list.items():
                if value == pokemon_id:
                    pokemon_name = key

            caught_check = pokemon_name

            if caught_check in lists.caught_pokemon_list.keys():
                print(f"\nPokemon name: {pokemon_name}\nPokemon ID: {pokemon_id}\nPokemon has been caught by {name}.")
            
            else:
                print(f"\nPokemon name: {pokemon_name}\nPokemon ID: {pokemon_id}\nPokemon hasn't been caught.")

        else:
                print("\n\n!!! Incorrect value. Please use a correct value (either Pokemon ID or Pokemon's name). !!!\n\n")
                pokemon_details()
                
    elif choice != "ID" and choice != "NAME":
        print("\n\n!!! Incorrect value. Please use a correct value (either Pokemon ID or Pokemon's name). !!!\n\n")
        pokemon_details()

    input("\nPress any button go to back to main menu.")
    main_menu()

def add_pokemon():
    global pokemon_id
    global pokemon_name

    pokemon_name = input("\nType in name of Pokemon you have caught: ")
    pokemon_id = lists.pokemon_list[pokemon_name]

    lists.caught_pokemon_list[pokemon_name] = pokemon_id

    del lists.remaining_pokemon_list[pokemon_name]

    print(f"\nCongrats on catching {pokemon_name}! Your new friend has been added to the list.\n")

    input("\nPress any button go to back to main menu.")
    main_menu()

def stats():
    global name

    amount_caught = len(lists.caught_pokemon_list)
    amount_remaining = len(lists.remaining_pokemon_list)

    if not lists.caught_pokemon_list:
        print(f"\n{name}'s Pokemon stats:\nPokemon caught: {amount_caught}\nPokemon not yet caught: {amount_remaining}\n")

    else:
        last_pokemon = list(lists.caught_pokemon_list)[-1]

        print(f"\n{name}'s Pokemon stats:\nPokemon caught: {amount_caught}\nPokemon not yet caught: {amount_remaining}\nLast caught Pokemon: {last_pokemon}.\n")

    input("\nPress any button go to back to main menu.")
    main_menu()

