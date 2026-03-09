import random
number = random.randint(0, 100)
def zahlenspiel():
    number = random.randint(0, 100)
    while True:
        guess = int(input("Rate die Zahl zwischen 0 und 100: "))
        if guess == 55610:
            print("Musturius way")
            break
        elif guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        elif guess == number:
            print("That's the right number!")
            break
        else:
            print("Thats not eine Zahl zwischen 0 and 100.")
