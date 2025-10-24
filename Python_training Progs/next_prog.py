#convert string to list
from ast import While
import random
import hangman_art

hangman_pics = hangman_art.HANGMANPICS
word_list = hangman_art.words


guess_word = random.choice(word_list)
guess_list = list(guess_word)

guessed_letters = ['_'] * len(guess_word)

#list to string
print(''.join(guessed_letters))

i = 0
print("guess the word, enter alphabet by alphabet: ")

false_chances = 7
print (f"your word is of length {len(guess_word)}. You have {false_chances} chances to guess wrong. Good luck!")

while True:
    while false_chances != 0 and len(guess_list) != 0:
        user_input = input("Enter a letter: ").lower()
        print("You entered:", user_input)

        if user_input in guess_list:
            print("Correct!")

            # Remove ALL occurrences of the guessed letter from guess_list
            guess_list = [ch for ch in guess_list if ch != user_input]

            # Reveal all instances in the guessed_letters display
            for idx, letter in enumerate(guess_word):
                if letter == user_input:
                    guessed_letters[idx] = user_input

            print(''.join(guessed_letters))
            if len(guess_list) == 0:
                print("🎉 Congratulations! You've guessed the word!")
                break

        else:
            print("Wrong guess.")
            false_chances -= 1
            print(hangman_pics[i])
            i += 1
            print(f"Chances left: {false_chances}")

    print("Game over!")
    print(f"The word was: {guess_word}")
    break
