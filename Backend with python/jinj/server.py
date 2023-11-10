from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
date = datetime.datetime.now()
date = str(date)

year = date.split("-")[0]


@app.route("/")
def home():
    number = random.randint(1, 10)

    return render_template("index.html", rand=number, this_year=year)


@app.route("/guess/<name>")
def guess(name):
    gender_api = f"https://api.genderize.io?name={name}"
    age_api = f"https://api.agify.io?name={name}"
    gender_response = requests.get(gender_api)
    gender_response = gender_response.json()
    gender = gender_response["gender"]
    age_response = requests.get(age_api)
    age_response = age_response.json()
    age = age_response["age"]

    return render_template("guess.html", person_name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
