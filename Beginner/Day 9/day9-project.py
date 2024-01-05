import art
from os import system

print(art.logo)
print("Welcome to the secret auction program\n")
done = False
bid_log = {}

while not done:
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))

    bid_log[name] = bid

    if input("Are there any other bidders? (y/n) ").lower() == "n":
        done = True

def find_highest_bidder(bid_log):
    winning_bid = 0
    winning_bidder = ""
    for key, value in bid_log.items():
        if winning_bid < value:
            winning_bid = value
            winning_bidder = key
    print(f"The winning bid is {winning_bid}. The winning bidder is {winning_bidder}")


find_highest_bidder(bid_log)

