
import datetime

from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    now =datetime.datetime.now()
    new_year = now.month ==1 and now.day==1
    m=(11-now.month)
    d=(31-now.day)
    return render_template('hi.html', new_year=new_year, m=m, d=d)
