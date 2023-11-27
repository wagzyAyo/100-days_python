from flask import Flask, render_template
import requests

app = Flask(__name__)

end_point = "https://api.npoint.io/7b4e9e3e6a08360d6ba0"
blog_post = requests.get(end_point).json()


@app.route('/')
def home():
    return render_template('index.html', blog_post=blog_post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in blog_post:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
