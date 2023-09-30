
import requests
API_USERS_SHEETY = "https://api.sheety.co/1d155e4c8874acf4ebd5da8953b622ad/flightDeals/users"

print("Welcome to Ayomide's flight club")
print("We find the best flight deals and email you.")
first_name = input("What is your first name? ")
last_name = input("What is your first name? ")
email = input("What is your email? ")
confirm_email = input("Type your email again.: ")

if email == confirm_email:
    print("You are in the club")
    response = requests.post(API_USERS_SHEETY)
    print(response.status_code)
