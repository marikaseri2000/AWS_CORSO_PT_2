# ☁️ ATTA - AWS Automation Toolkit

> Uno strumento di automazione per AWS progettato per semplificare le operazioni cloud tramite un'interfaccia a riga di comando intuitiva.

---

## 🛠️ Funzionalità

- **Configurazione Centralizzata**: Gestione sicura delle credenziali e dei parametri tramite file `.env`.
- **Interfaccia Modulare**: Struttura basata su menu per navigare facilmente tra le diverse utility di automazione.
- **Scalabilità**: Architettura package-based (`atta.ui`, `atta.logic`) per una facile estensione delle funzionalità.

---

## 📂 Struttura del Pacchetto

```text
ATTA/
├── main.py            # Entry point dell'automazione
├── atta/              # Core logic dell'applicazione
│   ├── ui/            # Gestione dei menu CLI
│   └── ...            # Moduli funzionali (AWS interaction)
├── scripts/           # Utility script aggiuntivi
├── tests/             # Suite di test unitari e d'integrazione
└── .env.example       # Template per le variabili d'ambiente
```

---

## ⚙️ Configurazione

1. Copia il file di esempio per le variabili d'ambiente:
   ```bash
   cp .env.example .env
   ```
2. Inserisci le tue credenziali AWS e le configurazioni necessarie nel file `.env`.
3. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
4. Avvia l'applicazione:
   ```bash
   python main.py
   ```

---

*Questo toolkit è stato sviluppato per ottimizzare i workflow cloud durante il percorso AWS re/Start.*
