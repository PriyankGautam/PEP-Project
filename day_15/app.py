from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Dummy database
users = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email in users and users[email] == password:
            flash("Login Successful ✅", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid Email or Password ❌", "danger")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email in users:
            flash("User already exists ⚠️", "danger")
        else:
            users[email] = password
            flash("Registration Successful 🎉 Please Login!", "success")
            return redirect(url_for("login"))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
