import random
import time
def ratetzahlenratespiel():
    number = random.randint(0, 100)
    a, b = 0, 101
    versuche = 0
    print("Bot 1: Ich habe mir eine Zahl zwischen 0 und 100 ausgedacht.")
    time.sleep(1)
    while True:
        c = (b - a) // 2 + a
        print(f"Bot 2: Ist die Zahl {c}?")
        time.sleep(1)
        if c < number:
            print("Bot 1: Nein, die Zahl ist größer.")
            versuche += 1
            a = c
            time.sleep(1)
        elif c > number:
            print("Bot 1: Nein, die Zahl ist kleiner.")
            versuche += 1
            b = c
            time.sleep(1)
        elif c == number:
            print(f"Bot 1: Das war richtig! Du hast {versuche} Versuche gebraucht.")
            print("Bot 2: Juhuuhuhuhuhuuu!")
            break
