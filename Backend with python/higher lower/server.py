from flask import Flask
import random

app = Flask(__name__)


number = random.randint(1, 9)
print(number)


@app.route("/")
def home():
    return """<h1>Guess a number between 0 and 9</h1>
    <iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/animation-retro-pixel-3o7aCSPqXE5C6T8tBC">via GIPHY</a></p>

    """


@app.route("/<int:guess>")
def guess_route(guess):
    if guess < number:
        return """
            <h1 style='color:red'>Too low, Try again!</h1>
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>
        """
    elif guess > number:
        return """
            <h1 style='color:purple'>Too High, Try again!</h1>
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>
        """
    else:
        return """
            <h1>Correct!</h1>
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>
        """


if __name__ == "__main__":
    app.run(debug=True)
