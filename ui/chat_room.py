import tkinter as tk
from tkinter import ttk

class ChatRoomUI(ttk.Frame):
    def __init__(self, master, room):
        super().__init__(master)
        self.room = room

        self.chat = tk.Text(self, height=20, state="disabled")
        self.chat.pack(fill="both", expand=True, padx=10, pady=10)

        self.entry = ttk.Entry(self)
        self.entry.pack(fill="x", padx=10, pady=10)
        self.entry.bind("<Return>", self.handle_input)

    def handle_input(self, event=None):
        text = self.entry.get().strip()
        self.entry.delete(0, "end")

        if not text:
            return

        if text == "/token":
            token = self.room.generate_token()
            self._print(f"Generated token: {token}")
            return

        self._print(f"You: {text}")

    def _print(self, msg):
        self.chat.config(state="normal")
        self.chat.insert("end", msg + "\n")
        self.chat.config(state="disabled")
        self.chat.see("end")
