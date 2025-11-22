import tkinter as tk
from tkinter import ttk

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("social transfer knot")
        self.root.state("zoomed")

        self.active_room = None

        self.setup_styles()
        self.setup_layout()

    # ----------------------------
    # Styles (Darkmode + Accent)
    # ----------------------------
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        accent = "#E066FF"
        dark_bg = "#1E1E1E"
        sidebar_bg = "#252525"
        text_color = "#FFFFFF"

        style.configure("Side.TFrame", background=sidebar_bg)
        style.configure("Main.TFrame", background=dark_bg)
        style.configure("Side.TLabel", background=sidebar_bg, foreground=text_color)
        style.configure("Main.TLabel", background=dark_bg, foreground=text_color)

        style.configure("Accent.TButton", background=accent, foreground="black")
        style.map("Accent.TButton",
                  background=[("active", "#C64DDB")],
                  foreground=[("active", "black")])

        style.configure("TButton", background="#333333", foreground=text_color)
        style.map("TButton", background=[("active", "#444444")])

    # ----------------------------
    # Layout
    # ----------------------------
    def setup_layout(self):
        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.sidebar_width = 400

        self.sidebar = ttk.Frame(self.container, style="Side.TFrame", width=self.sidebar_width)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        ttk.Button(self.sidebar, text="Join Room", style="Accent.TButton",
                   command=self.join_room_view).pack(fill="x", padx=10, pady=(20, 10))
        ttk.Button(self.sidebar, text="Create Room", style="Accent.TButton",
                   command=self.create_room_view).pack(fill="x", padx=10, pady=10)

        ttk.Label(self.sidebar, text="Rooms:", style="Side.TLabel",
                  font=("Arial", 12, "bold")).pack(anchor="w", padx=12, pady=(20, 5))

        self.rooms_frame = ttk.Frame(self.sidebar, style="Side.TFrame")
        self.rooms_frame.pack(fill="both", expand=True, padx=10)

        self.room_names = ["Room A", "Room B", "Room C"]
        self.render_rooms()

        self.main_area = ttk.Frame(self.container, style="Main.TFrame")
        self.main_area.pack(side="left", fill="both", expand=True)
        self.main_label = ttk.Label(self.main_area, text="Welcome!\n\nSelect a room or create one.",
                                    style="Main.TLabel", font=("Arial", 14))
        self.main_label.pack(pady=50)

    # ----------------------------
    # Rooms
    # ----------------------------
    def render_rooms(self):
        for widget in self.rooms_frame.winfo_children():
            widget.destroy()
        for room in self.room_names:
            ttk.Button(self.rooms_frame, text=room,
                       command=lambda r=room: self.enter_room(r)).pack(fill="x", pady=4)

    def join_room_view(self):
        self.show_text("Joining room...\n(not implemented yet)")

    def create_room_view(self):
        self.show_text("Creating a room...\n(not implemented yet)")

    # ----------------------------
    # Enter Room → token + username
    # ----------------------------
    def enter_room(self, room_name):
        self.active_room = room_name
        self.show_token_prompt(room_name)

    def show_token_prompt(self, room):
        self.clear_main()
        ttk.Label(self.main_area, text=f"Enter token for {room}:", style="Main.TLabel",
                  font=("Arial", 14)).pack(pady=20)
        self.token_entry = ttk.Entry(self.main_area, width=40)
        self.token_entry.pack(pady=10)
        ttk.Button(self.main_area, text="Submit Token", style="Accent.TButton",
                   command=lambda: self.token_entered(self.token_entry.get())).pack(pady=10)

    def token_entered(self, token):
        if not token.strip():
            self.show_text("Token cannot be empty.")
            return
        self.username_prompt()

    def username_prompt(self):
        self.clear_main()
        ttk.Label(self.main_area, text="Choose a username for this room:",
                  style="Main.TLabel", font=("Arial", 14)).pack(pady=20)
        self.username_entry = ttk.Entry(self.main_area, width=40)
        self.username_entry.pack(pady=10)
        ttk.Button(self.main_area, text="Set Username", style="Accent.TButton",
                   command=lambda: self.username_set(self.username_entry.get())).pack(pady=10)

    def username_set(self, name):
        if not name.strip():
            self.show_text("Username cannot be empty.")
            return
        self.show_text(f"You joined {self.active_room} as: {name}\n(Chat UI coming soon)")

    # ----------------------------
    # Helper UI
    # ----------------------------
    def clear_main(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

    def show_text(self, text):
        self.clear_main()
        ttk.Label(self.main_area, text=text, style="Main.TLabel", font=("Arial", 14)).pack(pady=50)


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
