from flask import render_template
from app import app


@app.get("/about")
def about():
    return render_template("about.html")