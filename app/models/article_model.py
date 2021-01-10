from datetime import datetime

from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    lead = db.Column(db.String(240), nullable=False)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    watched = db.Column(db.Integer, default=0)







