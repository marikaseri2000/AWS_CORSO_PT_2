import models
import data_handler

# Module-level state
_products = []
_tasks = []

def load_data():
    """Initializes data from storage."""
    global _products, _tasks
    raw_data = data_handler.load_data()
    # Data is already in dict format from JSON, but we ensure structure
    _products = raw_data.get("products", [])
    _tasks = raw_data.get("tasks", [])

def save_data():
    """Saves current state to storage."""
    data = {
        "products": _products,
        "tasks": _tasks
    }
    data_handler.save_data(data)

def add_product(name, price):
    global _products
    new_id = 1
    if _products:
        new_id = max(p["id"] for p in _products) + 1
    
    product = models.create_product(new_id, name, price)
    _products.append(product)
    save_data()
    return product

def get_products():
    return _products

def remove_product(product_id):
    global _products, _tasks
    # Remove product and its associated tasks
    _products = [p for p in _products if p["id"] != product_id]
    _tasks = [t for t in _tasks if t["product_id"] != product_id]
    save_data()

def add_task(description, product_id):
    global _tasks
    # Verify product exists
    if not any(p["id"] == product_id for p in _products):
        raise ValueError(f"Product with ID {product_id} not found.")

    new_id = 1
    if _tasks:
        new_id = max(t["id"] for t in _tasks) + 1
    
    task = models.create_task(new_id, description, product_id)
    _tasks.append(task)
    save_data()
    return task

def get_tasks(product_id=None):
    if product_id:
        return [t for t in _tasks if t["product_id"] == product_id]
    return _tasks

def complete_task(task_id):
    for task in _tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_data()
            return task
    raise ValueError(f"Task with ID {task_id} not found.")

# Initialize data on module load
load_data()
