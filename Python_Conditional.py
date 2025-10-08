#Python Training Conditional Statements

print("welcome to the roller coaster!")

height = int(input("What is your height in cm? "))

total_bill = 0

if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        total_bill += 5
        print("You get a child ticket, that will be $5.")
    elif age <= 18:
        total_bill += 7
        print("You get a youth ticket, that will be $7.")
    else:
        total_bill += 12
        print("You get an adult ticket, that will be $12.")
    decision_pic = input("Do you want a picture taken? Y or N. ")
    if decision_pic == "Y":
        total_bill += 3
        print("Your photo will be taken. That will be an extra $3.")
    print(f"You can ride the Roller Coaster, Your total bill is ${total_bill}.")
else:
    print("Sorry, you need to be at least 120cm tall to ride.")