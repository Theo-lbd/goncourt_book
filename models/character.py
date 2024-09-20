class Character:
    def __init__(self, character_id, name, book_id):
        self.character_id = character_id
        self.name = name
        self.book_id = book_id
    
    def __repr__(self):
        return f"Character({self.name})"
