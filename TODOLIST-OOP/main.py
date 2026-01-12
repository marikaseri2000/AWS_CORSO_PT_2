from todolist import Todolist
from project import Project
from menu import Menu
from task import Task

def seleziona_project(todolist: Todolist) -> Project|None:
    #voglio aggiungerlo su un progetto specifico e quindi mi rifaccio alla lista di progetti
    todolist.get_projects()
    #uso l'id
    id_progetto=input("Inserisci l'id del progetto da aggiornare: ")
    project=todolist.get_project_by_id(id_progetto)

    if project is None:
        print("Il progetto non esiste!")
    return project

def update_project_name(todolist: Todolist):
    """Questa funzione contine il nome dei progetti a cui assegnamo i nuovi nomi"""
    print("*"*20)
    print("Aggiorna l'id di un progetto, visualizzando di seguito tutti i progetti presenti!")
    print("*"*20)
    print(todolist.get_projects())
    id_progetto=input("Inserisci l'id del progetto da aggiornare: ")
                
    while True:
        new_name=input("Inserisci il nuovo nome da attribuire all'id selezionato: ")
                
        if todolist.is_project_name_already_exixt(new_name):
            print(f"Esiste già un oggetto che si chiama: {new_name}")
            continue

        todolist.update_project_name(id_progetto, new_name)
        print(f"Update eseguito con successo per l'oggetto {id_progetto}")
        break

def main():
    todolist=Todolist()
    menu=Menu()
    while True:
        menu.printMenu()
        i= input("Seleziona l'operazione da eseguire: ")
        match i:
            case "1":
                print("*"*20)
                print("Hai scelto di aggiungere un progetto!")
                print("*"*20)
                project_name=input("Inserisci il nome del nuovo progetto: ")
                
                if todolist.is_project_name_already_exixt(project_name):
                    print(f"Esiste già un oggetto che si chiama: {project_name}")
                    continue
                
                new_project=Project(project_name)
                todolist.add_project(new_project)
                print(f"Il numero di progetti è: {todolist.get_projects_lenght()}")
                continue
            case "2":
                print("*"*20)
                print("Hai scelto di aggiungere un task!")
                print("*"*20)
               
                print("*"*20)
                print("Aggiorna l'id di un progetto, visualizzando di seguito tutti i progetti presenti!")
                print("*"*20)
                
                project=seleziona_project(todolist)
            
                if project is None:
                    continue
                
                task_title: str= input("Inserisci il titolo della task: ")
                new_task=Task(task_title)
                project.add_task(new_task)
                print("Task aggiunta con successo!")
                continue

            case "3":
                print("*"*20)
                print("Hai scelto di aggiungere un tags!")
                print("*"*20)
                continue

            case "4":
                print("*"*20)
                print("Hai scelto di visualizzare la lista dei progetti!")
                print("*"*20)
                todolist.get_projects()

            case "5":
                print("*"*20)
                print("Hai scelto di visualizzare la lista dei task!")
                print("*"*20)
                project=seleziona_project(todolist)
                if project is None:
                    continue

                print(f"Numero di task: {project.get_tasks_lenght()}")
                continue
            case "6":
                print("*"*20)
                print("Hai scelto di aggiungere la lista di tags!")
                print("*"*20)
                continue
            case "7":
                update_project_name(todolist)
                continue
            case "8":
                break
            case _:
                print("Inserisci un valore corretto.")
                continue

if __name__ == "__main__":
    main()
