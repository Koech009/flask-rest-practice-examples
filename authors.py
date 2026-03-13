from flask import Flask, jsonify

app = Flask(__name__)

# Sample in-memory data
authors = [
    {"id": 1, "name": "Octavia Butler", "books": [
        {"id": 1, "title": "Kindred"},
        {"id": 2, "title": "Parable of the Sower"}
    ]},
    {"id": 2, "name": "Toni Morrison", "books": [
        {"id": 1, "title": "Beloved"},
        {"id": 2, "title": "Song of Solomon"}
    ]}
]
# route Get all authors


@app.route('/authors', methods=['GET'])
def get_authors():
    return jsonify(authors)
# route Get a single author by id


@app.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = next((a for a in authors if a['id'] == author_id), None)
    if author:
        return jsonify(author)
    else:
        return jsonify({'error': 'Author not found'}), 404
# route Get all books by a specific author


@app.route('/authors/<int:author_id>/books', methods=['GET'])
def get_author_books(author_id):
    author = next((a for a in authors if a['id'] == author_id), None)
    if author:
        return jsonify(author['books'])
    else:
        return jsonify({'error': 'Author not found'}), 404

# route Get a specific book by an author


@app.route('/authors/<int:author_id>/books/<int:book_id>', methods=['GET'])
def get_author_book(author_id, book_id):
    author = next((a for a in authors if a['id'] == author_id), None)
    if author:
        book = next((b for b in author['books'] if b['id'] == book_id), None)
        if book:
            return jsonify(book)
        else:
            return jsonify({'error': 'Book not found'}), 404
    else:
        return jsonify({'error': 'Author not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
