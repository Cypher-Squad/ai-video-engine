from flask import Flask, render_template, request, redirect, session
import sqlite3
from algorithm import recommend

app = Flask(__name__)
app.secret_key = "ai"

def get_db():
    return sqlite3.connect("database.db")

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect("/home")
    return render_template("login.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")
    rec = recommend(session["user"])
    return render_template("home.html", videos=rec)

@app.route("/watch/<category>")
def watch(category):
    db = get_db()
    user = session["user"]
    db.execute("INSERT INTO history(user,category) VALUES(?,?)",(user,category))
    db.commit()
    return redirect("/home")

app.run(debug=True)
