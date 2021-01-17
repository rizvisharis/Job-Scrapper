from flask import Flask, render_template, request, redirect

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
    if word:
        word = word.lower()
    else:
        return redirect("/")

    return render_template("report.html", searching_by = word)

app.run()