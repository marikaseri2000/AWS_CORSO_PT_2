import json
import os
from typing import List, Tuple
from models import Corso, Partecipante

class DataManager:
    @staticmethod
    def salva_dati(corsi: List[Corso], partecipanti: List[Partecipante], filename: str = "dati_presenze.json"):
        data = {
            "corsi": [c.to_dict() for c in corsi],
            "partecipanti": [p.to_dict() for p in partecipanti]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Dati salvati correttamente in {filename}")

    @staticmethod
    def carica_dati(filename: str = "dati_presenze.json") -> Tuple[List[Corso], List[Partecipante]]:
        if not os.path.exists(filename):
            print(f"File {filename} non trovato. Inizio con dati vuoti.")
            return [], []

        try:
            with open(filename, 'r') as f:
                content = f.read()
                if not content.strip():
                    return [], []
                data = json.loads(content)
        except (json.JSONDecodeError, ValueError) as e:
             print(f"Errore durante la lettura del file JSON: {e}. Inizio con dati vuoti.")
             return [], []
        
        corsi = [Corso.from_dict(c) for c in data.get("corsi", [])]
        partecipanti = [Partecipante.from_dict(p) for p in data.get("partecipanti", [])]

        # Ricostruzione relazioni: Corso deve conoscere i suoi Partecipanti
        corsi_map = {c.id: c for c in corsi}
        
        for p in partecipanti:
            for corso_id in p.lista_corsi:
                if corso_id in corsi_map:
                    # Aggiungiamo il partecipante all'oggetto Corso.
                    # Nota: Il partecipante ha già l'ID nel suo elenco, quindi stiamo solo ripopolando la lista inversa.
                    corsi_map[corso_id].aggiungi_partecipante(p)
                    
        return corsi, partecipanti
