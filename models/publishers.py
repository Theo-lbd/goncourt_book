class Publisher:
    def __init__(self, publisher_id, name):
        self.publisher_id = publisher_id
        self.name = name
    
    def __repr__(self):
        return f"Publisher({self.name})"
