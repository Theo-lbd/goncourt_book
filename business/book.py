from models.book import Book
from daos.book_daos import BookDAO

def get_all_books():
    # Crée une instance de BookDAO pour accéder aux livres
    book_dao = BookDAO()
    return book_dao.read_all()
