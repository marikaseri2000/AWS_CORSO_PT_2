from project import Project

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
            