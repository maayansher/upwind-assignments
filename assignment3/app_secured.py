from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Connect to the database
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # SECURE query using parameterized statement
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        print("Executing query:", query, "with params:", username, password)  # debug print

        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            message = "Login successful!"
        else:
            message = "Login failed. Invalid details."

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
