from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

username = "Shalev"
password = "123"
facebook_friends = ["Loai", "Yonathan", "Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
    if request.method == 'POST':
        name = request.form['username']
        pswrd = request.form['password']
        return render_template(url_for('home'), name=name, pswrd=pswrd)
    else:
        return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.form['username'] == username and request.form['password'] == password:
        return render_template('home.html', friends_list=facebook_friends)
    else:
        return render_template('login.html')


@app.route('/friend_exist/<string:name>', methods=['GET', 'POST'])
def friend_exist(name):
    return render_template('friend_exists.html', n=name)


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        debug=True
    )
