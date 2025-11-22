import tkinter as tk

class LoginPage:
    def __init__(self, app):
        self.app = app

        self.window = tk.Frame(app.root)
        self.window.pack()

        tk.Label(self.window, text="name:").pack()
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack()

        tk.Button(self.window, text="going", command=self.login).pack()

    def login(self):
        username = self.username_entry.get()
        if username:
            self.app.username = username
            self.window.destroy()
            self.app.open_room_list()
