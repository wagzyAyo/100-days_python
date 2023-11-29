from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import data_required, Email, Length


app = Flask(__name__)
app.secret_key = 'app key'


class Register(FlaskForm):
    email = StringField(label='email', validators=[
                        data_required(), Email(check_deliverability=True)])
    password = PasswordField(label='password', validators=[
                             data_required(), Length(min=8)])


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = Register()
    form.validate_on_submit()
    if request.method == 'POST':
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', login_form=form)


if __name__ == '__main__':
    app.run(debug=True)
