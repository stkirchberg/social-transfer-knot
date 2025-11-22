class MockServer:
    def __init__(self):
        self.rooms = {}

    def create_room(self, room_name):
        if room_name not in self.rooms:
            self.rooms[room_name] = {"messages": [], "users": []}
            return True
        return False

    def join_room(self, room_name, username):
        if room_name not in self.rooms:
            return False

        if username not in self.rooms[room_name]["users"]:
            self.rooms[room_name]["users"].append(username)

        return True

    def send_message(self, room_name, username, text):
        if room_name not in self.rooms:
            return False

        msg = {"user": username, "text": text}
        self.rooms[room_name]["messages"].append(msg)
        return msg

    def get_messages(self, room_name):
        if room_name not in self.rooms:
            return []

        return self.rooms[room_name]["messages"]
