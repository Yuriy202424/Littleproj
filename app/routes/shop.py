from datetime import datetime
from flask import render_template , request, redirect, url_for
from app import app
from ..db import Session, Purchase


@app.get("/shop")
def buy():
    return render_template("shop.html")


@app.post("/shop")
def get_bought():
        melons = request.form.get("melons")
        carrots = request.form.get("carrots")
        pickles = request.form.get("pickles")
        if carrots != None and melons != None and pickles != None:
            cost = int(melons) * 40 + int(carrots) * 20 + int(pickles) * 25
            date = datetime.now()
            with Session.begin() as session:
                purchases = Purchase(melons=melons, carrots=carrots, pickles=pickles, date=date, cost=cost)
                session.add(purchases)
            return redirect(url_for("result"))
        else:
            return redirect(url_for("get_bought"))
