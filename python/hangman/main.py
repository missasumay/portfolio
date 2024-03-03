# wybor jezyka > logo gry ASCII w danym jez > wybor poziomu trudnosci > normalny hangman > zapisanie wyniku > replay > exit jak nie replay

import functions

def choose_language():
    lang = input("Please choose language: PL or EN / Wybierz język: PL lub EN: ").upper()

    if lang == "EN":
        functions.english()

    if lang == "PL":
        functions.polski()

    if lang != "PL" and lang != "EN":
        print("!!! Unknown language. / Nieznany język. !!!\n")
        choose_language()

choose_language()
