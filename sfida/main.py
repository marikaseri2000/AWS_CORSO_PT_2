from books import get_all_books
from cmd import cmd_list, cmd_add, input_suggest_genre, input_delete_book, input_update_book, input_add_book, cmd_suggest, cmd_stats, cmd_delete, cmd_update

def main():
    while True:
        print("\n📚 BOOK MANAGER")
        print("1) Aggiungi un libro")
        print("2) Lista di tutti i libri")
        print("3) Aggiorna un libro")
        print("4) Elimina un libro")
        print("5) Statistiche")
        print("6) Suggerimenti AI")
        print("0) Esci")

        choice = input("Scelta della lista: ").strip()

        if choice == "1":
            book_data = input_add_book()
            if book_data:
                cmd_add(book_data)

        elif choice == "2":
            cmd_list()

        elif choice == "3":
            book_data = input_update_book()
            cmd_update(book_data)
        elif choice == "4":
            book_data = input_delete_book()
            cmd_delete(book_data)
        elif choice == "5":
            all_books = get_all_books()
            cmd_stats(all_books)
        elif choice == "6":
            genre_data = input_suggest_genre()
            cmd_suggest(genre_data)
        elif choice == "0":
            print("👋 Ciao!")
            break

        else:
            print("❌ Scelta non valida")

if __name__ == "__main__":
    main()
