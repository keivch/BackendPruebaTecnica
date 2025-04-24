from .models import Book
from . import db

def get_all_books():
    return [book.to_dict() for book in Book.query.all()]

def create_book(data):
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return new_book.to_dict()

def update_book(book_id, data):
    book = Book.query.get(book_id)
    if not book:
        return None
    book.title = data['title']
    book.author = data['author']
    db.session.commit()
    return book.to_dict()

def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return False
    db.session.delete(book)
    db.session.commit()
    return True
