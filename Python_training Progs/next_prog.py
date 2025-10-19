#convert string to list
from ast import While


guess_word = "pumpkin"
guess_list = list(guess_word)

input ("guess the word, enter aplhabet by alphabet: ")

false_chances = 7

while True:
    for letter in guess_list:
        user_input = input("Enter a letter: ")
        if user_input == letter:
            print("Correct!")
        else:
            print("Try again.")
            false_chances = false_chances - 1
            print(f"You have {false_chances} chances left.")    
            if false_chances == 0:
                print("Game over!")
                break
    break



