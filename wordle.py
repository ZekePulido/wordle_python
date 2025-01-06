from collections import Counter

def instructions():
    print("""
    You have six guesses to successfully guess a five-letter word
    "✅" Indicates the letter is correct and in the right position
    "➕" Indicates the letter is correct but in the wrong position
    "❌" Indicates the letter is completely wrong
    """)

def check_word():
    hidden_word = "snail"
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

            result = [""] * length
            for i in range(length):
                if guess[i] == hidden_word[i]:
                    result[i] = guess[i] + " ✅"
                    freq[guess[i]] -= 1

                    if freq[guess[i]] == 0:
                        del freq[guess[i]]
            
            for i in range(length):
                if result[i]:
                    continue

                current_guess = guess[i]
                if current_guess in freq and freq[current_guess] > 0:
                    result[i] = current_guess = " ➕"
                    freq[guess[i]] -= 1

                    if freq[current_guess] == 0:
                        del freq[current_guess]
                else:
                    result[i] = current_guess + " ❌"

            for mark in result:
                print(mark)

        if attempts == 0:
            print("Game Over!! The word was:", hidden_word)

instructions()
check_word()
