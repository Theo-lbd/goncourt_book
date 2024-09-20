from daos.dao import DAO
from models.authors import Author

class AuthorDAO(DAO):
    def read_all(self):
        query = "SELECT * FROM authors"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return [Author(**result) for result in results]
