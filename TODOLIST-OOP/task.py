import uuid

from tag import TagLibrary, Tag

class Task():
    def __init__(self, title: str):
        self.id=str(uuid.uuid4())
        self.title = title
        self.isComplete=False
        self.tag_list: list[Tag]=[]

    def add_tag(self, tag_library: TagLibrary, name: str, color: str, category_id: str) -> None:
        """
        Assigns a tag to the task. 
        Uses the provided TagLibrary to get or create the tag.
        """
        tag = tag_library.add_tag(name, color, category_id)
        # Check if we already have this tag assigned to avoid local duplication
        if tag not in self.tag_list:
            self.tag_list.append(tag)
    
    def get_id(self):
        """Restituiscie l'id del task"""
        return self.id
    
    def get_title(self) -> str:
        """Restituisce il titolo del task"""
        return self.title
    
    def set_title(self, new_title: str) -> None:
        if not isinstance(new_title, str):
            raise ValueError("Il titolo deve essere una stringa")
        if not new_title or not new_title.strip():
            raise ValueError("Il titolo non può essere vuoto")
        self.title = new_title
        
        