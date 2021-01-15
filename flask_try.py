from flask import Flask

app = Flask("SuperScarpper")

@app.route("/")
def home():
    return "Hello! Welcome to Job Scrapper!"\

@app.route("/contact")
def contact():
    return "Contact me!"

app.run(host = "0.0.0.0")