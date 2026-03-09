import hypertyper
import ratetzahlenratespiel
import ratetzahlespiel
import zahlenratespiel
import vocabulary_learn

selection = int(input("Welcome to the game menu! Please select a game or tool: \n1 = Hypertyper\n2 = Ratetzahlenratespiel\n3 = Ratetzahlespiel\n4 = Zahlenratespiel\n5 = Flashcards\n"))
if selection == 1:
    hypertyper.hypertyper()
elif selection == 2:
    ratetzahlenratespiel.ratetzahlenratespiel()
elif selection == 3:
    ratetzahlespiel.raten()
elif selection == 4:
    zahlenratespiel.zahlenspiel()

    