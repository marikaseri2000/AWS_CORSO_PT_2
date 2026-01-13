import uuid

class Tag:
    def __init__(self, name: str, color: str, category_id: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.color = color
        self.category_id = category_id

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name

    def get_color(self) -> str:
        return self.color
    
    def set_color(self, color: str) -> None:
        self.color = color

    def get_category_id(self) -> str:
        return self.category_id


class TagLibrary:
    def __init__(self):
        self.tags: list[Tag] = []

    def add_tag(self, name: str, color: str, category_id: str) -> Tag:
        # Check if tag already exists to avoid duplication
        existing_tag = self.find_tag_by_name(name)
        if existing_tag:
            return existing_tag
        
        new_tag = Tag(name, color, category_id)
        self.tags.append(new_tag)
        return new_tag

    def remove_tag(self, tag_id: str) -> bool:
        for i, tag in enumerate(self.tags):
            if tag.get_id() == tag_id:
                del self.tags[i]
                return True
        return False

    def update_tag_name(self, tag_id: str, new_name: str) -> bool:
        tag = self.get_tag_by_id(tag_id)
        if tag:
            tag.set_name(new_name)
            return True
        return False
    
    def update_tag_color(self, tag_id: str, new_color: str) -> bool:
        tag = self.get_tag_by_id(tag_id)
        if tag:
            tag.set_color(new_color)
            return True
        return False

    def find_tag_by_name(self, name: str) -> Tag | None:
        for tag in self.tags:
            if tag.get_name() == name:
                return tag
        return None

    def get_tag_by_id(self, tag_id: str) -> Tag | None:
        for tag in self.tags:
            if tag.get_id() == tag_id:
                return tag
        return None

    def get_all_tags(self) -> list[Tag]:
        return self.tags
