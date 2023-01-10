from ..models import book_model
from api import db


def cadastrar_book(book):
    book_db = book_model.Book(titulo=book.titulo, autor=book.autor, valor=book.valor)
    db.session.add(book_db)
    db.session.commit()
    return book_db


def listar_books():
    books = book_model.Book.query.all()
    return books


def listar_book_isbn(isbn):
    book_isbn = book_model.Book.query.filter_by(isbn=isbn).first()
    return book_isbn


def atualizar_book_isbn(book_anterior, book_novo):
    book_anterior.titulo = book_novo.titulo
    book_anterior.autor = book_novo.autor
    book_anterior.valor = book_novo.valor
    db.session.commit()


def remover_book(book):
    db.session.delete(book)
    db.session.commit()

