# Blind Auction Program
# Secret bidding with automatic winner detection
# Author: yoan9601

from art import logo
import os

print(logo)
print("Welcome to the Secret Auction Program!\n")

bids = {}
bidding_finished = False


def find_winner(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}!\n")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        bidding_finished = True
        find_winner(bids)
    elif should_continue == "yes":
        os.system('clear' if os.name == 'posix' else 'cls')  # Works Windows + Mac + Linux
