from models.book import Book
from daos.book_daos import BookDAO

def get_all_books():
    book_dao = BookDAO()
    return book_dao.read_all()
