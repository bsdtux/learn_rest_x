from flask_restx import Api, Resource, fields
from routes import api

ns = api.namespace('books', description='books operations')

book = api.model('Book', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'name': fields.String(required=True, description='The task details')
})


class BookDAO(object):
    def __init__(self):
        self.counter = 0
        self.books = []

    def get(self, id):
        for book in self.books:
            if book['id'] == id:
                return book
        api.abort(404, "Book {} doesn't exist".format(id))

    def create(self, data):
        book = data
        book['id'] = self.counter = self.counter + 1
        self.books.append(book)
        return book

    def update(self, id, data):
        book = self.get(id)
        book.update(data)
        return book

    def delete(self, id):
        todo = self.get(id)
        self.book.remove(todo)


DAO = BookDAO()
DAO.create({'name': 'Learn Python'})
DAO.create({'name': 'Learn Flask'})
DAO.create({'name': 'profit!'})


@ns.route('/')
class BookList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_books')
    @ns.marshal_list_with(book)
    def get(self):
        '''List all tasks'''
        return DAO.books

    @ns.doc('create_book')
    @ns.expect(book)
    @ns.marshal_with(book, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Book not found')
@ns.param('id', 'The book identifier')
class Book(Resource):
    '''Show a single book item and lets you delete them'''
    @ns.doc('get_book')
    @ns.marshal_with(book)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_book')
    @ns.response(204, 'book deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(book)
    @ns.marshal_with(book)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)
