# from replit import clear
# from art import logo
# #HINT: You can call clear() to clear the output in the console.
# print(logo)
# clear()
# bidders = {}
# def add_bidder(name,bid):
#   bidders_name=name[bid]
#   bidders_bid=bid[name]
#   bidders[bidders_name] = bidders_bid

# add_bidder(name=input("What is your name?"),bid=input("What is your bid?"))
# print(bidders)
# def highest_bidder(bid_record):
#   highest_bid=0
#   winner=""
#   for bidder in bid_record:
#     bid_amount=bid_record[bidder]
#     if bid_amount>highest_bid:
#       highest_bid=bid_amount
#       winner=bidder

# print(input("Are there any other bidders? Type 'yes' or 'no'"))
# if input == "yes":
#   clear()
#   print(input("What is your name?"))
#   print(input("What is your bid?"))
#   add_bidder(bidders_name,bidders_bid)
# else:
#   print(f"The winner is {winner} with a bid of {bid_amount}")


from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidders = {}


def add_bidder(name, bid):
  bidders[name] = int(bid)


def highest_bidder(bid_records):
  highest_bid = 0
  winner = " "
  for bidder in bid_records:
    bid_amount = bid_records[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
    return winner, highest_bid


while True:
  name = input("What is your name?")
  bid = input("What is your bid?")
  add_bidder(name, bid)
  response = input("Are there any other bidders? Types 'yes' or 'no':")
  if response.lower() != "yes":
    break
  clear()

winner, highest_bid = highest_bidder(bidders)
print(f"The winner is {winner} with a bid of {highest_bid}")
