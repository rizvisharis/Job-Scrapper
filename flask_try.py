from flask import Flask, render_template, request

app = Flask("SuperScarpper")

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/contact")
def contact():
    return "Contact me!"

@app.route("/report")
def report():
    print(request.arg.get('word'))
    # word = request.arg.get('word')
    return "hii"

app.run(host = "0.0.0.0")