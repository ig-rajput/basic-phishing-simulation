from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = "demo_submissions.txt"


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return render_template(
            "result.html",
            message="Please enter all fields."
        )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    with open(LOG_FILE,"a") as file:
        file.write(
            f"{timestamp} | Demo Input Received From: {username}\n"
        )


    return render_template(
        "result.html",
        message="""
This was a phishing awareness simulation.

In a real phishing attack, credentials entered here could be stolen.

Always verify URLs before logging in.
"""
    )


if __name__ == "__main__":

    if not os.path.exists(LOG_FILE):
        open(LOG_FILE,"w").close()

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=False
    )