from api import ma
from ..models import book_model
from marshmallow import fields


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = book_model.Book
        load_instance = True
        fields = ("titulo", "autor", "valor")

    titulo = fields.String(required=True)
    autor = fields.String(required=True)
    valor = fields.Float(required=True)
