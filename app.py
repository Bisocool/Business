from flask import Flask, render_template, request, redirect, session
from flask_session import Session

# Initializing app
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# The Portfolio Route
@app.route("/")
def index():
    return render_template("app.html")

# Was in use but now is not because it is unnecessary
@app.route("/display")
def display():
    return render_template("index2.html", name=session.get("name"))

# The signup route
# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     # Here we get the inputs from each field in the form
#     name = request.form.get("name")
#     username = request.form.get("username")
#     password = request.form.get("password")
#     # If the request.method is POST, we add the values in the form into the database and then go to the login page
#     if request.method == "POST":
#         session["name"] = request.form.get("name")
#         return redirect("/login")
#     # Else return the signup template
#     return render_template("signup.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     # Get the values from the fields in the login form
#     name = request.form.get("name")
#     password = request.form.get("password")
#     # Check if the values are in the database so we can login successfully
#     # If the number of rows meeting the condition is 1, send the user to the website.
#     else:
#       # If the login fails, stay on the login page.
#       return render_template("layout.html")


# The website route after the signin and here we intialize the name that was logged in to create a better experience.
# @app.route("/moreinfo")
# def moreinfo():
#     return render_template("app.html", name=session.get("name"))


# The route where we log out and get back to the website
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/")