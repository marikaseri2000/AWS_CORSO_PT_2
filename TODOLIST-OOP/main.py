"""
-menu
-todolist
-project
-task
-tag
"""

class Menu:
    #non ha bisogno di un costriuttore
    def printMenu(self)->None:
        print(f"""
              1. Add Project
              2. Add Task
              3. Add Tag
              4. List Projects
              5. List Task
              6. List Tags
              7. Add id
              8. Exit
              """)

import uuid

class Project:
    def __init__(self, name: str):
        self.id=str(uuid.uuid4())
        self.name = name
        self.tasks_list=[]
    
    def get_tasks_lenght(self) -> int:
        return len(self.tasks_list)
    
    def get_project_id(self):
        return self.id
    
    def get_project_name(self) -> str:
        return self.name
    
    def set_project_name(self, new_name: str)-> None:
        self.name = new_name

class Todolist:
    def __init__(self):
        self.projects=[]

    def add_project(self, project: Project)->None:
        self.projects.append(project)
    
    def get_projects_lenght(self) -> int:
        return len(self.projects)

    def get_projects(self)-> list[Project]:
        for p in self.projects:
            return f"{p.id} {p.name}"
        
    def update_project_name(self, id: str)->None:
        target=next((project for project in self.projects if project.get_project_id()==id), None)
        target.set_project_name("pippo")
            
def main():
    todolist=Todolist()
    menu=Menu()
    while True:
        menu.printMenu()
        i= input("Seleziona l'operazione da eseguire: ")
        match i:
            case "1":
                print("*"*20)
                print("Hai scelto aggiungi progetto")
                print("*"*20)
                project_name=input("Inserisci il nome del nuovo progetto: ")
                project=Project(project_name)
                todolist.add_project(project)
                print(todolist.get_projects_lenght())
                continue
            case "2":
                print("Aggiungi task")
                continue
            case "4":
                print(todolist.get_projects())
            case "7":
                id_progetto=input("Inserisci l'id del progetto da aggiornare: ")
                print(todolist.update_project_name(id_progetto))
            case "8":
                break
            case _:
                print("Inserisci un valore corretto.")
                continue

if __name__ == "__main__":
    main()
