from flask import render_template , request, redirect, url_for, flash
from app import app 
from ..db import Nick, Session


@app.get("/")
def menu():
    return render_template('index.html')

@app.post("/")
def get_nick():
    nickname = request.form.get("nickname")
    with Session.begin() as session:
        nick = Nick(nickname=nickname)
        session.add(nick)
    if nickname:
        return redirect(url_for('buy'))
    else:
        flash("Error sigma")
        return redirect(url_for("menu"))
    
