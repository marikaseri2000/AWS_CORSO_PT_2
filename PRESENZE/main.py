from menu import Menu

def main():
    corsi = []
    partecipanti = []
    menu=Menu()

    while True:
        
        menu.printMenu()
        scelta= input("Seleziona l'operazione da eseguire: ")

        # -------------------------
        if scelta == "1":
            nome = input("Nome corso: ")
            corso = Corso(nome)
            corsi.append(corso)
            print("Corso creato con ID:", corso.mostra_id())

        # -------------------------
        elif scelta == "2":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            p = Partecipante(nome, cognome)
            partecipanti.append(p)
            print("Partecipante creato. Matricola:", p.mostra_matricola())

        # -------------------------
        elif scelta == "3":
            for i, c in enumerate(corsi):
                print(i, c.mostra_nome())
            idx = int(input("Seleziona corso: "))

            for p in partecipanti:
                print(p.mostra_nome_cognome(), "-", p.mostra_matricola())
            mat = input("Matricola partecipante: ")

            partecipante = trova_partecipante(mat, partecipanti)
            if partecipante:
                corsi[idx].aggiungi_partecipante(partecipante)
                print("Partecipante aggiunto al corso")
            else:
                print("Matricola non trovata")

        # -------------------------
        elif scelta == "4":
            for i, c in enumerate(corsi):
                print(i, c.mostra_nome())
            idx = int(input("Seleziona corso: "))

            presenza = Presenza(corsi[idx].mostra_nome())

            for p in corsi[idx].partecipanti:
                risp = input(f"{p.mostra_nome_cognome()} presente? (s/n): ")
                presente = risp.lower() == "s"
                presenza.registra_presenza(p, presente)

            print("Presenze registrate")

        # -------------------------
        elif scelta == "5":
            for p in partecipanti:
                print(p.mostra_nome_cognome(), "-", p.mostra_matricola())
            mat = input("Inserisci matricola: ")
            p = trova_partecipante(mat, partecipanti)
            if p:
                print("Assenze totali:", p.mostra_assenze_tot())
                print("Assenze %:", round(p.mostra_assenze_percentuale(), 2))
            else:
                print("Partecipante non trovato")

        # -------------------------
        elif scelta == "6":
            mat = input("Inserisci matricola: ")
            p = trova_partecipante(mat, partecipanti)
            if p:
                nuovo_nome = input("Nuovo nome: ")
                nuovo_cognome = input("Nuovo cognome: ")
                p.modifica_nome_cognome(nuovo_nome, nuovo_cognome)
                print("Dati aggiornati")
            else:
                print("Matricola non trovata")

        # -------------------------
        elif scelta == "0":
            print("Uscita dal programma")
            break

        else:
            print("Scelta non valida")


# AVVIO PROGRAMMA
if __name__ == "__main__":
    main()