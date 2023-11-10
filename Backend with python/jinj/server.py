from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)
date = datetime.datetime.now()
date = str(date)

year = date.split("-")[0]


@app.route("/")
def home():
    number = random.randint(1, 10)

    return render_template("index.html", rand=number, this_year=year)


if __name__ == "__main__":
    app.run(debug=True)
