from daos.dao import DAO
from models.characters import Character

class CharacterDAO(DAO):
    def read_all(self):
        query = "SELECT * FROM characters"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return [Character(**result) for result in results]
