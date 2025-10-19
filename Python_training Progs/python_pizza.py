#pizza shop program

size = input("What size pizza do you want? S, M, or L ")

bill = 0

if size == "S" or size == "s":
    bill += 15
    print(f"Small pizza selected, ${bill}")
elif size == "M" or size == "m":
    bill += 20
    print(f"Medium pizza selected, ${bill}")
elif size == "L" or size == "l":
    bill += 25
    print(f"Large pizza selected, ${bill}")

    add_pepperoni = input("Do you want pepperoni? Y or N ")

    if add_pepperoni == "Y" or add_pepperoni == "y":
        if size == "S" or size == "s":
            bill += 2
            print(f"Pepperoni added to small pizza $2")
        else:
            bill += 3
            print(f"Pepperoni added to medium/large pizza $3")

    extra_cheese = input("Do you want extra cheese? Y or N ")

    if extra_cheese == "Y" or extra_cheese == "y":
        bill += 1
        print(f"Extra cheese added $1")

    print(f"Your final bill is: ${bill}.")

else:   
    print("No pizza selected.")

