# 📚 AI Book Manager - La Tua Libreria Intelligente

> Un assistente personale per la tua libreria che sfrutta l'Intelligenza Artificiale per suggerirti la prossima lettura.

---

## 🤖 AI Integration

La vera forza di questo progetto è il modulo `ai.py`, che comunica con modelli di linguaggio avanzati (Gemini) per analizzare i tuoi gusti letterari e suggerirti titoli basati su generi specifici o sulla tua storia di lettura.

---

## ✨ Caratteristiche

- **CRUD Completo**: Aggiungi, aggiorna, elenca ed elimina libri dalla tua collezione.
- **Smart Suggestions**: Ricevi consigli personalizzati direttamente nella CLI.
- **Statistiche Dinamiche**: Analizza l'andamento delle tue letture (libri letti, in lettura, da iniziare).
- **Stoccaggio JSON**: Database leggero in formato `db.json`.

---

## 📂 Struttura dei Moduli

- `main.py`: Punto di ingresso e ciclo principale.
- `cmd.py`: Parser dei comandi e interazione utente.
- `ai.py`: Interfaccia con le API di AI.
- `books.py`: Gestione degli oggetti libro.
- `storage.py`: Gestione del database JSON.
- `stats.py`: Logica di analisi dei dati.

---

## ⚙️ Configurazione

1. Crea un file `.env` partendo da `.env.example`.
2. Inserisci la tua API KEY per i servizi AI.
3. Avvia l'applicazione:
   ```bash
   python main.py
   ```

---
*Un progetto "Sfida" che unisce sviluppo backend tradizionale e integrazione AI.*
