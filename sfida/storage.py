import json
import os
from typing import Dict, Any

DB_FILE = "db.json"

def init_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({"books": []}, f, indent=2)

def load_db() -> Dict[str, Any]:
    if not os.path.exists(DB_FILE):
        init_db()
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"books": []}

def save_db(data: Dict[str, Any]):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)
