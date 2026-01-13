class Menu:
    #non ha bisogno di un costruttore
    def printMenu(self)->None:
        print(f"""
              1. Add Project
              2. Add Task
              3. Add Category
              4. Add Tag
              5. List Projects
              6. List Task
              7. List Categories
              8. List Tags
              9. Modifica nome progetto mediante l'id
              10. Exit
              """)
