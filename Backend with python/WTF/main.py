from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import data_required


app = Flask(__name__)
app.secret_key = 'app key'


class Register(FlaskForm):
    email = StringField(label='email', validators=[data_required()])
    password = PasswordField(label='password', validators=[data_required()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form = Register()
    return render_template('login.html', login_form=form)


if __name__ == '__main__':
    app.run(debug=True)
