from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search("[@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, feedback, color


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        result = check_password(password)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)