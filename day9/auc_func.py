from art import logo
import subprocess
import platform


def clear():
    subprocess.Popen("cls" if platform.system() ==
                     "Windows" else "clear", shell=True)


bidders = {}


def highest_bid(bidders_log):
    highest = 0
    winner = ""

    for prop_bidder in bidders_log:
        bid_amount = bidders_log[prop_bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = prop_bidder
    print(f"The highest bidder is {winner} with ${highest}")


print(logo)

new_bidders = True
while new_bidders:
    name = input("What is your name?\n")
    bid = int(input("How much do you bid?\n $"))
    bidders[name] = bid
    continuity = input("Are there any more bidders? 'yes' or 'no'\n")

    if continuity == "no":
        new_bidders = False
        highest_bid(bidders)
        print(bidders)
    else:
        clear()
