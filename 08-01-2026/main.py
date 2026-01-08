import uuid
import datetime

projects: list[dict]=[{'id': '628b5a3b-b79d-43d1-8fb0-8dadc67cd368', 'name': 'pippo', 'description': 'boh', 'createAt': '2026-01-08T09:13:28.545Z'}]
tasks: list[dict]=[]

def create_task (title: str,project_id: str,tags: list)->dict:
    """crea un elemento task"""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
    return  {
        'id': str(uuid.uuid4()),
        'title': title,
        'project_id': project_id,
        'is_completed': False,
        'tags': tags,
        'create_at': clean_date,
        'completed_at': None
    }

def create_project(name: str, descipion: str='') -> dict:
    """crea un elemento progetto"""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    return  {
        'id': str(uuid.uuid4()),
        'name': name,
        'description': "boh",
        'createAt': clean_date
    }

def check_task_name(title: str, tasks: list[dict]) -> bool:
    """verfica che non esista una task con lo stesso nome"""
    result: bool= False
    for p in tasks:
        if p['title'] == title:
            result= True
            break
    return result

def check_project_name(name: str, projects: list[dict]) -> bool:
    """verfica che non esista un progetto con lo stesso nome"""
    result: bool= False
    for p in projects:
        if p['name'] == name:
            result= True
            break
    return result

def save_task(title: str, project_id: str, tags: list)->None:
    """salva il task nel db"""
    if check_task_name(title, tasks):
        raise ValueError (f"il progetto {title} esiste già!!")
    task = create_task(title, project_id, tags)
    tasks.append(task)
    print(tasks)

def save_project(name: str, description: str="")->None:
    """salva il progetto nel db"""
    if check_project_name(name, projects):
        raise ValueError (f"il progetto {name} esiste già!!")
    project= create_project(name, description)
    projects.append(project)
    print(projects)


def main()-> None:
    try:
        print(save_task("compra pomodori", '628b5a3b-b79d-43d1-8fb0-8dadc67cd368', ['spesa']))
        print(save_task("compra pomodori", '628b5a3b-b79d-43d1-8fb0-8dadc67cd368', ['spesa']))
    except ValueError as e:
        print(f"L'errore: {e}")

if __name__ == "__main__":
    main()