# def life_in_weeks(age):
#     years_remaining = 90 - age
#     days_remaining = years_remaining * 365
#     weeks_remaining = years_remaining * 52
#     months_remaining = years_remaining * 12
#     print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")


# input_age = int(input("What is your current age? "))

# life_in_weeks(input_age)

def calculate_love_score(name1, name2):

    combined_names = (name1 + name2).lower()
    true_count = sum(combined_names.count(char) for char in "true")
    love_count = sum(combined_names.count(char) for char in "love")
    love_score = int(str(true_count) + str(love_count))
    if (love_score < 10) or (love_score > 90):
        return f"Your love score is {love_score}, you go together like coke and mentos."
    elif 40 <= love_score <= 50:
        return f"Your love score is {love_score}, you are alright together."
    else:
        return f"Your love score is {love_score}."
    

name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

# get unique characters from both names
unique_chars = set(name1.lower()) | set(name2.lower())
print(f"Unique characters: {unique_chars}")

#sort unique characters
sorted_chars = sorted(unique_chars)
print(f"Sorted unique characters: {sorted_chars}")
print(f"{name1} and {name2}")

count_char1 = sum(name1.count(char) for char in "true")
count_char2 = sum(name2.count(char) for char in "true")

print(calculate_love_score(name1, name2))


    

