from . import db

class Diseases(db.Model):
    __tablename__ = 'threads'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    signs = db.Column(db.String())
