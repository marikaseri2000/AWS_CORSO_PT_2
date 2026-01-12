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
