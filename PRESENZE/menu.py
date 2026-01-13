class Menu:
    #non ha bisogno di un costruttore
    def printMenu(self)->None:
        print("\n--- MENU GESTIONE PRESENZE ---")
        print(f"""
              1. Crea corso
              2. Crea partecipante
              3. Aggiungi partecipante a corso
              4. Registra presenze
              5. Mostra assenze partecipante
              6. Modifica nome partecipante
              7. Exit
              """)
