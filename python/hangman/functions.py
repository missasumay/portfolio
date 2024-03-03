import random
import art
import words
import sys

score = 0

end_of_game = False

en_try_again = "Y"
pl_try_again = "TAK"

def pl_easy():
    global score
    global end_of_game 

    display = []

    chosen_word = random.choice(words.polski_easy)

    for letter in chosen_word:
        display.append("_")

    for letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == " " or letter == "-":
                display[position] = letter

    lives = 6

    while not end_of_game:
        guess = input("\nPodaj wybraną literę: ").lower()

        if guess in display:
                print("Ta litera została już wykorzystana. Wybierz inną.")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print("Tej litery nie ma w tym słowie. Tracisz jedną szansę.")
            lives -= 1

            print(art.stages[lives])
            
            if lives == 0:
                end_of_game = True
                print(f"Przegrywasz. Twoje słowo to {chosen_word}.\nTwój wynik ogólny to {score}.\n")


        print(f"{' '.join(display)}")


        if "_" not in display:
            end_of_game = True
            score += 1
            print(f"Gratulacje, wygrywasz! Twój wynik to {score}.\n")

def pl_medium():
    global score
    global end_of_game 

    display = []

    chosen_word = random.choice(words.polski_medium)

    for letter in chosen_word:
        display.append("_")

    for letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == " " or letter == "-":
                display[position] = letter

    lives = 6

    while not end_of_game:
        guess = input("\nPodaj wybraną literę: ").lower()

        if guess in display:
                print("Ta litera została już wykorzystana. Wybierz inną.")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print("Tej litery nie ma w tym słowie. Tracisz jedną szansę.")
            lives -= 1

            print(art.stages[lives])
            
            if lives == 0:
                end_of_game = True
                print(f"Przegrywasz. Twoje słowo to {chosen_word}.\nTwój wynik ogólny to {score}.\n")


        print(f"{' '.join(display)}")


        if "_" not in display:
            end_of_game = True
            score += 1
            print(f"Gratulacje, wygrywasz! Twój wynik to {score}.\n")

def pl_hard():
    global score
    global end_of_game 

    display = []

    chosen_word = random.choice(words.polski_hard)

    for letter in chosen_word:
        display.append("_")

    for letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == " " or letter == "-":
                display[position] = letter

    lives = 6

    while not end_of_game:
        guess = input("\nPodaj wybraną literę: ").lower()

        if guess in display:
                print("Ta litera została już wykorzystana. Wybierz inną.")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print("Tej litery nie ma w tym słowie. Tracisz jedną szansę.")
            lives -= 1

            print(art.stages[lives])
            
            if lives == 0:
                end_of_game = True
                print(f"Przegrywasz. Twoje słowo to {chosen_word}.\nTwój wynik ogólny to {score}.\n")


        print(f"{' '.join(display)}")


        if "_" not in display:
            end_of_game = True
            score += 1
            print(f"Gratulacje, wygrywasz! Twój wynik to {score}.\n")

def en_easy():
    global score
    global end_of_game 

    display = []

    chosen_word = random.choice(words.english_easy)

    for letter in chosen_word:
        display.append("_")

    for letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == " " or letter == "-":
                display[position] = letter

    lives = 6

    while not end_of_game:
        guess = input("\nGuess a letter: ").lower()

        if guess in display:
                print("This letter has already been guessed. Please enter a different one.")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print("This letter is not in the word. You are losing one chance.")
            lives -= 1

            print(art.stages[lives])
            
            if lives == 0:
                end_of_game = True
                print(f"You have lost. The word was {chosen_word}.\nYour score is {score}.\n")


        print(f"{' '.join(display)}")


        if "_" not in display:
            end_of_game = True
            score += 1
            print(f"Congrats, you have won! Your score is now {score}.\n")

def en_medium():
    global score
    global end_of_game 

    display = []

    chosen_word = random.choice(words.english_medium)

    for letter in chosen_word:
        display.append("_")

    for letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == " " or letter == "-":
                display[position] = letter

    lives = 6

    while not end_of_game:
        guess = input("\nGuess a letter: ").lower()

        if guess in display:
                print("This letter has already been guessed. Please enter a different one.")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print("This letter is not in the word. You are losing one chance.")
            lives -= 1

            print(art.stages[lives])
            
            if lives == 0:
                end_of_game = True
                print(f"You have lost. The word was {chosen_word}.\nYour score is {score}.\n")


        print(f"{' '.join(display)}")


        if "_" not in display:
            end_of_game = True
            score += 1
            print(f"Congrats, you have won! Your score is now {score}.\n")

def en_hard():
    global score
    global end_of_game 

    display = []

    chosen_word = random.choice(words.english_hard)

    for letter in chosen_word:
        display.append("_")

    for letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == " " or letter == "-":
                display[position] = letter

    lives = 6

    while not end_of_game:
        guess = input("\nGuess a letter: ").lower()

        if guess in display:
                print("This letter has already been guessed. Please enter a different one.")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print("This letter is not in the word. You are losing one chance.")
            lives -= 1

            print(art.stages[lives])
            
            if lives == 0:
                end_of_game = True
                print(f"You have lost. The word was {chosen_word}.\nYour score is {score}.\n")


        print(f"{' '.join(display)}")


        if "_" not in display:
            end_of_game = True
            score += 1
            print(f"Congrats, you have won! Your score is now {score}.\n")



def polski():
    global end_of_game
    global pl_try_again
    
    print(art.pl_logo)
    difficulty = input("Proszę wybrać poziom trudności - ŁATWY, ŚREDNI lub TRUDNY: ").upper()

    if difficulty == "ŁATWY":
        pl_easy()

    if difficulty == "ŚREDNI":
        pl_medium()

    if difficulty == "TRUDNY":
        pl_hard()

    if difficulty != "ŁATWY" and difficulty != "ŚREDNI" and difficulty != "TRUDNY":
        print("!!! Niepoprawny poziom trudności. !!!\n")
        polski()

    while pl_try_again == "TAK":
        pl_try_again = input("Czy chcesz zagrać ponownie? Wpisz TAK lub NIE (wpisanie innej wartości spowoduje zakończenie gry): ").upper()

        if pl_try_again == "TAK":
            end_of_game = False
            difficulty = input("Proszę wybrać poziom trudności - ŁATWY, ŚREDNI lub TRUDNY: ").upper()

            if difficulty == "ŁATWY":
                pl_easy()

            if difficulty == "ŚREDNI":
                pl_medium()

            if difficulty == "TRUDNY":
                pl_hard()

            if difficulty != "ŁATWY" and difficulty != "ŚREDNI" and difficulty != "TRUDNY":
                print("!!! Niepoprawny poziom trudności. !!!\n")
                polski()

        if pl_try_again != "TAK":
                    input("Dziękuję za grę! Wciśnij dowolny przycisk aby zakończyć.")
                    sys.exit()

def english():
    global end_of_game
    global en_try_again

    print(art.en_logo)
    difficulty = input("Please choose difficulty level - EASY, MEDIUM or HARD: ").upper()

    if difficulty == "EASY":
        en_easy()

    if difficulty == "MEDIUM":
        en_medium()

    if difficulty == "HARD":
        en_hard()

    if difficulty != "EASY" and difficulty != "MEDIUM" and difficulty != "HARD":
        print("!!! Incorrect difficulty level. !!!\n")
        english()

    while en_try_again == "Y":

        en_try_again = input("Would you like to try again? Y or N (typing other option will exit the game): ").upper()

        if en_try_again == "Y":
            end_of_game = False
            difficulty = input("Please choose difficulty level - EASY, MEDIUM or HARD: ").upper()

            if difficulty == "EASY":
                en_easy()

            if difficulty == "MEDIUM":
                en_medium()

            if difficulty == "HARD":
                en_hard()

            if difficulty != "EASY" and difficulty != "MEDIUM" and difficulty != "HARD":
                print("!!! Incorrect difficulty level. !!!\n")
                english()

        if en_try_again != "Y":
            input("Thank you for playing! Press any key to exit.")
            sys.exit()