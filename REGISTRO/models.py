from typing import Dict, List, Optional

class Presenza:
    def __init__(self, registro: Optional[Dict[str, int]] = None):
        # registro: Data (ISO str: YYYY-MM-DD) -> Stato (1=Presente, 0=Assente)
        self.registro: Dict[str, int] = registro if registro is not None else {}

    def aggiungi_presenza(self, data: str, stato: int):
        if stato not in [0, 1]:
            raise ValueError("Stato deve essere 0 (Assente) o 1 (Presente)")
        self.registro[data] = stato

    def get_presenze(self) -> Dict[str, int]:
        return self.registro

    def calcola_ore_assenza(self, durata_lezione: int = 1) -> int:
        # Assumiamo durata_lezione = 1 ora per semplicità se non specificato diversamente,
        # ma il requisito parla di "ore assenza". Se ogni data è una lezione,
        # e le assenze sono registrate come 0.
        # Bisogna capire se "stato 0" conta come X ore.
        # Per ora assumiamo 1 record = 1 ora o unità.
        # Se il corso ha ore totali, dobbiamo sapere quante ore vale una lezione.
        # Generalmente in questi esercizi 1 presenza/assenza = 1 ora o blocco fisso.
        assenze = 0
        for stato in self.registro.values():
            if stato == 0:
                assenze += 1
        return assenze * durata_lezione

    def to_dict(self):
        return self.registro

    @classmethod
    def from_dict(cls, data: Dict[str, int]):
        return cls(registro=data)


class Corso:
    def __init__(self, nome: str, id_corso: str, ore_totali: int):
        self.nome = nome
        self.id = id_corso
        self.ore_totali = ore_totali
        self.limite_assenze = ore_totali * 0.20
        # Lista di oggetti Partecipante
        self.lista_partecipanti: List['Partecipante'] = []

    def aggiungi_partecipante(self, partecipante: 'Partecipante'):
        # Evita duplicati
        if not any(p.matricola == partecipante.matricola for p in self.lista_partecipanti):
            self.lista_partecipanti.append(partecipante)

    def to_dict(self):
        return {
            "nome": self.nome,
            "id": self.id,
            "ore_totali": self.ore_totali,
            # Salviamo solo le matricole per evitare ricorsione infinita/duplicazione dati eccessiva
            # o possiamo salvare l'intera struttura se il DataManager lo gestisce.
            # Per semplicità, il DataManager ricostruirà le relazioni.
            "partecipanti_matricole": [p.matricola for p in self.lista_partecipanti]
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nome=data["nome"],
            id_corso=data["id"],
            ore_totali=data["ore_totali"]
        )


class Partecipante:
    def __init__(self, nome: str, cognome: str, matricola: str):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.lista_corsi: List[str] = [] # List of Course IDs
        # Mappa CourseID -> Oggetto Presenza
        self.presenze_corsi: Dict[str, Presenza] = {}

    def iscrivi_corso(self, corso: Corso):
        if corso.id not in self.lista_corsi:
            self.lista_corsi.append(corso.id)
            self.presenze_corsi[corso.id] = Presenza()
            corso.aggiungi_partecipante(self)

    def registra_presenza(self, id_corso: str, data: str, stato: int):
        if id_corso in self.presenze_corsi:
            self.presenze_corsi[id_corso].aggiungi_presenza(data, stato)
        else:
            raise ValueError(f"Partecipante non iscritto al corso {id_corso}")

    def to_dict(self):
        return {
            "nome": self.nome,
            "cognome": self.cognome,
            "matricola": self.matricola,
            "corsi": self.lista_corsi,
            "presenze": {cid: p.to_dict() for cid, p in self.presenze_corsi.items()}
        }

    @classmethod
    def from_dict(cls, data: dict):
        p = cls(
            nome=data["nome"],
            cognome=data["cognome"],
            matricola=data["matricola"]
        )
        p.lista_corsi = data.get("corsi", [])
        presenze_raw = data.get("presenze", {})
        for cid, reg in presenze_raw.items():
            p.presenze_corsi[cid] = Presenza.from_dict(reg)
        return p
