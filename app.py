from flask import Flask, render_template
from database import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to CareRoster - NDIS Roster Management System"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/participants")
def participants():
    conn = get_db_connection()
    participants = conn.execute("SELECT * FROM participants").fetchall()
    conn.close()
    return render_template("participants.html", participants=participants)

if __name__ == "__main__":
    app.run(debug=True)
