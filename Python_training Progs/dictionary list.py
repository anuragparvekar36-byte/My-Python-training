# This is a dictionary that contains a list of fruits and their corresponding prices

fruit_prices = {
    'apple': 0.5,
    'banana': 0.3,
    'cherry': 0.8,
    'date': 1.0
}

# dictionary of items type and their corresponding list of items

shop_items = {
    'fruits' : ['apple', 'banana', 'cherry'],
    'vegetables' : ['carrot', 'broccoli', 'spinach'],
    'dairy' : ['milk', 'cheese', 'yogurt']
}

# Print the fruit prices
for fruit, price in fruit_prices.items():
    print(f"The price of {fruit} is ${price}")  

print("\nItems in the shop:")
for category, items in shop_items.items():
    print(f"{category.capitalize()}: {', '.join(items)}")

# print 2nd fruit in the fruits list
print(f"\nThe second fruit in the list is: {shop_items['fruits'][1]}")

nested_list = (('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'))

print(nested_list[1][2])  # Output: f