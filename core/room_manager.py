import uuid

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
