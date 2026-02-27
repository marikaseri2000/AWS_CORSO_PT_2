# 📝 TODOLIST-OOP - Advanced Task Manager

> Un sistema di gestione attività avanzato sviluppato interamente secondo i principi della programmazione a oggetti (OOP).

---

## 🎨 Il Sistema dei Tag e delle Categorie

Questo progetto non è una semplice To-Do list. Implementa un sistema completo di catalogazione:
- **Progetti**: Raggruppa le attività per contesti specifici.
- **Categorie**: Definisce macro-aree (es. "Lavoro", "Studio") con colori associati.
- **Tag**: Etichette granulari che appartengono alle categorie, applicabili ai singoli Task per una ricerca rapida.

---

## 🚀 Caratteristiche Tecniche

- **OOP Pura**: Utilizzo di incapsulamento e relazioni complesse tra oggetti.
- **Librerie Centralizzate**: `TagLibrary` e `CategoryLibrary` per garantire l'integrità dei dati e prevenire duplicati.
- **Match-Case Logic**: Navigazione fluida nel menu CLI grazie all'uso delle feature più recenti di Python.

---

## 📂 Organizzazione Modulare

```text
TODOLIST-OOP/
├── main.py        # Logica dei menu e interazione utente
├── todolist.py    # Classe Manager principale
├── project.py     # Gestione dei progetti
├── task.py        # Definizione delle singole attività
├── tag.py         # Logica dei tag e della libreria tag
├── category.py    # Logica delle categorie
└── menu.py        # Utility di visualizzazione
```

---

## 💻 Come Usarlo

Avvia il programma e naviga tra le opzioni per creare il tuo ecosistema di produttività:
```bash
python main.py
```

1. **Crea una Categoria** (es: "Sviluppo", Colore: "Blu").
2. **Crea un Tag** associato (es: "Bug Fix").
3. **Crea un Progetto** (es: "Progetto Web").
4. **Aggiungi un Task** al progetto assegnandogli il tag creato.

---
*Progettato per dimostrare la padronanza dei concetti di software design e flussi di dati complessi.*
