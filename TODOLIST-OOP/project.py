import uuid
from task import Task

class Project:
    def __init__(self, name: str):
        self.id=str(uuid.uuid4())
        self.name = name
        self.task_list: list[Task]=[]
    
    def get_tasks_lenght(self) -> int:
        return len(self.task_list)
    
    def get_project_id(self):
        return self.id
    
    def get_project_name(self) -> str:
        return self.name
    
    def set_project_name(self, new_name: str)-> None:
        self.name = new_name
    
    def add_task(self, new_task: Task) -> None:
        self.task_list.append(new_task)
