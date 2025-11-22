import tkinter as tk
from tkinter import ttk


class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")
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

        screen_width = self.root.winfo_screenwidth()
        self.min_width = 150
        self.max_width = screen_width // 2

        self.sidebar_width = int(screen_width * 0.20)

        self.sidebar = ttk.Frame(self.container, style="Side.TFrame", width=self.sidebar_width)
        self.sidebar.pack(side="left", fill="y")

        self.resize_handle = tk.Frame(self.container, bg="#444", cursor="sb_h_double_arrow", width=6)
        self.resize_handle.pack(side="left", fill="y")

        self.resize_handle.bind("<Button-1>", self.start_resize)
        self.resize_handle.bind("<B1-Motion>", self.perform_resize)

        ttk.Button(self.sidebar, text="Join Room", style="Accent.TButton",
                   command=self.join_room_view).pack(fill="x", padx=10, pady=(20, 10))

        ttk.Button(self.sidebar, text="Create Room", style="Accent.TButton",
                   command=self.create_room_view).pack(fill="x", padx=10, pady=10)

        ttk.Label(self.sidebar, text="Rooms:", style="Side.TLabel",
                  font=("Arial", 12, "bold")).pack(anchor="w", padx=12, pady=(20, 5))

        self.rooms_frame = ttk.Frame(self.sidebar, style="Side.TFrame")
        self.rooms_frame.pack(fill="both", expand=True, padx=10)

        for room in ["Room A", "Room B", "Room C"]:
            ttk.Button(self.rooms_frame, text=room,
                       command=lambda r=room: self.enter_room(r)).pack(fill="x", pady=4)

        self.main_area = ttk.Frame(self.container, style="Main.TFrame")
        self.main_area.pack(side="left", fill="both", expand=True)

        self.main_label = ttk.Label(
            self.main_area,
            text="Welcome!\n\nSelect a room or create one.",
            style="Main.TLabel",
            font=("Arial", 14)
        )
        self.main_label.pack(pady=50)

    # ----------------------------
    # Sidebar Resize
    # ----------------------------
    def start_resize(self, event):
        self.drag_start_x = event.x

    def perform_resize(self, event):
        delta = event.x - self.drag_start_x
        new_width = self.sidebar.winfo_width() + delta

        if new_width < self.min_width:
            new_width = self.min_width
        if new_width > self.max_width:
            new_width = self.max_width

        self.sidebar.config(width=new_width)

    # ----------------------------
    # Views
    # ----------------------------
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

        entry = ttk.Entry(self.main_area, width=40)
        entry.pack(pady=10)

        ttk.Button(self.main_area, text="Submit Token", style="Accent.TButton",
                   command=lambda: self.token_entered(entry.get())).pack(pady=10)

    def token_entered(self, token):
        if not token.strip():
            self.show_text("Token cannot be empty.")
            return

        self.username_prompt()

    def username_prompt(self):
        self.clear_main()
        ttk.Label(self.main_area, text="Choose a username for this room:",
                  style="Main.TLabel", font=("Arial", 14)).pack(pady=20)

        entry = ttk.Entry(self.main_area, width=40)
        entry.pack(pady=10)

        ttk.Button(self.main_area, text="Set Username", style="Accent.TButton",
                   command=lambda: self.username_set(entry.get())).pack(pady=10)

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
        ttk.Label(self.main_area, text=text, style="Main.TLabel",
                  font=("Arial", 14)).pack(pady=50)


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
