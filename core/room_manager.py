import uuid
from core.storage import load_rooms, save_rooms

class Room:
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
        self.users = {admin}
        self.tokens = set()
        self.valid_tokens = {}
    def generate_token(self):
        token = uuid.uuid4().hex[:10]
        self.tokens.add(token)
        return token

    def use_token(self, token, username):
        if token in self.tokens:
            self.tokens.remove(token)
            self.users.add(username)
            return True
        return False


class RoomManager:
    def __init__(self):
        self.rooms = {}

    def create_room(self, name, admin):
        if name in self.rooms:
            raise ValueError("Room already exists")
        room = Room(name, admin)
        self.rooms[name] = room
        return room

    def get_room(self, name):
        return self.rooms.get(name)

class RoomManager:
    def __init__(self):
        self.rooms = {}
        self.load_from_disk()

    def load_from_disk(self):
        saved = load_rooms()
        for r in saved:
            room = Room(r["name"], r["admin"])
            self.rooms[r["name"]] = room

    def save_to_disk(self):
        serializable = [{"name": r.name, "admin": r.admin} for r in self.rooms.values()]
        save_rooms(serializable)

    def create_room(self, name, admin):
        if name in self.rooms:
            raise ValueError("Room already exists")
        room = Room(name, admin)
        self.rooms[name] = room
        self.save_to_disk()
        return room
