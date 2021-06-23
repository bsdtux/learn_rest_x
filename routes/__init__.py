from flask import Blueprint
from flask_restx import Api

api_bp = Blueprint("api", __name__)
api = Api(api_bp, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

from routes.todo import ns as ns_todos
from routes.books import ns as ns_books
