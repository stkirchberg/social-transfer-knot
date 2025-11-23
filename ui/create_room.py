import tkinter as tk
from tkinter import ttk

class CreateRoomUI(ttk.Frame):
    def __init__(self, master, room_manager, on_room_created):
        super().__init__(master)
        self.room_manager = room_manager
        self.on_room_created = on_room_created

        ttk.Label(self, text="Room Name:", font=("Arial", 14)).pack(pady=(20, 10))
        self.room_entry = ttk.Entry(self, width=40)
        self.room_entry.pack(pady=10)

        ttk.Label(self, text="Your Username:", font=("Arial", 14)).pack(pady=(20, 10))
        self.user_entry = ttk.Entry(self, width=40)
        self.user_entry.pack(pady=10)

        ttk.Button(self, text="Create Room",
                   command=self.create_room).pack(pady=20)

    def create_room(self):
        name = self.room_entry.get().strip()
        user = self.user_entry.get().strip()

        if not name or not user:
            return

        try:
            room = self.room_manager.create_room(name, admin=user)
        except ValueError:
            return

        self.on_room_created(room, user)
