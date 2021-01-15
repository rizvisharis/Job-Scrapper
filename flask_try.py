from flask import Flask, render_template

app = Flask("SuperScarpper")

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/contact")
def contact():
    return "Contact me!"

app.run(host = "0.0.0.0")