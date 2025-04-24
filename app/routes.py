from flask import Blueprint, request, jsonify
from .controlles import get_all_books, create_book, update_book, delete_book

book_bp = Blueprint('books', __name__)

@book_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify(get_all_books())

@book_bp.route('/books', methods=['POST'])
def post_book():
    data = request.json
    return jsonify(create_book(data)), 201

@book_bp.route('/books/<int:book_id>', methods=['PUT'])
def put_book(book_id):
    data = request.json
    updated = update_book(book_id, data)
    if updated:
        return jsonify(updated)
    return jsonify({'error': 'Book not found'}), 404

@book_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete(book_id):
    if delete_book(book_id):
        return jsonify({'message': 'Deleted'}), 200
    return jsonify({'error': 'Book not found'}), 404
