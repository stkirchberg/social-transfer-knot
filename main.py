import tkinter as tk
from tkinter import ttk
from core.room_manager import RoomManager
from ui.create_room import CreateRoomUI
from ui.chat_room import ChatRoomUI


class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("social transfer knot")
        self.root.state("zoomed")

        # ----------------------------
        # Core
        # ----------------------------
        self.room_manager = RoomManager()
        self.active_room = None

        # ----------------------------
        # Styles & Layout
        # ----------------------------
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

        # Sidebar
        self.sidebar_width = 450
        self.sidebar = ttk.Frame(self.container, style="Side.TFrame", width=self.sidebar_width)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Separator für Resize
        self.separator = ttk.Separator(self.container, orient="vertical", cursor="sb_h_double_arrow")
        self.separator.pack(side="left", fill="y")
        self.separator.bind("<ButtonPress-1>", self.start_resize)
        self.separator.bind("<B1-Motion>", self.perform_resize)

        # Sidebar Inhalte
        ttk.Button(self.sidebar, text="Join Room", style="Accent.TButton",
                   command=self.join_room_view).pack(fill="x", padx=10, pady=(20, 10))
        ttk.Button(self.sidebar, text="Create Room", style="Accent.TButton",
                   command=self.create_room_view).pack(fill="x", padx=10, pady=10)

        ttk.Label(self.sidebar, text="Rooms:", style="Side.TLabel",
                  font=("Arial", 12, "bold")).pack(anchor="w", padx=12, pady=(20, 5))

        self.rooms_frame = ttk.Frame(self.sidebar, style="Side.TFrame")
        self.rooms_frame.pack(fill="both", expand=True, padx=10)

        self.render_rooms()

        # Hauptbereich
        self.main_area = ttk.Frame(self.container, style="Main.TFrame")
        self.main_area.pack(side="left", fill="both", expand=True)
        self.main_label = ttk.Label(self.main_area, text="Welcome!\n\nSelect a room or create one.",
                                    style="Main.TLabel", font=("Arial", 14))
        self.main_label.pack(pady=50)

    # ----------------------------
    # Sidebar Resize
    # ----------------------------
    def start_resize(self, event):
        self.start_x = event.x

    def perform_resize(self, event):
        dx = event.x - self.start_x
        new_width = self.sidebar.winfo_width() + dx

        min_width = 100
        max_width = int(self.root.winfo_width() * 0.5)
        if new_width < min_width: new_width = min_width
        if new_width > max_width: new_width = max_width

        self.sidebar_width = new_width
        self.sidebar.config(width=new_width)
        self.sidebar.pack_propagate(False)

    # ----------------------------
    # Rooms in Sidebar
    # ----------------------------
    def render_rooms(self):
        for w in self.rooms_frame.winfo_children():
            w.destroy()
        for room_name, room in self.room_manager.rooms.items():
            ttk.Button(
                self.rooms_frame,
                text=room_name,
                command=lambda r=room_name: self.open_room(r)
            ).pack(fill="x", pady=4)

    def open_room(self, room_name):
        room = self.room_manager.get_room(room_name)
        self.clear_main()
        username = room.admin  # Admin ist automatisch
        ui = ChatRoomUI(self.main_area, room, username)
        ui.pack(fill="both", expand=True)

    # ----------------------------
    # Join / Create Room
    # ----------------------------
    def join_room_view(self):
        self.show_text("Joining room...\n(not implemented yet)")

    def create_room_view(self):
        self.clear_main()
        ui = CreateRoomUI(
            self.main_area,
            self.room_manager,
            on_room_created=self.enter_created_room
        )
        ui.pack(fill="both", expand=True)

    def enter_created_room(self, room, username):
        self.clear_main()
        ui = ChatRoomUI(self.main_area, room, username)
        ui.pack(fill="both", expand=True)
        self.render_rooms()

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