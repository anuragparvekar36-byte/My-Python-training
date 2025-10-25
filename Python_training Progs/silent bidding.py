#silent bidding

# need to build a silent bidding system where users can place bids without seeing others' bids

bids_dict = {}

def get_bid():
    # get name
    # get bid amount
    name = input("What is your name? ")
    bid_amount = int(input("What is your bid amount? $"))
    return name, bid_amount 

def add_bid_to_dict(name, bid_amount):
    bids_dict[name] = bid_amount

# do you want to bid ? enter yes or no and continue accordingly
while True:
    name, bid_amount = get_bid()
    add_bid_to_dict(name, bid_amount)
    more_bidders = input("Are there any other bidders? Type 'y' or 'n': ").lower()
    if more_bidders == 'n':
        break

#display all the bids
print("Bids placed:")
for name, bid in bids_dict.items():
    print(f"{name}: ${bid}")

# determine the highest bid
highest_bid = 0
winner = ""
for name, bid in bids_dict.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name


print(f"The winner is {winner} with a bid of ${highest_bid}")
