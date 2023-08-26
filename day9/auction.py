from art import logo
import subprocess
import platform


def clear():
    subprocess.Popen("cls" if platform.system() ==
                     "Windows" else "clear", shell=True)


highest = 0
print(logo)
bidders = {}
new_bidders = True
while new_bidders:
    name = input("What is your name?\n")
    bid = int(input("How much do you bid?\n $"))
    bidders[name] = (bid)
    continuity = input("Are there any more bidders? 'yes' or 'no'\n")

    if continuity == "no":
        new_bidders = False
        for x in bidders:
            if bid > highest:
                highest = bid
        print(f"The highest bidder is {name} with {highest}")

