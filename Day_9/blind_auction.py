from logo import gavel

print(gavel)

# Initializing the bid dictionary
bids = {}

#  Creating a function to collect bidder names and values and adding them to the dictionary
def bidder_information():
    name = input("What's your name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("What's your name: ").strip()

    while True:
        try:
            bet = int(input("What's your bid: $"))
            if bet <= 0:
                print("Bid must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the bid.")

    bids[name] = bet

    return bids

# Creating a function that loops through the bids dictionary and determines the winnder of the bid
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print("\nWelcome to the auction house \n")

# Creating a loop to continue as long as there are more bidders
while True:
    bidder_information()
    keep_bidding = input("Are there any other bidders? Enter Y for 'yes' or N for 'no':")
    if keep_bidding == "N":
        break
find_highest_bidder(bids)

