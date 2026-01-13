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
                
                # Option to assign tag immediately
                print("Vuoi assegnare un tag a questo task? (s/n)")
                if input().lower() == 's':
                    # Show available categories and tags or prompt to create
                    tags = todolist.tag_library.get_all_tags()
                    if not tags:
                        print("Non ci sono tag disponibili. Crea prima Categorie e Tag.")
                    else:
                        print("Tag disponibili:")
                        for t in tags:
                            print(f"ID: {t.get_id()} - Nome: {t.get_name()} - Colore: {t.get_color()}")
                        
                        tag_name = input("Inserisci il nome del tag da assegnare: ")
                        # We need category_id and color to 'get or create' via add_tag, 
                        # but if selecting existing, logic should be slightly different or we just ask parameters.
                        # For simplicity, let's ask for the tag parameters to ensure 'get or create' works as designed in Task.add_tag
                        
                        existing_tag = todolist.tag_library.find_tag_by_name(tag_name)
                        if existing_tag:
                            new_task.add_tag(todolist.tag_library, existing_tag.get_name(), existing_tag.get_color(), existing_tag.get_category_id())
                            print(f"Tag '{tag_name}' assegnato.")
                        else:
                            print("Tag non trovato. Usa il menu 'Add Tag' per crearne uno nuovo con tutti i dettagli.")

                project.add_task(new_task)
                print("Task aggiunta con successo!")
                continue

            case "3":
                print("*"*20)
                print("Hai scelto di aggiungere una Categoria!") 
                print("*"*20)
                cat_name = input("Inserisci il nome della categoria: ")
                cat_color = input("Inserisci il colore della categoria: ")
                todolist.category_library.add_category(cat_name, cat_color)
                print("Categoria aggiunta con successo!")
                continue

            case "4":
                print("*"*20)
                print("Hai scelto di aggiungere un Tag!") 
                print("*"*20)
                
                # Check for categories first
                categories = todolist.category_library.get_all_categories()
                if not categories:
                    print("ATTENZIONE: Devi creare almeno una categoria prima di creare un tag.")
                    continue

                print("Categorie disponibili:")
                for cat in categories:
                    print(f"ID: {cat.get_id()} - Nome: {cat.get_name()}")

                cat_id = input("Inserisci l'ID della categoria per questo tag: ")
                # Verify category exists
                if not todolist.category_library.get_category_by_id(cat_id):
                   print("ID Categoria non valido.")
                   continue

                tag_name = input("Inserisci il nome del tag: ")
                tag_color = input("Inserisci il colore del tag: ")
                
                todolist.tag_library.add_tag(tag_name, tag_color, cat_id)
                print("Tag aggiunto con successo!")
                continue

            case "5":
                print("*"*20)
                print("Hai scelto di visualizzare la lista dei progetti!")
                print("*"*20)
                todolist.get_projects()

            case "6":
                print("*"*20)
                print("Hai scelto di visualizzare la lista dei task!")
                print("*"*20)
                project=seleziona_project(todolist)
                if project is None:
                    continue

                print(f"Numero di task: {project.get_tasks_lenght()}")
                for t in project.task_list:
                    tag_str = ", ".join([tag.get_name() for tag in t.tag_list])
                    print(f"- {t.get_title()} [Tags: {tag_str}]")
                continue
            
            case "7":
                print("*"*20)
                print("Lista Categorie:")
                print("*"*20)
                for cat in todolist.category_library.get_all_categories():
                    print(f"ID: {cat.get_id()} | Nome: {cat.get_name()} | Colore: {cat.get_color()}")
                continue

            case "8":
                print("*"*20)
                print("Lista Tags:")
                print("*"*20)
                for tag in todolist.tag_library.get_all_tags():
                     # Find category name for display
                    cat = todolist.category_library.get_category_by_id(tag.get_category_id())
                    cat_name = cat.get_name() if cat else "N/A"
                    print(f"ID: {tag.get_id()} | Nome: {tag.get_name()} | Colore: {tag.get_color()} | Categoria: {cat_name}")
                continue

            case "9":
                update_project_name(todolist)
                continue
            case "10":
                break
            case _:
                print("Inserisci un valore corretto.")
                continue

if __name__ == "__main__":
    main()
