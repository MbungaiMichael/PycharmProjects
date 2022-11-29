# this code is a blind auction using dictionaries
print("Welcome to our blind auction the artefacts wil be revealed shortly")


def highest_bid(bidding_record):
    highest = 0
    winner = ''
    for key in bidding_record:
        highest_bidder = bidding_record[key]
        if highest_bidder > highest:
            highest = highest_bidder
            winner = key
    print(f"The highest bid is {winner} with a price of ${highest}")


bid = True
while bid:
    name = input("what is your name ?: ").upper()
    bid_price = int(input("what is your bidding price? :$"))
    bidding_dic = {}
    bidding_dic[name] = bid_price
    quest = input("is there any other user who wants to bid?,'yes' or 'no': ").lower()
    if quest == 'no':
        bid = False
        highest_bid(bidding_dic)
