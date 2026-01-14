import uuid
#
class Category:
    def __init__(self, name: str, color: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.color = color

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

class CategoryLibrary:
    def __init__(self):
        self.categories: list[Category] = []

    def add_category(self, name: str, color: str) -> Category:
        new_category = Category(name, color)
        self.categories.append(new_category)
        return new_category

    def remove_category(self, category_id: str) -> bool:
        for i, category in enumerate(self.categories):
            if category.get_id() == category_id:
                del self.categories[i]
                return True
        return False

    def update_category_name(self, category_id: str, new_name: str) -> bool:
        category = self.get_category_by_id(category_id)
        if category:
            category.set_name(new_name)
            return True
        return False
    
    def update_category_color(self, category_id: str, new_color: str) -> bool:
        category = self.get_category_by_id(category_id)
        if category:
            category.set_color(new_color)
            return True
        return False

    def get_category_by_id(self, category_id: str) -> Category | None:
        for category in self.categories:
            if category.get_id() == category_id:
                return category
        return None

    def get_all_categories(self) -> list[Category]:
        return self.categories
