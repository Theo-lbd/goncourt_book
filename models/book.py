class Book:
    """
    Représente un livre dans la base de données.
    
    Attributs :
    - book_id (int) : Identifiant du livre.
    - title (str) : Titre du livre.
    - summary (str) : Résumé du livre.
    - publication_date (str) : Date de publication du livre.
    - pages (int) : Nombre de pages du livre.
    - isbn (str) : Numéro ISBN du livre.
    - price (float) : Prix du livre.
    - author_id (int) : Identifiant de l'auteur du livre.
    - publisher_id (int) : Identifiant de l'éditeur du livre.
    """
    
    def __init__(self, book_id, title, summary, publication_date, pages, isbn, price, author_id, publisher_id):
        """
        Initialise un nouvel objet Book.
        
        Args :
        - book_id (int) : Identifiant du livre.
        - title (str) : Titre du livre.
        - summary (str) : Résumé du livre.
        - publication_date (str) : Date de publication du livre.
        - pages (int) : Nombre de pages du livre.
        - isbn (str) : Numéro ISBN du livre.
        - price (float) : Prix du livre.
        - author_id (int) : Identifiant de l'auteur du livre.
        - publisher_id (int) : Identifiant de l'éditeur du livre.
        """
        self.book_id = book_id
        self.title = title
        self.summary = summary
        self.publication_date = publication_date
        self.pages = pages
        self.isbn = isbn
        self.price = price
        self.author_id = author_id
        self.publisher_id = publisher_id
    
    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne du livre.
        
        Returns :
        - str : Représentation du livre.
        """
        return f"livre : {self.title}"
