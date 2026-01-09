import os 
import google.generativeai as genai
from typing import List, Dict, Any, Optional

GEMINI_API_KEY="AIzaSyBip0sH8BfBsuVkQlK2ucj_WqbI1T3xFOY"

def get_recommendations(books: List[Dict[str, Any]], genre_focus: Optional[str] = None) -> str:
    """Inizializza la libreria Gemini"""
    api_key = GEMINI_API_KEY
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set."

    genai.configure(api_key=api_key)
    
    """Inizializza il modello Gemini"""
    model = genai.GenerativeModel("gemini-3-flash-preview")
    
    """Costruisce il prompt"""
    prompt = "Consiglia dei libri basandoti sui libri che ho letto e considerando le mie valutazioni:\n"
    
    """Filtra i libri letti"""
    read_books = [b for b in books if b["status"] == "done"]
    
    """Se non ci sono libri letti e nessun genere specificato"""    
    if not read_books and not genre_focus:
        return "Non hai ancora finito nessun libro! Leggi dei libri così posso aiutarti!"
    
    """Aggiunge i libri letti al prompt"""    
    for book in read_books:
        rating_str = f"Rated: {book['rating']}/5" if book.get('rating') else "No rating"
        prompt += f"- {book['title']} by {book['author']} ({book['genre']}). {rating_str}\n"
    
    """Aggiunge il genere specificato al prompt se presente"""    
    if genre_focus:
        prompt += f"\nSuggerisci libri esclusivamente del genere '{genre_focus}'."
    else:
        prompt += "\nSuggerisci 3-5 libri che potresti apprezzare. Formattali come una lista con Titolo, Autore e una breve ragione."
        
    """Invia il prompt al modello Gemini e restituisce la risposta"""    
    try:  
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini: {str(e)}"