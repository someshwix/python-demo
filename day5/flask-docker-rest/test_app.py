import unittest
import json
from app import app, books

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'VLib - Online Library', result.data)

    def test_get_all_books(self):
        result = self.app.get('/api/v1/books/all')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Eloquent JavaScript, Third Edition', result.data)

    def test_get_book_by_id(self):
        result = self.app.get('/api/v1/books?id=1')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Eloquent JavaScript, Third Edition', result.data)

    def test_get_book_by_id_not_found(self):
        result = self.app.get('/api/v1/books?id=100')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b'[]')

    def test_get_book_by_id_no_id(self):
        result = self.app.get('/api/v1/books')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Error: No id field provided. Please specify an id.', result.data)

    def test_add_book(self):
        new_book = {
            "id": 9,
            "isbn": "9781449331819",
            "title": "New Book",
            "subtitle": "A New Book Subtitle",
            "author": "New Author",
            "published": "2023-10-10T00:00:00.000Z",
            "publisher": "New Publisher",
            "pages": 123,
            "description": "A new book description.",
            "website": "http://newbook.com/"
        }
        result = self.app.post('/api/v1/books', data=json.dumps(new_book), content_type='application/json')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Success: Book information has been added.', result.data)
        self.assertIn(new_book, books)

    def test_delete_book(self):
        result = self.app.delete('/api/v1/books/1')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Success: Book information has been deleted.', result.data)
        self.assertNotIn(next((book for book in books if book["id"] == 1), None), books)

if __name__ == '__main__':
    unittest.main()