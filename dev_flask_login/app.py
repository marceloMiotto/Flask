from flask import Flask, session, render_template, flash, request, redirect, url_for
from os import urandom
from flask_login import LoginManager

app = Flask(__name__)
SECRET_KEY = urandom(24)
app.secret_key = SECRET_KEY
login_manager = LoginManager()

login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    """form = LoginForm()
    if form.validate_on_submit():

        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')

        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    """

    # return render_template('login.html', form=form)
    if request.method == "POST":
        flash('Logged in successfully.')
        return redirect(url_for('home'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
