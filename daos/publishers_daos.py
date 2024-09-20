from daos.dao import DAO
from models.publishers import Publisher

class PublisherDAO(DAO):
    def read_all(self):
        query = "SELECT * FROM publishers"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return [Publisher(**result) for result in results]
