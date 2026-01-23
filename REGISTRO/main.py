import sys
import uuid
from typing import List, Optional
from models import Corso, Partecipante
from data_manager import DataManager

class GestorePresenze:
    def __init__(self):
        self.corsi: List[Corso] = []
        self.partecipanti: List[Partecipante] = []
        self.filename = "dati_presenze.json"
        
    def avvia(self):
        self.corsi, self.partecipanti = DataManager.carica_dati(self.filename)
        print("Dati caricati correttamente.")
        
        while True:
            self.mostra_menu()
            scelta = input("Seleziona un'opzione: ").strip()
            
            if scelta == "1":
                self.aggiungi_corso()
            elif scelta == "2":
                self.aggiungi_partecipante()
            elif scelta == "3":
                self.iscrivi_partecipante()
            elif scelta == "4":
                self.registra_presenze()
            elif scelta == "5":
                self.report_assenze()
            elif scelta == "6":
                self.salva_ed_esci()
                break
            else:
                print("Opzione non valida, riprova.")

    def mostra_menu(self):
        print("\n--- GESTIONE PRESENZE ---")
        print("1. Aggiungi Corso")
        print("2. Aggiungi Partecipante")
        print("3. Iscrivi Partecipante a Corso")
        print("4. Registra Presenze")
        print("5. Report Assenze")
        print("6. Salva ed Esci")

    def aggiungi_corso(self):
        print("\n[NUOVO CORSO]")
        nome = input("Nome Corso: ").strip()
        # id_corso = input("ID Corso: ").strip() # REMOVED
        id_corso = str(uuid.uuid4())
        print(f"ID Corso generato: {id_corso}")
        
        # Check superfluo se usiamo UUID, ma lo teniamo per robustezza
        if any(c.id == id_corso for c in self.corsi):
            print("Errore: UUID collision (davvero sfortunato). Riprova.")
            return

        try:
            ore = int(input("Ore Totali: ").strip())
        except ValueError:
            print("Errore: Le ore devono essere un numero intero.")
            return
            
        corso = Corso(nome, id_corso, ore)
        self.corsi.append(corso)
        self.salvataggio_automatico()
        print(f"Corso '{nome}' aggiunto con successo.")

    def aggiungi_partecipante(self):
        print("\n[NUOVO PARTECIPANTE]")
        nome = input("Nome: ").strip()
        cognome = input("Cognome: ").strip()
        # matricola = input("Matricola: ").strip() # REMOVED
        matricola = str(uuid.uuid4())
        print(f"Matricola generata (UUID): {matricola}")
        
        if any(p.matricola == matricola for p in self.partecipanti):
            print("Errore: UUID collision (davvero sfortunato).")
            return
            
        partecipante = Partecipante(nome, cognome, matricola)
        self.partecipanti.append(partecipante)
        self.salvataggio_automatico()
        print(f"Partecipante {nome} {cognome} aggiunto.")

    def iscrivi_partecipante(self):
        print("\n[ISCRIZIONE CORSO]")
        corso = self.seleziona_corso()
        if not corso:
            return
            
        partecipante = self.seleziona_partecipante()
        if not partecipante:
            return
            
        if corso.id in partecipante.lista_corsi:
            print("Partecipante già iscritto a questo corso.")
            return
            
        partecipante.iscrivi_corso(corso)
        self.salvataggio_automatico()
        print(f"Iscrizione completata per {partecipante.cognome} al corso {corso.nome}.")

    def registra_presenze(self):
        print("\n[REGISTRA PRESENZE]")
        corso = self.seleziona_corso()
        if not corso:
            return
            
        data = input("Inserisci data (YYYY-MM-DD): ").strip()
        # Controllo se data esiste già (avviso)
        # Controlliamo il primo partecipante per vedere se ha già un record
        if corso.lista_partecipanti:
             primo_p = corso.lista_partecipanti[0]
             # Accediamo all'oggetto presenza per questo corso
             presenza_obj = primo_p.presenze_corsi.get(corso.id)
             if presenza_obj and data in presenza_obj.get_presenze():
                 print(f"ATTENZIONE: Risultano già registrazioni per la data {data}. I dati verranno sovrascritti.")
                 confirm = input("Vuoi continuare? (s/n): ").lower()
                 if confirm != 's':
                     return

        if not corso.lista_partecipanti:
            print("Nessun partecipante iscritto a questo corso.")
            return

        print(f"\nLista Partecipanti Corso: {corso.nome}")
        for idx, p in enumerate(corso.lista_partecipanti):
            print(f"{idx + 1}. {p.cognome} {p.nome} (Matr: {p.matricola})")
            
        print("\nInserisci i numeri degli ASSENTI separati da virgola (es: 1, 3, 4).")
        print("Premi Invio senza scrivere nulla se sono tutti PRESENTI (0 Assenti).")
        print("Scrivi 'tutti' se sono tutti ASSENTI.")
        
        inp = input("Assenti: ").strip().lower()
        
        assenti_indices = set()
        if inp == 'tutti':
            assenti_indices = set(range(len(corso.lista_partecipanti)))
        elif inp:
            try:
                parts = inp.split(',')
                for part in parts:
                    val = int(part.strip()) - 1
                    if 0 <= val < len(corso.lista_partecipanti):
                        assenti_indices.add(val)
            except ValueError:
                print("Input non valido. Operazione annullata.")
                return

        count_pres = 0
        for idx, p in enumerate(corso.lista_partecipanti):
            # Se è nell'elenco assenti -> stato 0, altrimenti 1
            stato = 0 if idx in assenti_indices else 1
            try:
                p.registra_presenza(corso.id, data, stato)
                if stato == 1: count_pres += 1
            except Exception as e:
                print(f"Errore registrazione per {p.cognome}: {e}")
        
        self.salvataggio_automatico()
        print(f"Registrazione completata. {count_pres} presenti su {len(corso.lista_partecipanti)}.")

    def report_assenze(self):
        print("\n[REPORT ASSENZE]")
        print("1. Lista Generale")
        print("2. Ricerca per Matricola")
        sub = input("Scelta: ").strip()
        
        if sub == "1":
            for corso in self.corsi:
                print(f"\nCorso: {corso.nome} (Ore Tot: {corso.ore_totali})")
                if not corso.lista_partecipanti:
                    print("  - Nessun partecipante.")
                    continue
                for p in corso.lista_partecipanti:
                    self.stampa_dettaglio_studente(p, corso)
        elif sub == "2":
            matr = input("Inserisci Matricola: ").strip()
            found = False
            for p in self.partecipanti:
                if p.matricola == matr:
                    found = True
                    print(f"\nStudente: {p.cognome} {p.nome}")
                    for cid in p.lista_corsi:
                        # Trova oggetto corso
                        c_obj = next((c for c in self.corsi if c.id == cid), None)
                        if c_obj:
                            self.stampa_dettaglio_studente(p, c_obj)
            if not found:
                print("Matricola non trovata.")

    def stampa_dettaglio_studente(self, p: Partecipante, c: Corso):
        presenza_obj = p.presenze_corsi.get(c.id)
        if presenza_obj:
            ore_assenza = presenza_obj.calcola_ore_assenza()
            status = ""
            if ore_assenza > c.limite_assenze:
                status = " [RISCHIO BOCCIATURA]"
            perc = (ore_assenza / c.ore_totali) * 100 if c.ore_totali > 0 else 0
            print(f"  - {p.cognome} {p.nome}: {ore_assenza} ore assenza ({perc:.1f}%){status}")
        else:
            print(f"  - {p.cognome} {p.nome}: Dati presenza non trovati")

    def seleziona_corso(self) -> Optional[Corso]:
        if not self.corsi:
            print("Nessun corso disponibile.")
            return None
        for i, c in enumerate(self.corsi):
            print(f"{i+1}. {c.nome} (ID: {c.id})")
        try:
            sel = int(input("Seleziona Corso (numero): ").strip()) - 1
            if 0 <= sel < len(self.corsi):
                return self.corsi[sel]
        except ValueError:
            pass
        print("Selezione non valida.")
        return None

    def seleziona_partecipante(self) -> Optional[Partecipante]:
        if not self.partecipanti:
            print("Nessun partecipante disponibile.")
            return None
        # Per brevità mostro solo i primi 10 o chiedo matricola se sono tanti, 
        # ma qui mostro lista semplice come da specifica "inserimento facilitato"
        print("Lista Partecipanti:")
        for i, p in enumerate(self.partecipanti):
            print(f"{i+1}. {p.cognome} {p.nome} (Matr: {p.matricola})")
        try:
            sel = int(input("Seleziona Partecipante (numero): ").strip()) - 1
            if 0 <= sel < len(self.partecipanti):
                return self.partecipanti[sel]
        except ValueError:
            pass
        print("Selezione non valida.")
        return None

    def salvataggio_automatico(self):
        DataManager.salva_dati(self.corsi, self.partecipanti, self.filename)

    def salva_ed_esci(self):
        self.salvataggio_automatico()
        print("Arrivederci!")

if __name__ == "__main__":
    app = GestorePresenze()
    app.avvia()
