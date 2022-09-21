

from art import logo
print(logo)

bids = {}

name = input("What is your name? ")
price = input('What is your bids? ')

bids[name] = price
bidding_finished = False


should_continue = input("Are there any other bidders? Type 'Yes' or 'No'.")
if should_continue == "no":
    bidding_finished = True

    