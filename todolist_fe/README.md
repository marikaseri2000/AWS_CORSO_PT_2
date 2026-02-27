# 🌐 To-Do List API Client

> Un client leggero in Python per interrogare le API di gestione task, dimostrando l'integrazione tra sistemi diversi.

---

## 💡 Panoramica

Questo progetto funge da ponte tra una CLI locale e un server backend (Django/FastAPI). Utilizza la libreria `requests` per effettuare chiamate HTTP e manipolare i dati ricevuti in formato JSON.

---

## 🛠️ Funzionalità

- **Fetch Progetti**: Recupera la lista completa dei progetti dal server remoto.
- **Filtro Task**: Interroga il backend per ottenere le task associate a uno specifico ID progetto.
- **JSON Parsing**: Manipolazione efficiente degli endpoint API.

---

## 🚀 Come Eseguirlo

Assicurati che il server backend sia attivo all'indirizzo `http://127.0.0.1:8000`.

1. Installa i requisiti:
   ```bash
   pip install requests
   ```
2. Esegui lo script:
   ```bash
   python main.py
   ```

---
*Progetto focalizzato sulle competenze di integrazione API e comunicazione client-server.*
