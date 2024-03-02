import random
import sys

# required data

ambidex = ["ALLY", "BETRAY"]
enemy_names = ["Zero", "Sigma", "Phi", "Alice", "Luna", "Dio", "Quark", "Tenmyouji", "Clover", "K"]
true_false = ["true", "false"]

print("The Ambidex Game will now begin.\n")
print("Rules are as follows:\n1. If both you and your opponent choose ALLY, both of you will receive 2 points.\n2. If both of you will choose BETRAY, no points will be added.\n3. If you choose ALLY and your opponent chooses BETRAY, you lose 2 points while they gain 3 points. If you choose BETRAY while they choose ALLY, you will receive 3 points and they will lose 2.\n4. You need at least 9 points to win the game.\n5. If your score will drop below 0, you will be punished.\nHave a nice tragedy!\n")

Player_A = str(input("Please provide your name: "))

Player_B = random.choice(enemy_names)
enemy_names.remove(Player_B)

Player_C = random.choice(enemy_names)

# setting the score

player_score = 0
opponent_score = 0

# pairing up

pairing = random.choice(true_false)

if pairing == "true":
    print(f"You are playing as a PAIR. Your partner is {Player_B}.")
    print(f"Your opponent is {Player_C}.\n")

    while player_score < 9 or opponent_score < 9 or player_score > -1 or opponent_score > -1:
        if player_score >= 9 or opponent_score >= 9:
            print("The game has concluded.")
            if player_score >= 9:
                print("You have won the Ambidex Game. Congratulations! Please go to Door 9.")
                input("Press any key to quit.")
                sys.exit()
                
            elif opponent_score >= 9:
                print("You have lost the Ambidex Game. Please await your punishment.")
                input("Press any key to quit.")
                sys.exit()

        elif player_score < 0 or opponent_score < 0:
            if opponent_score < 0:
                print("You have won the Ambidex Game. Congratulations! Please go to Door 9.")
                input("Press any key to quit.")
                sys.exit()
                
            elif player_score < 0:
                print("You have lost the Ambidex Game. Please await your punishment.")
                input("Press any key to quit.")
                sys.exit()

# the main game logic 
                
        else:
            print(f"It is your turn, {Player_A}. Do you wish to Ally or Betray {Player_C}?")
            player_choice = input("Please provide your answer by typing either ALLY or BETRAY: ").upper()

            if player_choice != "ALLY" and player_choice != "BETRAY":
                print("\n!!! Unknown command. Round will be skipped. !!!\n")
            
            else:
                opponent_choice = random.choice(ambidex)
                print(f"{Player_A} and {Player_B} have chosen {player_choice}.")
                print(f"{Player_C} has chosen {opponent_choice}.")


            if player_choice == "ALLY" and opponent_choice == "ALLY":
                player_score += 2
                opponent_score += 2
            elif player_choice == "BETRAY" and opponent_choice == "BETRAY":
                player_score += 0
                opponent_score += 0
            elif player_choice == "ALLY" and opponent_choice == "BETRAY":
                player_score -= 2
                opponent_score += 3
            elif player_choice == "BETRAY" and opponent_choice == "ALLY":
                player_score += 3
                opponent_score -= 2
            
            print(f"{Player_A} and {Player_B}'s score is {player_score}.")
            print(f"{Player_C}'s score is {opponent_score}.\n")

if pairing == "false":
    print(f"You are playing as a SOLO.")
    print(f"Your opponents are {Player_B} and {Player_C}.\n")

    while player_score < 9 or opponent_score < 9 or player_score > -1 or opponent_score > -1:
        if player_score >= 9 or opponent_score >= 9:
            print("The game has concluded.")
            if player_score >= 9:
                print("You have won the Ambidex Game. Congratulations! Please go to Door 9.")
                input("Press any key to quit.")
                sys.exit()
                
            elif opponent_score >= 9:
                print("You have lost the Ambidex Game. Please await your punishment.")
                input("Press any key to quit.")
                sys.exit()

        elif player_score < 0 or opponent_score < 0:
            if opponent_score < 0:
                print("You have won the Ambidex Game. Congratulations! Please go to Door 9.")
                input("Press any key to quit.")
                sys.exit()
                
            elif player_score < 0:
                print("You have lost the Ambidex Game. Please await your punishment.")
                input("Press any key to quit.")
                sys.exit()

# the main game logic 
                
        else:
            print(f"It is your turn, {Player_A}. Do you wish to Ally or Betray {Player_B} and {Player_C}?")
            player_choice = input("Please provide your answer by typing either ALLY or BETRAY: ").upper()

            if player_choice != "ALLY" and player_choice != "BETRAY":
                print("\n!!! Unknown command. Round will be skipped. !!!\n")
            
            else:
                opponent_choice = random.choice(ambidex)
                print(f"{Player_A} has chosen {player_choice}.")
                print(f"{Player_B} and {Player_C} have chosen {opponent_choice}.")

            if player_choice == "ALLY" and opponent_choice == "ALLY":
                player_score += 2
                opponent_score += 2
            elif player_choice == "BETRAY" and opponent_choice == "BETRAY":
                player_score += 0
                opponent_score += 0
            elif player_choice == "ALLY" and opponent_choice == "BETRAY":
                player_score -= 2
                opponent_score += 3
            elif player_choice == "BETRAY" and opponent_choice == "ALLY":
                player_score += 3
                opponent_score -= 2
            
            print(f"{Player_A}'s score is {player_score}.")
            print(f"{Player_B} and {Player_C}'s score is {opponent_score}.\n")