from flask_restful import Resource
from ..schemas import book_schema
from flask import request, make_response, jsonify
from ..entidades import book
from ..services import book_service
from api import api


class BookList(Resource):
    def get(self):
        books = book_service.listar_books()
        bs = book_schema.BookSchema(many=True)
        return make_response(bs.jsonify(books), 200)

    def post(self):
        bs = book_schema.BookSchema()
        validate = bs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            autor = request.json['autor']
            valor = request.json['valor']
            book_novo = book.Book(titulo=titulo, autor=autor, valor=valor)
            resultado = book_service.cadastrar_book(book_novo)
            return make_response(bs.jsonify(resultado), 200)


class BookDetail(Resource):
    def get(self, isbn):
        book_listar = book_service.listar_book_isbn(isbn)
        bs = book_schema.BookSchema()
        return make_response(bs.jsonify(book_listar), 200)

    def put(self, isbn):
        book_anterior = book_service.listar_book_isbn(isbn)
        bs = book_schema.BookSchema()
        validate = bs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo_novo = request.json['titulo']
            autor_novo = request.json['autor']
            valor_novo = request.json['valor']
            if book_service.listar_book_isbn(isbn) is None:
                return make_response("Erro: Livro não existe", 404)
            else:
                book_novo = book.Book(titulo=titulo_novo, autor=autor_novo, valor=valor_novo)
                book_service.atualizar_book_isbn(book_anterior, book_novo)
                book_atualizado = book_service.listar_book_isbn(isbn)

                return make_response(bs.jsonify(book_atualizado), 200)

    def delete(self, isbn):
        if book_service.listar_book_isbn(isbn) is None:
            return make_response("Erro: Livro não existe", 404)
        else:
            book_deletado = book_service.listar_book_isbn(isbn)
            book_service.remover_book(book_deletado)
            books = book_service.listar_books()
            bs = book_schema.BookSchema(many=True)
            return make_response(bs.jsonify(books), 201)


api.add_resource(BookDetail, '/books/api/<int:isbn>')
api.add_resource(BookList, '/books/api')

