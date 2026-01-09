import uuid
from datetime import datetime
from typing import List, Dict, Optional, Any
from storage import load_db, save_db

def add_book(title: str, author: str, genre: str, pages: int) -> Dict[str, Any]:
    db = load_db()
    
    new_book = {
        "id": str(uuid.uuid4()),
        "title": title,
        "author": author,
        "genre": genre,
        "pages": pages,
        "status": "todo",
        "current_page": 0,
        "rating": None,
        "added_at": datetime.now().isoformat(),
        "finished_at": None
    }
    
    db["books"].append(new_book)
    save_db(db)
    return new_book

def get_all_books() -> List[Dict[str, Any]]:
    db = load_db()
    return db.get("books", [])

def get_book_by_id(book_id: str) -> Optional[Dict[str, Any]]:
    books = get_all_books()
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def update_book_status(book_id: str, status: str, current_page: Optional[int] = None, rating: Optional[int] = None) -> Optional[Dict[str, Any]]:
    db = load_db()
    books = db.get("books", [])
    
    for book in books:
        if book["id"] == book_id:
            book["status"] = status
            
            if current_page is not None:
                book["current_page"] = current_page
                
            if status == "done":
                book["finished_at"] = datetime.now().isoformat()
                if rating is not None:
                    book["rating"] = rating
                book["current_page"] = book["pages"] # Ensure pages are maxed if done
            elif status == "reading":
                book["finished_at"] = None
                
            save_db(db)
            return book
            
    return None

def delete_book(book_id: str) -> bool:
    db = load_db()
    books = db.get("books", [])
    
    original_count = len(books)
    books = [b for b in books if b["id"] != book_id]
    
    if len(books) < original_count:
        db["books"] = books
        save_db(db)
        return True
    return False
