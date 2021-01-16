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
    word = request.args.get('word', '')
    return render_template("report.html", searching_by = word)

app.run()