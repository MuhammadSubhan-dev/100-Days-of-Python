import art
print(art.logo)

secret_auction = {}     #{name: price}

highest_bid = 0
highest_bidder = ""
more_bids = True
while more_bids == True:
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    secret_auction[name] = bid

    if more_bidders == "no":
        more_bids = False
        for bidder in secret_auction:
            if secret_auction[bidder] > highest_bid:
                highest_bid = secret_auction[bidder]
                highest_bidder = bidder
    else:
        print("\n"*20)      #Clears the screen for new bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")