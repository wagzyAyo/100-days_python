from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def home():
    number = random.randint(1, 10)
    return render_template("index.html", rand=number)


if __name__ == "__main__":
    app.run(debug=True)
