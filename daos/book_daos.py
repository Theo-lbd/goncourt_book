from daos.dao import DAO
from models.book import Book

class BookDAO(DAO):
    def read_all(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        # Crée une liste d'objets Book à partir des résultats
        return [Book(**result) for result in results]
