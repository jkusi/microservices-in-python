from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

# Uncomment this when you have the route logic for signup and login forms
# @app.route("/signup", methods=["POST"])
# def signup_post():
#     # Handle signup form submission logic here
#     pass

# @app.route("/login", methods=["POST"])
# def login_post():
#     # Handle login form submission logic here
#     pass

# Running Flask on a different port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
