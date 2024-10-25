from flask import render_template
from sqlalchemy import select
from app import app
from ..db import Session, Purchase, User


@app.get("/result")
def result():
    with Session.begin() as session:
        purchases = session.execute(select(Purchase.carrots, Purchase.melons, Purchase.pickles, Purchase.cost, Purchase.date)).all()
    namings = ["carrots", "melons", "pickles", "cost", "date"]
    packed = []
    for p in purchases:
        item = {}
        for i in range(len(namings)):
            item[namings[i]] = p[i]
        packed.append(item)
    return render_template("result.html", packed=packed)
    