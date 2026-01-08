def create_product(product_id, name, price):
    """Factory function to create a product dictionary."""
    return {
        "id": product_id,
        "name": name,
        "price": price
    }

def create_task(task_id, description, product_id, status="Open"):
    """Factory function to create a task dictionary."""
    return {
        "id": task_id,
        "description": description,
        "product_id": product_id,
        "status": status
    }
