import uuid

class Task():
    def __init__(self, title: str):
        self.id=str(uuid.uuid4())
        self.title = title
        self.isComplete=False
    
    def get_id(self):
        """Restituiscie l'id del task"""
        return self.id
    
    def get_title(self) -> str:
        """Restituisce il titolo del task"""
        return self.title
        
        