import json
import os

DATA_FILE = "supermarket_data.json"

def load_data():
    """Loads data from the JSON file. Returns an empty structure if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return {"products": [], "tasks": []}
    
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
            # Backup corrupted file if needed, but for now just return empty to avoid crash
        return {"products": [], "tasks": []}

def save_data(data):
    """Saves data to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")
