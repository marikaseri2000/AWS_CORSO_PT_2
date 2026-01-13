from project import Project
from tag import TagLibrary
from category import CategoryLibrary

class Todolist:
    def __init__(self):
        self.projects: list[Project]=[]
        self.tag_library = TagLibrary()
        self.category_library = CategoryLibrary()

    def add_project(self, project: Project)->None:
        self.projects.append(project)
    
    def get_projects_lenght(self) -> int:
        return len(self.projects)

    def get_projects(self)-> list[Project]:
        for p in self.projects:
            print (f"{p.id} {p.name}")

    def is_project_name_already_exixt(self, new_name: str) -> bool:
        for p in self.projects:
            #un metodo ha bisogno di parentesi
            if p.get_project_name() == new_name.strip():
                return True
            else:
                return False
        
    def get_project_by_id(self, id: str) -> Project | None:
        return next((project for project in self.projects if project.get_project_id() == id), None)

        
    def update_project_name(self, id: str, new_name: str) -> None:
        """Update the project name based on his id"""
        project = self.get_project_by_id(id)

        if project is None:
            print("Il projetto con questo ID non esiste.")

        project.set_project_name(new_name)