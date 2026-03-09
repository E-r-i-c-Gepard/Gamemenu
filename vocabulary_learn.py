import json
import random
from pathlib import Path
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
    word = input("Enter the word you want to learn: ")
    translation = input("Enter the translation of the word: ")
    vocab[word] = translation
    save_vocabulary(vocab)
    print(f"Added '{word}' with translation '{translation}' to your vocabulary.")
def quiz(vocab):
    if not vocab:
        print("Your vocabulary is empty. Please add some words first.")
        return
    word, translation = random.choice(list(vocab.items()))
    answer = input(f"What is the translation of '{word}'? ")
    if answer.strip().lower() == translation.strip().lower():
        print("Correct! Well done!")
    else:
        print(f"Wrong! The correct translation is '{translation}'.")
while True:
    vocab = load_vocabulary()
    choice = input("Do you want to add a word (a), take a quiz (q), or exit (exit)? (a/q/exit): ")
    if choice.lower() == 'a':
        add_word(vocab)
    elif choice.lower() == 'q':
        quiz(vocab)
    elif choice.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'a' to add a word, 'q' to take a quiz, or 'exit' to quit.")
# nice