#generating a list of numbers from 1 to 100

import random
numbers = list(range(1, 101,2))

print(type(numbers))

sum_numbers = sum(numbers)



print(f"The sum of all the odd numbers from 1 to 100 is: {sum_numbers}")

total_sum = 0

for number in numbers:
    total_sum += number
print(f"The sum of all the numbers from 1 to 100 is: {total_sum}")

sum_numbers = 0

for number in range(1, 101, 2):
    print(number)
    sum_numbers += number

print(f"The sum of all odd numbers from 1 to 100 is: {sum_numbers}")