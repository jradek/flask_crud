from flask import render_template, url_for
from dummyapp import app_obj


@app_obj.route("/")
def index():
    return render_template("index.html")


@app_obj.route("/documentation")
def documentation():
    return render_template("documentation.html")
