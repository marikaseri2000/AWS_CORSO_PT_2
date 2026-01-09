import os
import google.generativeai as genai
from typing import List, Dict, Any, Optional

GEMINI_API_KEY=AIzaSyBip0sH8BfBsuVkQlK2ucj_WqbI1T3xFOY
def get_recommendations(books: List[Dict[str, Any]], genre_focus: Optional[str] = None) -> str:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set."
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    # Construct prompt
    prompt = "Consiglia dei libri basandoti sui libri che ho letto e considerando le mie valutazioni:\n"
    
    read_books = [b for b in books if b["status"] == "done"]
    if not read_books and not genre_focus:
        return "Non hai ancora finito nessun libro! Leggi dei libri così posso aiutarti!"
        
    for book in read_books:
        rating_str = f"Rated: {book['rating']}/5" if book.get('rating') else "No rating"
        prompt += f"- {book['title']} by {book['author']} ({book['genre']}). {rating_str}\n"
        
    if genre_focus:
        prompt += f"\nI am specifically looking for suggestions in the '{genre_focus}' genre."
    else:
        prompt += "\nPlease suggest 3-5 new books I might enjoy. Format them as a list with Title, Author, and a brief reason why."
        
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini: {str(e)}"
