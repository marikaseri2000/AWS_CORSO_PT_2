from utils import print_error, print_success, print_info
from ai import get_recommendations
from stats import calculate_stats
from books import add_book, update_book_status, delete_book, get_all_books

def cmd_add(args):
    
    """Aggiunge un nuovo libro."""
    if args["pages"] <= 0:
        print_error("Le pagine devono essere maggiori di 0")
        return

    book = add_book(args["title"], args["author"], args["genre"], args["pages"])
    print_success(f"Libro aggiunto: '{book['title']}' (ID: {book['id'][:8]})")

def cmd_list(args=None):
    """Mostra tutti i libri."""
    all_books = get_all_books()

    if not all_books:
        print_info("Nessun libro presente. Usa 'add' per iniziare.")
        return

    print("\n📚 LIBRERIA\n")

    for book in all_books:
        status = {
            "todo": "📋 Da leggere",
            "reading": "📖 In lettura",
            "done": "✅ Completato"
        }.get(book["status"], book["status"])

        current = book.get("current_page", 0)
        pages = book["pages"]
        pct = int((current / pages) * 100) if pages > 0 else 0

        rating = f"⭐ {book['rating']}/5" if book.get("rating") else "⭐ N/A"

        print(f"ID: {book['id'][:8]}")
        print(f"Titolo: {book['title']}")
        print(f"Autore: {book['author']}")
        print(f"Stato: {status}")
        print(f"Progresso: {current}/{pages} ({pct}%)")
        print(f"Rating: {rating}")
        print("-" * 30)

def cmd_update(args):
    """Aggiorna stato, progresso o rating di un libro."""
    all_books = get_all_books()
    target = None

    for b in all_books:
        if b["id"].startswith(args["book_id_prefix"]):
            target = b
            break

    if not target:
        print_error("Libro non trovato")
        return

    status = args["status"]
    page = args["page"]
    rating = args["rating"]

    if status == "reading" and page is None:
        try:
            page = int(input(f"Pagina corrente (0-{target['pages']}): "))
        except ValueError:
            print_error("Numero di pagina non valido")
            return

    if page is not None and (page < 0 or page > target["pages"]):
        print_error("Pagina fuori range")
        return

    if status == "done" and rating is None:
        try:
            rating = int(input("Valutazione (1-5): "))
        except ValueError:
            print_error("Valutazione non valida")
            return

    if rating is not None and (rating < 1 or rating > 5):
        print_error("La valutazione deve essere tra 1 e 5")
        return

    updated = update_book_status(target["id"], status, page, rating)
    if updated:
        print_success(f"Libro aggiornato: {updated['title']}")
    else:
        print_error("Aggiornamento fallito")

def cmd_delete(args):
    """Elimina un libro."""
    all_books = get_all_books()
    target = None

    for b in all_books:
        if b["id"].startswith(args["book_id_prefix"]):
            target = b
            break

    if not target:
        print_error("Libro non trovato")
        return

    confirm = input(f"Eliminare '{target['title']}'? (y/n): ")
    if confirm.lower() == "y":
        if delete_book(target["id"]):
            print_success("Libro eliminato")
        else:
            print_error("Errore durante l'eliminazione")

def cmd_stats(args):
    """Mostra statistiche della libreria."""
    all_books = get_all_books()
    data = calculate_stats(all_books)

    print("\n📊 STATISTICHE\n")
    print(f"📚 Totale libri: {data['total_books']}")
    print(
        f"📋 Da leggere: {data['by_status']['todo']} | "
        f"📖 In lettura: {data['by_status']['reading']} | "
        f"✅ Completati: {data['by_status']['done']}"
    )
    print(f"📄 Pagine lette: {data['total_pages_read']}")
    print(f"⭐ Rating medio: {data['average_rating']:.1f}/5")

def cmd_suggest(args):
    """Suggerimenti AI."""
    all_books = get_all_books()

    if not all_books:
        print_info("Nessun libro disponibile per i suggerimenti.")
        return

    print_info("Sto chiedendo suggerimenti a Gemini...")
    recommendation = get_recommendations(all_books, args["genre"])

    print("\n🤖 SUGGERIMENTI AI\n")
    print(recommendation)

def input_add_book():
    """Chiede all'utente i dati per aggiungere un libro."""
    try:
        title = input("Titolo: ")
        author = input("Autore: ")
        genre = input("Genere: ")
        pages = int(input("Pagine: "))
    except ValueError:
        print("❌ Le pagine devono essere un numero")
        return None
    
    return{
        "title": title,
        "author": author,
        "genre": genre,
        "pages": pages
    }

def input_update_book():
    """Chiede all'utente ID, stato e opzionali page/rating."""
    book_data = {
        "book_id_prefix": input("ID libro (inizio): "),
        "status": input("Stato (todo/reading/done): "),
        "page": None,
        "rating": None
    }
    return book_data

def input_delete_book():
    """Chiede all'utente ID del libro da eliminare."""
    book_data = {
        "book_id_prefix": input("ID libro (inizio): ")
    }
    return book_data

def input_suggest_genre():
    """Chiede all'utente genere per i suggerimenti."""
    genre = input("Genere (invio per nessuno): ")
    return {"genre": genre if genre else None}