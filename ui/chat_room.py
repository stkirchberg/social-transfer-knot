import tkinter as tk
from tkinter import ttk


class ChatRoomUI(ttk.Frame):
    def __init__(self, master, room, username):
        super().__init__(master)
        self.room = room
        self.username = username

        top = ttk.Frame(self)
        top.pack(fill="x", padx=10, pady=(10, 0))

        ttk.Label(top, text=f"Room: {room.name}", font=("Arial", 14)).pack(side="left")

        if username == room.admin:
            ttk.Button(top, text="Generate Token",
                       command=self.generate_token).pack(side="right")

        self.chat = tk.Text(self, height=20, state="disabled")
        self.chat.pack(fill="both", expand=True, padx=10, pady=10)

        self.entry = ttk.Entry(self)
        self.entry.pack(fill="x", padx=10, pady=10)
        self.entry.bind("<Return>", self.handle_input)

    def generate_token(self):
        token = self.room.generate_token()
        self._print(f"Generated token: {token}")

    def handle_input(self, event=None):
        text = self.entry.get().strip()
        self.entry.delete(0, "end")

        if not text:
            return

        self._print(f"{self.username}: {text}")

    def _print(self, msg):
        self.chat.config(state="normal")
        self.chat.insert("end", msg + "\n")
        self.chat.config(state="disabled")
        self.chat.see("end")