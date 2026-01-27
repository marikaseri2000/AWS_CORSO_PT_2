import requests

def get_project():
    data=requests.get("http://127.0.0.1:8000/projects/")
    print(data.json()) #puliamo il file project con il metodo .json()

def get_task_by_project_id(project_id: str):
    data=requests.get(f"http://127.0.0.1:8000/tasks/project/{project_id}/")
    print(data.json()) #puliamo il file task con il metodo .json()

def main():
    #Assuminamo che il main lanci il menu con varie opzioni. 
    # Tra queste la lista dei progetti.
    print("*"*40)
    print("STAMPA I PROJECT")
    print("*"*40)
    get_project()
    print("*"*40)
    print("STAMPA I TASK")
    print("*"*40)
    get_task_by_project_id('32f6c272-896a-4781-8b82-be0cc7829dba')

main()