import os
from api import app
from api.services import book_service
from api.entidades import book
from flask import render_template, redirect, request, url_for, abort, make_response
from api.views import book_view


@app.route("/", methods=["GET"])
def index():
    livros = book_service.listar_books()
    # livros = book_view.BookList.get(book.Book.self)
    return render_template("index.html", livros=livros)


@app.route('/add_book/', methods=['POST'])
def add_book():
    if not request.form:
        abort(400)
    else:
        autor_novo = request.form.get("autor")
        titulo_novo = request.form.get("titulo")
        valor_novo = request.form.get("valor")
        book_novo = book.Book(titulo=titulo_novo, autor=autor_novo, valor=valor_novo)
        resultado = book_service.cadastrar_book(book_novo)
        return redirect(url_for("index"))


@app.route('/update_book/<int:isbn>', methods=['POST'])
def update_book(isbn):
    if book_service.listar_book_isbn(isbn) is None:
        return make_response("Erro: Livro não existe", 404)
    else:
        book_anterior = book_service.listar_book_isbn(isbn)
        if request.method == "POST":
            autor_alterado = request.form['autor']
            titulo_alterado = request.form['titulo']
            valor_alterado = request.form['valor']
            book_novo = book.Book(titulo=titulo_alterado, autor=autor_alterado, valor=valor_alterado)
            book_service.atualizar_book_isbn(book_anterior, book_novo)
        return redirect(url_for("index"))


@app.route('/delete_book/<int:isbn>', methods=['GET', 'POST'])
def delete_book(isbn):
    if book_service.listar_book_isbn(isbn) is None:
        return make_response("Erro: Livro não existe", 404)
    else:
        book_deletado = book_service.listar_book_isbn(isbn)
        print(book_deletado)
        book_service.remover_book(book_deletado)
    return redirect(url_for("index"))
