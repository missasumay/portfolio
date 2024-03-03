import lists
import sys
import random

# setting up default values

toy_number = 0
go_up = ""
go_right = 0
chances = 0
empty_spot = "⬜"
toy_name = ""
amount_of_toys = len(lists.collected_toys)
toys_left = 0

def intro():
    print("Welcome to the PyClaw Game!\n")
    print("Rules are as follows:\n1. Game will randomly choose an amount of toys that you'll be able to grab and redistribute them on the grid.\n2. Toys will be displayed on the grid as colorful squares.\n3. When asked, you will need to provide a number from 1 to 6 to decide how far up and how far right you want to go to catch a toy.\n4. If you're gonna miss a square with a toy, the round will start again (don't worry, grid won't be reset).\n5. If you'll input correct coordinates, the game will then calculate your chances of actually catching the toy.\n6. If the almighty gods of Python will decide that you can catch the toy, the corresponding icon on the grid will be changed to a white square and you'll see the name of the toy you got.\n7. Game continues until you catch all the toys.\n\nHave fun!\n")

def outro():
    print("Thank you for playing!\n")
    input("Press any key to exit.")
    sys.exit()

def generate_grid():
    global toy_number
    global toys_left

    # define amount of toys that Player will be able to collect
    toy_number = random.randint(3, 15)
    toys_left = toy_number

    # place toys in random positions on the grid

    for toy in range(0, toy_number):
        toy = random.choice(lists.toys_colors)
        row = random.choice(lists.grid)
        placement = random.randint(0, 5)
        row[placement] = toy

    # print final version of the grid
    print(f"{' '.join(lists.line1)}\n{' '.join(lists.line2)}\n{' '.join(lists.line3)}\n{' '.join(lists.line4)}\n{' '.join(lists.line5)}\n{' '.join(lists.line6)}")


def player_action():
    global go_up
    global go_right
    global empty_spot
    global chances
    global toy_name
    global amount_of_toys
    global toys_left

    # have Player decide how high they want to go
    go_up = str(input("\nHow many spots UP you want to move your claw? Type in number between 1 and 6: "))

    # assign correct list
    if go_up == "1":
        go_up = lists.line6
    elif go_up == "2":
        go_up = lists.line5
    elif go_up == "3":
        go_up = lists.line4
    elif go_up == "4":
        go_up = lists.line3
    elif go_up == "5":
        go_up = lists.line2
    elif go_up == "6":
        go_up = lists.line1
    else:
        print("Number out of range. Round will be reset.")
        player_action()

    # have Player decide how far right they want to go
    go_right = int(input("How many spots RIGHT you want to move your claw? Type in number between 1 and 6: ")) - 1

    if go_right <= 0 and go_right >= 5:
        print("Number out of range. Round will be reset.")
        player_action()

    # if there is a toy in a chosen spot

    if empty_spot != go_up[go_right]:
        
        # calculate a number that will be defining if Player caught the toy or not

        chances = random.randrange(0, 11)

        # Player required at least 6 to grab a toy. Logic if that requirement is met:

        if chances >= 6:
            toy_name = random.choice(lists.toys_names)
            lists.collected_toys.append(toy_name)

            go_up[go_right] = empty_spot

            toys_left -= 1
            amount_of_toys += 1

            print(f"Congrats, you got a {toy_name}!\n")
            print(f"You caught {amount_of_toys} toys out of {toy_number}. Keep going!\n")
            print("List of all caught toys: ")
            print(*lists.collected_toys, sep = ", ")
            print(" ")
            print(f"{' '.join(lists.line1)}\n{' '.join(lists.line2)}\n{' '.join(lists.line3)}\n{' '.join(lists.line4)}\n{' '.join(lists.line5)}\n{' '.join(lists.line6)}")

            # logic to check if all toys are caught, if so - end the game

            if toys_left > 0:
                player_action()
            else:
                outro()
        
        # if Player will roll less than 6

        else:
            print("Oh no, you dropped your toy! Try again!\n")
            
            player_action()

    # if there is no toy in the spot chosen by the Player

    if go_up[go_right] == empty_spot:
        print("There is no toy in this spot. Try again!\n")
        player_action()

