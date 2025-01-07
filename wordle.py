from collections import Counter
import random

def instructions():
    print("""
    You have six guesses to successfully guess a five-letter word.
    Wordle-like feedback:
    🟩 = correct letter, correct position
    🟨 = correct letter, wrong position
    ⬜ = letter not in the hidden word
    """)

def new_word():
    words = [
        "apple",
        "mango",
        "lemon",
        "berry",
        "guava",
        "house",
        "quick",
        "crisp",
        "trace",
        "stare",
        "pilot",
        "fiery",
        "radar",
        "snake",
        "shark",
        "chair",
        "stone",
        "phone",
        "spoon",
        "thick"
    ]
    return random.choice(words)

def check_word():
    hidden_word = new_word()
    attempts = 6
    length = len(hidden_word)

    while attempts > 0:
        guess = input("Guess the word: ").lower()

        if len(guess) != length:
            print(f"Please enter a {length}-letter word.")
            continue

        if guess == hidden_word:
            print("You guessed the word correctly!")
            break
        else:
            attempts -= 1
            print(f"You have {attempts} attempt(s) left...")
            
            freq = Counter(hidden_word)

            result = [None] * length
            for i in range(length):
                if guess[i] == hidden_word[i]:
                    result[i] = guess[i].upper() + "🟩"
                    freq[guess[i]] -= 1
                    if freq[guess[i]] == 0:
                        del freq[guess[i]]

            for i in range(length):
                if result[i] is not None:
                    continue

                if guess[i] in freq and freq[guess[i]] > 0:
                    result[i] = guess[i].upper() + "🟨"
                    freq[guess[i]] -= 1
                    if freq[guess[i]] == 0:
                        del freq[guess[i]]
                else:
                    result[i] = guess[i].upper() + "⬜"

            print(" ".join(result))

    if attempts == 0:
        print("Game Over!! The word was:", hidden_word.upper())

instructions()
check_word()
