from flask import Flask,render_template,request,url_for,redirect,session
app = Flask(__name__)
app.secret_key = "somerandomfsjdfjk"
bekar = "" 
@app.route("/",method = ["GET","POST"])
def home():
    data_incoming = "" 
    if request.method == "POST"
