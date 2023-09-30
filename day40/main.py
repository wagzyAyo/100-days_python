
import requests
API_USERS_SHEETY = "https://api.sheety.co/1d155e4c8874acf4ebd5da8953b622ad/flightDeals/users"

print("Welcome to Ayomide's flight club")
print("We find the best flight deals and email you.")
first_name = input("What is your first name? ")
last_name = input("What is your first name? ")
email = input("What is your email? ")
confirm_email = input("Type your email again.: ")


sheet_input = {
    "user": {
        "First Name": first_name,
        "Last Name": last_name,
        "Email": email
    }
}
if email == confirm_email:
    print("You are in the club")
    response = requests.post(url=API_USERS_SHEETY, json=sheet_input)
    print(response.text)
