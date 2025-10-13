#pw gen

pw_length = input ("How many character do you want your password to be? \n")

pw_schar = input ("how many special character do you want your password to be? \n")

pw_num = input ("how many numbers do you want your password to be? \n")

if int(pw_schar) + int(pw_num) > int(pw_length):
    print("Invalid input! The sum of special characters and numbers cannot exceed the total password length.")
    exit()


special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/','|','~','`']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

import random

pw_list = []

for char in range(1, int(pw_length) + 1):
    if len(pw_list) < int(pw_schar):
        pw_list.append(random.choice(special_char))
    elif len(pw_list) < int(pw_schar) + int(pw_num):
        pw_list.append(random.choice(numbers))
    else:
        pw_list.append(random.choice(letters))

random.shuffle(pw_list)

pw = ""
for char in pw_list:
    pw += char

print(f"Your password is: {pw}")


