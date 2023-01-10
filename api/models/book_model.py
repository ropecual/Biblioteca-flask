from api import db


class Book(db.Model):
    __tablename__ = "book"

    isbn = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
