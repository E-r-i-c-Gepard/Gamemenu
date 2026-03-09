import json
import random
from pathlib import Path
import colorama
path = Path(__file__).parent / "vocabulary.json"
def load_vocabulary():
    if path.exists():
        with open(path, "r") as f:
            return json.load(f)
    else:        
        return {}
    
def save_vocabulary(vocab):
    with open(path, "w") as f:
        json.dump(vocab, f, indent=2, ensure_ascii=False)
def add_word(vocab):
    word = input(colorama.Fore.GREEN + "Enter the word you want to learn: " + colorama.Style.RESET_ALL)
    translation = input(colorama.Fore.BLUE + "Enter the translation of the word: " + colorama.Style.RESET_ALL)
    vocab[word] = translation
    save_vocabulary(vocab)
    print(f"Added '{word}' with translation '{translation}' to your vocabulary.")
    continuer = input(colorama.Fore.YELLOW + "If you want to add another word, press Enter. Otherwise, type 'exit' to return to the main menu: " + colorama.Style.RESET_ALL )
    if continuer.lower() == 'exit':
        return
    if continuer == '':
        add_word(vocab)
def quiz(vocab):
    if not vocab:
        print("Your vocabulary is empty. Please add some words first.")
        return
    word, translation = random.choice(list(vocab.items()))
    answer = input(f"What is the translation of '{word}'? ")
    if answer.strip().lower() == translation.strip().lower():
        print(colorama.Fore.GREEN + "Correct! Well done!" + colorama.Style.RESET_ALL)
    else:
        print(f"Wrong! The correct translation is '{translation}'.")
    continuer = input(colorama.Fore.YELLOW + "If you want to keep doing the quiz, press Enter. Otherwise, type 'exit' to return to the main menu: " + colorama.Style.RESET_ALL)
    if continuer.lower() == 'exit':
        return
    if continuer == '':
        quiz(vocab)
def reset_vocabulary():
    if path.exists():
        path.unlink()
        print(colorama.Fore.RED + "Vocabulary has been reset." + colorama.Style.RESET_ALL)
    else:
        print(colorama.Fore.YELLOW + "No vocabulary file found to reset." + colorama.Style.RESET_ALL)
while True:
    vocab = load_vocabulary()
    choice = input(colorama.Fore.LIGHTGREEN_EX + "Do you want to add a word (a), take a quiz (q), reset the vocabulary (r), or exit (exit)? (a/q/r/exit): " + colorama.Style.RESET_ALL)
    if choice.lower() == 'a':
        add_word(vocab)
    elif choice.lower() == 'q':
        quiz(vocab)
    elif choice.lower() == 'r':
        reset_vocabulary()
    elif choice.lower() == 'exit':
        print(colorama.Fore.RED + "Exiting the program. Goodbye!" + colorama.Style.RESET_ALL)
        break
    else:
        print(colorama.Fore.RED + "Invalid choice. Please enter 'a' to add a word, 'q' to take a quiz, or 'exit' to quit." + colorama.Style.RESET_ALL)