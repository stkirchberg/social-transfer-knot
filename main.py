import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat App")
        
        try:
            # Windows
            self.root.state("zoomed")
        except:
            # Linux/macOS fallback
            self.root.attributes("-zoomed", True)

        self.show_home()

        self.root.mainloop()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Welcome!", font=("Arial", 40)).pack(pady=40)

        tk.Button(
            frame,
            text="Join Room",
            font=("Arial", 20),
            width=20,
            command=self.show_join_room
        ).pack(pady=20)

        tk.Button(
            frame,
            text="Create Room",
            font=("Arial", 20),
            width=20,
            command=self.show_create_room
        ).pack(pady=20)

    def show_join_room(self):
        self.clear()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Enter Room Code", font=("Arial", 30)).pack(pady=20)

        entry = tk.Entry(frame, font=("Arial", 20))
        entry.pack(pady=10)

        tk.Button(
            frame,
            text="Next",
            font=("Arial", 20),
            command=lambda: self.show_set_username(entry.get())
        ).pack(pady=20)

        tk.Button(
            frame,
            text="Back",
            font=("Arial", 18),
            command=self.show_home
        ).pack(pady=10)

    def show_create_room(self):
        self.clear()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="Create Room", font=("Arial", 30)).pack(pady=20)
        tk.Label(frame, text="(Not implemented yet)", font=("Arial", 18)).pack(pady=10)

        tk.Button(
            frame,
            text="Back",
            font=("Arial", 20),
            command=self.show_home
        ).pack(pady=20)

    def show_set_username(self, room_code):
        self.clear()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text=f"Room: {room_code}", font=("Arial", 30)).pack(pady=20)
        tk.Label(frame, text="Choose a username for this room:", font=("Arial", 25)).pack(pady=10)

        entry = tk.Entry(frame, font=("Arial", 20))
        entry.pack(pady=10)

        tk.Button(
            frame,
            text="Join",
            font=("Arial", 20),
            command=lambda: self.show_room(room_code, entry.get())
        ).pack(pady=20)

        tk.Button(
            frame,
            text="Back",
            font=("Arial", 18),
            command=self.show_join_room
        ).pack(pady=10)

    def show_room(self, room_code, username):
        self.clear()

        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text=f"Room: {room_code}", font=("Arial", 30)).pack(pady=10)
        tk.Label(frame, text=f"You are: {username}", font=("Arial", 20)).pack(pady=5)

        tk.Label(frame, text="(Chat will be added later)", font=("Arial", 20)).pack(pady=40)

        tk.Button(
            frame,
            text="Back to Home",
            font=("Arial", 20),
            command=self.show_home
        ).pack(pady=20)


App()