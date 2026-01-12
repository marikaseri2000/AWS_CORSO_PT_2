"""

class Formina:
    def __init__(self, nome_forma: str):     #costrutto
        self.forma = nome_forma #proprietà di un oggetto 

biscotto1 = Formina("cuoricino")
biscotto2 = Formina("triangolo")

print(type(biscotto1))
print(biscotto1.forma)
print(biscotto2.forma)

"""

#classe che definisce le caratteristiche di una persona del corso AWS

class Persona:
    def __init__(self, nome: str, cognome: str, isEdgemonyPartecipant: bool):
        self.nome=nome
        self.cognome=cognome
        self.isEdgemonyPartecipant= isEdgemonyPartecipant
    
    def printisEdegemonyPartecipant(self)-> None:
        print(f"{self.nome} {self.cognome}: {self.isEdgemonyPartecipant}")

class Corso:
    def __init__(self, nome: str):
        self.nome = nome
        self.partecipants = []
    
    #inizio di interazione tra due classi
    #METODO che dovrà avere le caratteristiche specificate nella classe Persona
    def addPartecipant(self, p: Persona) -> bool:
        if p.isEdgemonyPartecipant:
            self.partecipants.append(f"{p.nome} {p.cognome}")
            return True
        else:
            return False

persona1=Persona("Claudia", "Nigno", True)
persona2=Persona("Marika", "DiBari", True)
persona3=Persona("Mario", "Rossi", False)

"""

array=[persona1, persona2, persona3]

for persona in array:
    persona.printisEdegemonyPartecipant()
    
"""

corso1=Corso("Edgemony")

plist=[persona1, persona2, persona3]
for p in plist:
    print(f"Prima: {corso1.partecipants}")
    print(corso1.addPartecipant(p))
    print(f"Dopo: {corso1.partecipants}")