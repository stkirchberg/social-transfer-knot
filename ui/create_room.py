import tkinter as tk
from tkinter import ttk

class CreateRoomUI(ttk.Frame):
    def __init__(self, master, room_manager, on_room_created):
        super().__init__(master)
        self.room_manager = room_manager
        self.on_room_created = on_room_created

        ttk.Label(self, text="Room Name:", font=("Arial", 14)).pack(pady=(20, 10))
        self.entry = ttk.Entry(self, width=40)
        self.entry.pack(pady=10)

        ttk.Button(self, text="Create",
                   command=self.create_room).pack(pady=10)

    def create_room(self):
        name = self.entry.get().strip()
        if not name:
            return
        
        try:
            room = self.room_manager.create_room(name, admin="you")
        except ValueError:
            return

        self.on_room_created(room)
