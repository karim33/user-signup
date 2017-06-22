from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True      

def is_invalid(text):

    return re.search(r"\s+", text) or re.search(r"^.{0,2}$", text) or re.search(r"^.{20,}$", text)


@app.route("/", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    vrf_password = request.form['vrf_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    vrf_password_error = ''
    email_error = ''

    if is_invalid(username):
        username_error = "That's not a valid username"
    if is_invalid(password):
        password_error = "That's not a valid password"
    if vrf_password == '':
        vrf_password_error = "That's not a valid password"
    if vrf_password != password:
        vrf_password_error = "Passwords don't match"
    if email != '' and (email.count("@") != 1 or email.count(".") != 1 or is_invalid(email)):
        email_error = "That's not a valid email"


    if not (username_error or password_error or vrf_password_error or email_error):
        return redirect('/welcome-page?username= ' + username)
    else:
        return render_template('form.html',
            username = username,
            email = email,
            username_error = username_error,
            password_error = password_error,
            vrf_password_error = vrf_password_error,
            email_error = email_error)


@app.route("/welcome-page")
def welcome():
    username = request.args.get('username')
    return render_template('welcome-page.html', username=username)


@app.route("/")
def index():
    return render_template('form.html')


app.run()
