import random
import string

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/','|','~','`']

while True:
    try:
        pw_length = int(input("How many characters do you want your password to be? \n"))
        pw_spchar = int(input("How many special characters do you want your password to be? \n"))
        if pw_length <= 0 or pw_spchar < 0 or pw_spchar > pw_length:
            print("Please enter valid numbers: length > 0, 0 <= special characters <= length.")
            continue
        break
    except ValueError:
        print("Please enter valid integers.")

pw_list = []
for length in range(1, int(pw_length)+1):
    if len(pw_list) < int(pw_spchar):
        pw_list.append(random.choice(special_char))
    else:
        pw_list.append(random.choice(string.ascii_letters + string.digits))

random.shuffle(pw_list)

print(pw_list)

pw = ""
for item in pw_list:
    pw += item

print(f"Your password is: {pw}")
