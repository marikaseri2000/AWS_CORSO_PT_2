from typing import List, Dict, Any

def calculate_stats(books: List[Dict[str, Any]]) -> Dict[str, Any]:
    total_books = len(books)
    by_status = {
        "todo": 0,
        "reading": 0,
        "done": 0
    }
    total_pages_read = 0
    total_rating = 0
    rated_books_count = 0
    
    for book in books:
        status = book.get("status", "todo")
        by_status[status] = by_status.get(status, 0) + 1
        
        # Calculate pages read
        if status == "done":
            total_pages_read += book.get("pages", 0)
        elif status == "reading":
            total_pages_read += book.get("current_page", 0)
            
        if status == "done" and book.get("rating"):
            total_rating += int(book.get("rating") or 0)
            rated_books_count += 1
            
    media_rating = 0.0
    if rated_books_count > 0:
        media_rating = total_rating / rated_books_count
        
    return {
        "total_books": total_books,
        "by_status": by_status,
        "total_pages_read": total_pages_read,
        "average_rating": media_rating
    }
