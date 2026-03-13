from flask import Flask, jsonify
app = Flask(__name__)

# define book class


class Book:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {'id': self.id, 'title': self.title}

# define author class


class Author:
    def __init__(self, id, name, books):
        self.id = id
        self.name = name
        self.books = books

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'books': [book.to_dict() for book in self.books]}


# Sample in-memory data
authors = [
    Author(1, "Octavia Butler", [
        Book(1, "Kindred"),
        Book(2, "Parable of the Sower")
    ]),
    Author(2, "Toni Morrison", [
        Book(3, "Beloved"),
        Book(4, "Song of Solomon")
    ])
]
# route Get all authors


@app.route('/authors', methods=['GET'])
def get_authors():
    return jsonify([author.to_dict() for author in authors])
# route Get a single author by id


@app.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = next((a for a in authors if a.id == author_id), None)
    if author:
        return jsonify(author.to_dict())
    return jsonify({'error': 'Author not found'}), 404
# route Get all books by a specific author


@app.route('/authors/<int:author_id>/books', methods=['GET'])
def get_author_books(author_id):
    author = next((a for a in authors if a.id == author_id), None)
    if author:
        return jsonify([book.to_dict() for book in author.books])
    return jsonify({'error': 'Author not found'}), 404
# route Get a specific book by an author


@app.route('/authors/<int:author_id>/books/<int:book_id>', methods=['GET'])
def get_author_book(author_id, book_id):
    author = next((a for a in authors if a.id == author_id), None)
    if author:
        book = next((b for b in author.books if b.id == book_id), None)
        if book:
            return jsonify(book.to_dict())
        return jsonify({'error': 'Book not found'}), 404
    return jsonify({'error': 'Author not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
