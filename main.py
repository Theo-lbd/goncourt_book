from business.book import get_all_books

selected_books_global = []
final_books_global = []
winning_book_global = []

def display_books():    
    """
    Affiche la liste de tous les livres disponibles.
    Récupère les livres depuis la source de données et affiche leurs détails.
    """
    books = get_all_books()
    if books:
        print("Liste des livres :")
        for book in books:
            print(f"ID: {book.book_id}, Titre: {book.title}, Auteur ID: {book.author_id}, Éditeur ID: {book.publisher_id}")
    else:
        print("Aucun livre trouvé.")

def display_book_select():
    print("Options pour le public :")
    print("1 - Afficher tous les livres disponibles")
    print("2 - Afficher les 8 livres sélectionnés")
    print("3 - Afficher les 4 livres finalistes")
    print("4 - Afficher le livre gagnant")
    
    action = input("Que voulez-vous faire ? (1/2/3/4) : ")
    
    if action == '1':
        # Afficher tous les livres disponibles
        display_books()
    elif action == '2':
        # Afficher les 8 livres sélectionnés
        if selected_books_global:
            print("Voici les 8 livres sélectionnés :")
            display_books_vote(selected_books_global)
        else:
            print("Aucun livre n'a encore été sélectionné.")
    elif action == '3':
        # Afficher les 4 livres finalistes
        if final_books_global:
            print("Voici les 4 livres finalistes :")
            display_books_vote(final_books_global)
        else:
            print("Les finalistes n'ont pas encore été sélectionnés.")
    elif action == '4':
        # Afficher le livre gagnant
        if winning_book_global:
            print("Voici le livre gagnant :")
            display_books_vote(winning_book_global)
        else:
            print("Le livre gagnant n'a pas encore été sélectionné.")
    else:
        print("Choix invalide.")

def select_books(books, max_books):
    """
    Permet au jury de sélectionner un nombre spécifique de livres parmi une liste donnée.

    Args:
        books (list): Liste des livres disponibles à sélectionner.
        max_books (int): Nombre maximum de livres à sélectionner.

    Returns:
        list: Liste des livres sélectionnés.
    """
    selected_books = []
    while len(selected_books) < max_books:
        try:
            book_id = int(input(f"Entrez l'id du livre à sélectionner (max {max_books}): "))
            # trouver le livre avec id
            book = next((b for b in books if  b.book_id == book_id), None)
            if book and book_id not in [b.book_id for b in selected_books]:
                selected_books.append(book)
                print(f"Livre ajouté : {book.title}")
            elif not book:
                print("ID de livre invalide.")
            elif book_id in [b.book_id for b in selected_books]:
                print("livre déjà sélectionnés.")
            if len(selected_books) == max_books:
                print("8 livres ont été sélectionnés.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    return selected_books

def display_books_vote(selected_books):
    """
    Affiche la liste des livres sélectionnés pour le vote.

    Args:
        selected_books (list): Liste des livres sélectionnés pour le vote.
    """
    if selected_books:
        print("Livres sélectionnés pour le vote :")
        for book in selected_books:
            print(f"- {book.title}")
    else:
        print("Aucun livre sélectionné pour le vote.")

def second_vote(selected_books):
    """
    Gère la deuxième étape du vote pour sélectionner 4 livres parmi les 8 sélectionnés précédemment.

    Args:
        selected_books (list): Liste des livres sélectionnés lors du premier vote.

    Returns:
        list: Liste des 4 livres sélectionnés lors du deuxième vote.
    """
    print("\nPassons maintenant à la sélection de 4 livres parmis les 8")
    final_books = select_books(selected_books, 4)
    display_books_vote(final_books)
    return final_books

def final_vote(selected_books):
    """
    Gère la troisième étape du vote pour sélectionner le grand gagnant parmi les livres sélectionnés.

    Args:
        selected_books (list): Liste des livres sélectionnés lors du deuxième vote.

    Returns:
        list: Liste contenant le livre gagnant.
    """
    print("\nPassons maintenant à la sélection du grand gagnant")
    winning_book  = select_books(selected_books, 1)
    print("\nLe livre gagnant est :")
    display_books_vote(winning_book)
    return winning_book

def vote():
    """
    Gère les différentes étapes du processus de vote, y compris la sélection initiale, la sélection des 4 livres et la sélection du gagnant.
    """
    global selected_books_global, final_books_global, winning_book_global
    
    books = get_all_books()

    if not selected_books_global:
        # Premier vote pour sélectionner 8 livres
        selected_books_global = select_books(books, 8)
        display_books_vote(selected_books_global)
        print("Vous avez sélectionné 8 livres. Retour à l'accueil.")
    elif selected_books_global and not final_books_global:
        print("8 livres déjà sélectionnés.")
        display_books_vote(selected_books_global)
        action = input("Souhaitez-vous passer au second vote pour sélectionner 4 livres parmi les 8 ? oui(1) / non(2): ")
        if action == '1':
            final_books_global = second_vote(selected_books_global)
            print("Vous avez sélectionné 4 livres. Retour à l'accueil.")
    elif final_books_global and not winning_book_global:
        print("4 livres déjà sélectionnés.")
        display_books_vote(final_books_global)
        action = input("Souhaitez-vous voter pour le grand gagnant ? oui(1) / non(2): ")
        if action == '1':
            winning_book_global = final_vote(final_books_global)
            print("Le grand gagnant a été sélectionné ! Retour à l'accueil.")
    else:
        print("Le grand gagnant a déjà été sélectionné.")
        display_books_vote(winning_book_global)

def authenticate_jury():
    """
    Authentifie l'utilisateur comme jury en demandant un mot de passe.
    
    Returns:
        bool: True si l'authentification réussit, False sinon.
    """
    password = "123456789"
    input_password = input("Veuillez entrer le mot de passe du jury : ")

    if input_password == password:
        print("Authentification réussi.")
        return True
    else:
        print("Mot de passe incorrect. Accès refusé.")
        return False


def jury_or_public():
    """
    Gère les choix entre le jury et le public, et appelle les fonctions appropriées en fonction de ces choix.
    """
    global selected_books_global, final_books_global, winning_book_global

    choice = input("Êtes-vous le jury(1) ou le public(2) ? ")
    if choice == '1':
        if authenticate_jury():
            action = input("Voulez-vous afficher la liste des livres(1) ou passer au vote(2) ? ")
            if action == '1':
                display_books()
            elif action == '2':
                vote()
            else:
                print("Choix invalide.")
    elif choice == '2':
        display_book_select()
    else:
        print("Choix invalide.")
    
    jury_or_public()

def main():
    """
    Gère la boucle d'exécution continue de la gestion du jury ou du public.
    """
    while True:
        jury_or_public()

if __name__ == "__main__":
    main()