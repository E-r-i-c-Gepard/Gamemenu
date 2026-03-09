import time as timo
import colorama
import random
from pathlib import Path
def hypertyper():
    script_dir = Path(__file__).resolve().parent
    wordlist_path = script_dir / "wordlist.txt"

    try:
        with open(wordlist_path, "r", encoding="utf-8") as file:
            words = [w for w in file.read().splitlines() if w.strip()]
    except FileNotFoundError:
        print(f"wordlist.txt not found at {wordlist_path}")
        return

    if not words:
        print(f"wordlist.txt at {wordlist_path} contains no words")
        return

    # load highscore early so it's available even if the player fails
    try:
        with open("highscore.txt", "r") as f:
            highscore = f.read().strip()
    except FileNotFoundError:
        highscore = ""
    try:
        highscore_val = float(highscore)
    except ValueError:
        highscore_val = float("inf")

    random_word = random.choice(words)
    timer = 3
    first_user_input = input("This game is about writing a word as fast as possible. Write " + colorama.Fore.LIGHTBLUE_EX + "reset highscore" + colorama.Fore.WHITE + " or press Enter to start. ")

    if first_user_input.lower() == "reset highscore":
        with open("highscore.txt", "w") as file:
            file.write("")
        print("Highscore reset.")
        return

    for i in range(3):
        print(timer)
        timo.sleep(1)
        timer -= 1
    print("Go!")
    timo.sleep(1)
    start = timo.time()
    user_input = input("Write the word " + colorama.Fore.YELLOW + random_word + colorama.Fore.WHITE + " as fast as possible: ")
    if user_input == random_word:
        end = timo.time()
        time_elapsed = end - start
        time_elapsed = round(time_elapsed, 2 )
        print("Time elapsed: " + colorama.Fore.CYAN + f"{time_elapsed} seconds" + colorama.Fore.WHITE)
        if time_elapsed < highscore_val:
            print(colorama.Fore.GREEN + "Congratulations! You set a new highscore!" + colorama.Fore.WHITE)
            with open("highscore.txt", "w") as file:
                file.write(str(time_elapsed))
            highscore_val = time_elapsed

    else:
        print("That's not the word you were supposed to write dumbass.")
        
    display = "N/A" if highscore_val == float("inf") else str(highscore_val)
    print("Highscore: " + colorama.Fore.RED + display + colorama.Fore.WHITE)
hypertyper()