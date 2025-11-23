import json
import os

DB_PATH = "rooms.json"


def load_rooms():
    if not os.path.exists(DB_PATH):
        return []
    try:
        with open(DB_PATH, "r", encoding="utf8") as f:
            return json.load(f)
    except:
        return []


def save_rooms(rooms):
    with open(DB_PATH, "w", encoding="utf8") as f:
        json.dump(rooms, f, indent=4)
