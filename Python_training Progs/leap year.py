def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("True")
                return True
            else:
                print("False")
                return False
        else:
            print("True")
            return True
    print("False")
    return False


print("Welcome to the Leap Year Checker!")

year = int(input("Enter a year to check if it's a leap year: "))

is_leap_year(year)

