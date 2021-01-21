from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from save import save_to_file

app = Flask("SuperScarpper")

db  ={}
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
        fromDb = db.get(word)
        if fromDb:
            jobs = fromDb
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")

    return render_template("report.html", searching_by = word, resultsNumber = len(jobs), jobs = jobs)

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")
app.run()