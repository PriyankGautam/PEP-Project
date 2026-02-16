from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    
    return redirect(url_for("success",name=name))

@app.route("/success")
def success():
    name = request.args.get("name","Guest")
    return render_template("success.html",name=name)

if __name__ == "__main__":
    app.run(debug=True)
