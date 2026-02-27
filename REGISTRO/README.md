# 📋 REGISTRO - Sistema di Gestione Presenze

> Un'applicazione Python professionale nata per gestire in modo efficiente presenze, corsi e partecipanti con persistenza dei dati e architettura ad oggetti (OOP).

---

## 🚀 Panoramica del Progetto

Il progetto **REGISTRO** rappresenta l'evoluzione da un semplice script di automazione a un'applicazione strutturata e scalabile. Progettato per essere utilizzato tramite Interfaccia a Riga di Comando (**CLI**), il sistema permette di monitorare l'andamento delle presenze degli studenti in diversi corsi, segnalando tempestivamente il rischio di bocciatura in base alle assenze accumulate.

### ✨ Caratteristiche Principali

- **Architettura OOP**: Utilizzo di classi e oggetti (`Partecipante`, `Corso`, `Presenza`) per una gestione pulita e manutenibile del codice.
- **Persistenza JSON**: Tutti i dati vengono salvati in un file `dati_presenze.json`, permettendo di chiudere e riaprire l'app senza perdere le informazioni.
- **Identificatori Univoci (UUID)**: Generazione automatica di ID univoci per corsi e matricole per evitare conflitti di dati.
- **Calcolo Automatico Assenze**: Monitoraggio della percentuale di assenza rispetto al totale delle ore del corso.
- **Reportistica Dinamica**: Generazione di report generali o specifici per singolo studente.

---

## 🛠️ Struttura del Progetto

```text
REGISTRO/
├── main.py           # Entry point dell'applicazione (GestorePresenze)
├── models.py         # Definizione delle classi (Corso, Partecipante, Presenza)
├── data_manager.py   # Logica di salvataggio/caricamento JSON
├── dati_presenze.json # Storage dei dati persistenti
└── README.md         # Documentazione (questo file)
```

---

## ⌨️ Come Iniziare

### Prerequisiti
- Python 3.8 o superiore

### Installazione
1. Clona il repository.
2. Naviga nella cartella del progetto:
   ```bash
   cd REGISTRO
   ```
3. Avvia l'applicazione:
   ```bash
   python main.py
   ```

---

## 📖 Esempi di Utilizzo

### 1. Aggiungere un Corso
L'ID del corso verrà generato automaticamente tramite UUID.
```text
[NUOVO CORSO]
Nome Corso: AWS re/Start Part 2
ID Corso generato: 550e8400-e29b-41d4-a716-446655440000
Ore Totali: 100
```

### 2. Registrare le Presenze
Puoi registrare gli assenti in modo rapido inserendo solo i numeri corrispondenti nella lista.
```text
[REGISTRA PRESENZE]
Seleziona Corso: 1. AWS re/Start Part 2
Inserisci data (YYYY-MM-DD): 2026-02-27

1. Rossi Mario
2. Bianchi Luigi
3. Verdi Anna

Assenti (es: 1, 3): 1, 3
Registrazione completata. 1 presenti su 3.
```

### 3. Visualizzare il Report Assenze
Il sistema calcola la percentuale e avvisa se si supera il limite del 20% (rischio bocciatura).
```text
[REPORT ASSENZE]
Corso: AWS re/Start Part 2 (Ore Tot: 100)
  - Rossi Mario: 20 ore assenza (20.0%)
  - Bianchi Luigi: 0 ore assenza (0.0%)
  - Verdi Anna: 25 ore assenza (25.0%) [RISCHIO BOCCIATURA]
```

---

## 🤝 Contribuire
Questo progetto è stato sviluppato come parte del percorso di apprendimento **AWS re/Start**. Suggerimenti e miglioramenti sono sempre benvenuti!

---

*Made with ❤️ for coding and cloud.*
