# 🛒 Supermarket Manager - Esercizio Gestionale

> Un applicativo leggero e funzionale per la gestione di inventari e task operativi nel contesto di un punto vendita.

---

## 💡 Descrizione

Sviluppato come esercizio pratico per consolidare la gestione dei dati in Python, questo progetto simula un backend gestionale per un supermercato. Permette di gestire il catalogo prodotti e di associare ad ogni prodotto dei "compiti" (task) specifici, come il controllo inventario o il rifornimento.

---

## 🛠️ Funzionalità

- **Gestione Prodotti**: Aggiunta, visualizzazione e rimozione di articoli con ID univoci.
- **Task Integrati**: Possibilità di assegnare compiti specifici ad ogni prodotto.
- **Data Persistence**: Salvataggio automatico dello stato del magazzino in `supermarket_data.json`.
- **Error Handling**: Gestione degli input per evitare corruzione dei dati.

---

## 📂 Architettura

```text
esercizio8_gennaio/
├── main.py        # Interfaccia utente CLI
├── manager.py     # Logica di business per prodotti e task
├── data_handler.py # Utility per la manipolazione del file JSON
├── models.py      # Strutture dati base
└── supermarket_data.json # Database locale
```

---

## 🚀 Installazione e Avvio

```bash
cd esercizio8_gennaio
python main.py
```

---
*Esercizio focalizzato sulla manipolazione di liste, dizionari e persistenza file.*
