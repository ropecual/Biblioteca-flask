
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api

# https://www.grepper.com/tpc/flask+template+folder
# https://thinkinfi.com/flask-adding-html-and-css/
app = Flask(__name__, template_folder='../routes/templates', static_folder='../routes/static')
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
mi = Migrate(app, db)
api = Api(app)

from .models import book_model
from .views import book_view
# criar uma pasta routes e mover para la as rotas
from routes import book_routes


