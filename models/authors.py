class Author:
    def __init__(self, author_id, name, biography):
        self.author_id = author_id
        self.name = name
        self.biography = biography
    
    def __repr__(self):
        return f"Author({self.name})"
