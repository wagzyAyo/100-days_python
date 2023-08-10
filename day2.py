bill = input(
    "Welcome ! Lets take the burden of calculating your tip of your shoulders\n How much is your bill $ ? : ")
bill_amount = int(bill)
split = input("How many people will split the bill ? ")
split = int(split)
percentage = input("What is percantage are u tipping (10 12 0r 15) ? ")
percentage = int(percentage)
total_amount = bill_amount + (bill_amount + (bill_amount * percentage / 100))
dutch_split = total_amount / split
dutch_split = float(dutch_split)
print(
    f"your total bill is {total_amount} which will be split into {split} and each person should pay {dutch_split}")
