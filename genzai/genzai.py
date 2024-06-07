# @name: Genzai!
# @author: Dino Paulo R. Gomez 2024

from pypresence import Presence
from PIL import ImageTk
import customtkinter as ctk
from datetime import datetime
import time
import sys
import os

# Dont really understand why, but it increases the render speed.
# Caught ibus to be getting most of the cpu% so quick read
# through github leads me to this fix.

# disable input methods to improve speed
# @https://github.com/ibus/ibus/issues/2324#issuecomment-996449177

os.environ['XMODIFIERS'] = "@im=none"

# App Constants
CONFIG = {
    "TITLE": "Genzai: Discord Rich Presence @dinogomez",
    "DIMENSION": "520x480",

}

# Widget Coloring
STYLE = {
    "NORMAL": "#2fa572",
    "DISABLED": "#0e5637",
    "ENTRY": "#343638",
    "ENTRY_DISABLED": "#28292a"
}

# Retrieves assets relpath


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Discord Presence provided by pypresence


class DiscordRPC:
    def __init__(self):
        self.RPC = Presence(None)

    def connect(self, client_id):
        try:
            self.RPC = Presence(client_id)
            self.RPC.connect()
            self.RPC.update(state="Launching Genzai 🚀",
                            details="A user is preparing his presence.", start=int(time.time()))
            return True, None
        except Exception as e:
            return False, e

    def disconnect(self):
        try:
            self.RPC.close()
            return True
        except:
            return False

    def update_presence(self, **kwargs):
        if self.RPC:
            presence = {}
            for key, value in kwargs.items():
                if value:
                    presence[key] = value
            print("Args", presence)
            self.RPC.update(**presence)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Discord Presence
        self.discord_rpc = DiscordRPC()

        # Timestamp Timers
        self.start_time = time.time()
        self.update_timestamp = None
        self.selected_timestamp = None

        # App Configs
        ctk.set_default_color_theme("green")
        self.title(CONFIG["TITLE"])
        self.geometry(CONFIG["DIMENSION"])
        self.resizable(False, False)

        # App Main Frame [Frame]
        self.frame = ctk.CTkFrame(master=self)
        self.frame.grid_columnconfigure((0, 1), weight=1)
        self.frame.pack(padx=10, pady=10, fill="x")

        # Client ID [Label,Entry]@Grid
        self.label_client_id = ctk.CTkLabel(
            self.frame, text="Client ID", font=("Consolas", 12))
        self.label_client_id.grid(row=0, column=0, padx=5, pady=5)

        self.entry_client_id = ctk.CTkEntry(self.frame)
        self.entry_client_id.grid(
            row=0, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        # Connect [Button:connect()]@Grid
        self.button_connect = ctk.CTkButton(self.frame, text="Connect", font=(
            "Consolas", 12), command=self.connect, width=110)
        self.button_connect.grid(row=0, column=4, padx=3, sticky="w")

        # Disconnect [Button:disconnect()]@Grid
        self.button_disconnect = ctk.CTkButton(self.frame, state="disabled", text="Disconnect", fg_color=STYLE["DISABLED"], font=(
            "Consolas", 12), command=self.disconnect, width=110)
        self.button_disconnect.grid(row=0, column=5, padx=3, sticky="we")

        # Details [Label,Entry]@Grid
        self.label_details = ctk.CTkLabel(
            self.frame, text="Details", font=("Consolas", 12))
        self.label_details.grid(row=1, column=0, padx=5, pady=5)

        self.entry_details = ctk.CTkEntry(self.frame)
        self.entry_details.grid(
            row=1, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        # Party State [Label, Entry]@Grid
        self.label_state = ctk.CTkLabel(
            self.frame, text="State", font=("Consolas", 12))
        self.label_state.grid(row=2, column=0, padx=5, pady=5)

        self.entry_state = ctk.CTkEntry(self.frame)
        self.entry_state.grid(row=2, column=1, columnspan=2,
                              padx=5, pady=5, sticky="we")

        # Party [Label]@Grid
        self.label_party = ctk.CTkLabel(
            self.frame, text="Party", font=("Consolas", 12), width=5)
        self.label_party.grid(row=2, column=3, padx=5, pady=5, sticky="w")

        # Party Min [Entry:validate_integer()]@Grid
        self.vcmd = (self.register(self.validate_integer), '%P')
        self.entry_party_min = ctk.CTkEntry(
            self.frame, validate="key", validatecommand=self.vcmd, width=90, placeholder_text=0)
        self.entry_party_min.grid(
            row=2, column=4, padx=(5, 25), pady=5, sticky="we")

        # Party Separator [Label]@Grid
        self.separator_label = ctk.CTkLabel(
            self.frame, text="of", font=("Consolas", 12))
        self.separator_label.grid(row=2, column=4, padx=5, pady=5, sticky="e")

        # Party Max [Entry:validate_integer()]@Grid
        self.vcmd = (self.register(self.validate_integer), '%P')
        self.entry_party_max = ctk.CTkEntry(
            self.frame, validate="key", validatecommand=self.vcmd, width=10, placeholder_text=1)
        self.entry_party_max.grid(row=2, column=5, padx=5, pady=5, sticky="we")

        # Timestamp Dropdown Content
        self.timestamp_list = ["None", "Start Time",
                               "Last Update", "Local Time", "Custom Timestamp"]

        # Timestamp [Label, Combobox]@Grid
        self.label_timestamp = ctk.CTkLabel(
            self.frame, text="Timestamp", font=("Consolas", 12))
        self.label_timestamp.grid(row=3, column=0, padx=5, pady=5)

        self.combobox_var = ctk.StringVar(
            value=self.timestamp_list[1])  # set initial value
        self.combobox_timestamp = ctk.CTkComboBox(self.frame,
                                                  values=self.timestamp_list,
                                                  command=self.combobox_timestamp_callback,
                                                  variable=self.combobox_var
                                                  )
        self.combobox_timestamp.grid(
            row=3, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        # Custom Timestamp [Label,Entry]@Grid
        self.label_custom_timestamp = ctk.CTkLabel(
            self.frame, text="Custom", font=("Consolas", 12), width=5)
        self.label_custom_timestamp.grid(
            row=3, column=3, padx=5, pady=5, sticky="w")

        self.entry_custom_timestamp = ctk.CTkEntry(
            self.frame, validate="key", state="disabled", fg_color=STYLE["ENTRY"])
        self.entry_custom_timestamp.grid(
            row=3, column=4, columnspan=3, padx=5, pady=5, sticky="we")

        # Large Image [Label]@Grid
        self.label_large_image = ctk.CTkLabel(
            self.frame, text="Large Image", font=("Consolas", 12))
        self.label_large_image.grid(
            row=6, column=1, padx=5, pady=5, sticky="w")

        # Large Image URL [Entry]@Grid
        self.entry_large_image_url = ctk.CTkEntry(self.frame)
        self.entry_large_image_url.grid(
            row=7, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        # Large Image Text [Entry]@Grid
        self.entry_large_image_text = ctk.CTkEntry(self.frame)
        self.entry_large_image_text.grid(
            row=8, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        # Small Image [Label]@Grid
        self.label_small_image = ctk.CTkLabel(
            self.frame, text="Small Image", font=("Consolas", 12))
        self.label_small_image.grid(
            row=6, column=4, padx=5, pady=5, sticky="w")

        # Small Image Url [Entry]@Grid
        self.entry_small_image_url = ctk.CTkEntry(self.frame)
        self.entry_small_image_url.grid(
            row=7, column=4, columnspan=3, padx=5, pady=5, sticky="we")

        # Small Image Text [Entry]@Grid
        self.entry_small_image_text = ctk.CTkEntry(self.frame)
        self.entry_small_image_text.grid(
            row=8, column=4, columnspan=3, padx=5, pady=5, sticky="we")

        # Image URL [Label]@Grid
        self.label_image_url = ctk.CTkLabel(
            self.frame, text="URL", font=("Consolas", 12))
        self.label_image_url.grid(row=7, column=0, padx=5, pady=5)

        # Image Text [Label]@Grid
        self.label_image_text = ctk.CTkLabel(
            self.frame, text="Text", font=("Consolas", 12))
        self.label_image_text.grid(row=8, column=0, padx=5, pady=5)

        # Button 1 [Label]@Grid
        self.label_button_one = ctk.CTkLabel(
            self.frame, text="Button 1", font=("Consolas", 12))
        self.label_button_one.grid(row=9, column=1, padx=5, pady=5, sticky="w")

        # Button 1 Url [Entry]@Grid
        self.entry_button_one_url = ctk.CTkEntry(self.frame)
        self.entry_button_one_url.grid(
            row=10, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        # Button 1 Text [Entry]@Grid
        self.entry_button_one_text = ctk.CTkEntry(self.frame)
        self.entry_button_one_text.grid(
            row=11, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        # Button 2 [Label]@Grid
        self.label_button_two = ctk.CTkLabel(
            self.frame, text="Button 2", font=("Consolas", 12))
        self.label_button_two.grid(row=9, column=4, padx=5, pady=5, sticky="w")

        # Button 2 Url [Entry]@Grid
        self.entry_button_two_url = ctk.CTkEntry(self.frame)
        self.entry_button_two_url.grid(
            row=10, column=4, columnspan=3, padx=5, pady=5, sticky="we")

        # Button 2 Text [Entry]@Grid
        self.entry_button_two_text = ctk.CTkEntry(self.frame)
        self.entry_button_two_text.grid(
            row=11, column=4, columnspan=3, padx=5, pady=5, sticky="we")

        # Button URL [Label]@Grid
        self.label_button_url = ctk.CTkLabel(
            self.frame, text="URL", font=("Consolas", 12))
        self.label_button_url.grid(row=10, column=0, padx=5, pady=5)

        # Button Text [Label]@Grid
        self.label_button_text = ctk.CTkLabel(
            self.frame, text="TEXT", font=("Consolas", 12))
        self.label_button_text.grid(row=11, column=0, padx=5, pady=5)

        # Update Presence [Button:update()]@Grid
        self.button_update = ctk.CTkButton(self.frame, state="disabled", fg_color=STYLE["DISABLED"], text="Update Presence", font=(
            "Consolas", 12), border_width=1, command=self.update)
        self.button_update.grid(
            row=12, column=0, columnspan=6, padx=5, pady=10, sticky="ew")

        # Connection State [Label]@Pack
        self.label_connection_state = ctk.CTkLabel(
            master=self, text="Disconnected", font=("Consolas", 12),)
        self.label_connection_state.pack(padx=15, pady=(0, 5), side="right")

        # Error State [Label]@Pack
        self.label_error_state = ctk.CTkLabel(
            master=self, text="", text_color="red", font=("Consolas", 12),)
        self.label_error_state.pack(pady=(0, 5), padx=15, side="left")

        # Vars
        self.isConnected = False

    def update(self):

        self.label_error_state.configure(text="")

        self.details = self.entry_details.get()
        self.party_state = self.entry_state.get()
        self.party_min = self.entry_party_min.get()
        self.party_max = self.entry_party_max.get()
        self.timestamp = ""
        self.large_img_url = self.entry_large_image_url.get()
        self.large_img_txt = self.entry_large_image_text.get()
        self.small_img_url = self.entry_small_image_url.get()
        self.small_img_txt = self.entry_small_image_text.get()
        self.button_one_txt = self.entry_button_one_text.get()
        self.button_one_url = self.entry_button_one_url.get()
        self.button_two_txt = self.entry_button_two_text.get()
        self.button_two_url = self.entry_button_two_url.get()
        self.buttons = []

        if self.invalid_length(value=self.details):
            self.label_error_state.configure(
                text="Details needs 2 or more characters.")
            return
        if self.invalid_length(value=self.party_state):
            self.label_error_state.configure(
                text="Party State needs 2 or more characters.")
            return
        if self.invalid_length(value=self.large_img_txt):
            self.label_error_state.configure(
                text="Large Image Text needs 2 or more characters.")
            return

        if self.invalid_length(value=self.small_img_txt):
            self.label_error_state.configure(
                text="Small Image Text needs 2 or more characters.")
            return

        if self.party_min:
            if not self.party_state:
                self.label_error_state.configure(
                    text="Party number needs a state.")
                return
            if not self.party_max:
                self.label_error_state.configure(text="Max is required.")
                return
            elif int(self.party_min) > int(self.party_max):
                self.label_error_state.configure(
                    text="Min must not exceed or equal Max")
                self.party_min = 0
                return

        if self.button_one_url:
            button_one = {"url": self.button_one_url}
            if self.button_one_txt:
                button_one["label"] = self.button_one_txt
                self.buttons.append(button_one)
            else:
                self.label_error_state.configure(
                    text="Button 1 needs a label.")

        if self.button_two_url:
            button_two = {"url": self.button_one_url}
            if self.button_two_txt:
                button_two["label"] = self.button_two_txt
                self.buttons.append(button_two)
            else:
                self.label_error_state.configure(
                    text="Button 2 needs a label.")

        if self.combobox_timestamp.get() == self.timestamp_list[4]:
            custom_timestamp = self.entry_custom_timestamp.get(
            ).strip().replace('\n', '\\n').replace('\r', '\\r')
            if custom_timestamp:
                try:
                    dt = datetime.strptime(
                        custom_timestamp, "%B %d, %Y %I:%M:%S %p")
                    timestamp = int(time.mktime(dt.timetuple()))
                    self.selected_timestamp = timestamp
                except ValueError:
                    self.label_error_state.configure(
                        text="Invalid custom timestamp.")

        if self.isConnected:
            update_kwargs = {}
            if self.details:
                update_kwargs["details"] = self.details
            if self.party_state:
                update_kwargs["state"] = self.party_state
            if self.timestamp:
                update_kwargs["start"] = self.timestamp
            if self.large_img_url and self.large_img_txt:
                update_kwargs["large_image"] = (self.large_img_url)
                update_kwargs["large_text"] = self.large_img_txt
            if self.small_img_url and self.small_img_txt:
                update_kwargs["small_image"] = (self.small_img_url)
                update_kwargs["small_text"] = self.small_img_txt
            if self.buttons:
                update_kwargs["buttons"] = self.buttons
            if self.party_min and self.party_max:
                party_size = [int(self.party_min), int(self.party_max)]
                update_kwargs["party_size"] = party_size
            if self.selected_timestamp:
                update_kwargs["start"] = self.selected_timestamp
            if update_kwargs:
                self.discord_rpc.update_presence(**update_kwargs)
                self.update_timestamp = datetime.now().timestamp()
                self.label_error_state.configure(text="")

        else:
            self.label_error_state.configure(text="No connection available.")

    def connect(self):

        self.client_id = self.entry_client_id.get()

        if self.client_id:
            success, res = self.discord_rpc.connect(self.client_id)
            if success:
                self.isConnected = True
                self.label_connection_state.configure(text="Connected")
                self.button_connect.configure(
                    state="disabled", fg_color=STYLE["DISABLED"])
                self.button_disconnect.configure(
                    state="normal", fg_color=STYLE["NORMAL"])
                self.button_update.configure(
                    state="normal", fg_color=STYLE["NORMAL"])
                self.label_error_state.configure(text="")
            else:
                self.label_error_state.configure(
                    text=f"Connection Failed. {res.message}")
        else:
            self.label_error_state.configure(text="No client id.")

    def disconnect(self):
        if self.isConnected:
            if self.discord_rpc.disconnect():
                self.isConnected = False
                self.label_connection_state.configure(text="Disconnected")
                self.button_connect.configure(
                    state="normal", fg_color=STYLE["NORMAL"])
                self.button_disconnect.configure(
                    state="disabled", fg_color=STYLE["DISABLED"])
                self.button_update.configure(
                    state="disabled", fg_color=STYLE["DISABLED"])
                self.label_error_state.configure(text="")

    def validate_integer(self, P):
        if P == "":
            return True
        try:
            value = int(P)
            if value < 0:
                return False
            return True
        except ValueError:
            return False

    def invalid_length(self, value):
        if len(value) == 1:
            return True
        return False

    def combobox_timestamp_callback(self, choice):

        if choice != self.timestamp_list[4]:
            self.entry_custom_timestamp.configure(
                state="disabled", fg_color=STYLE["ENTRY"])

        if choice == self.timestamp_list[1]:
            self.selected_timestamp = self.start_time
            return
        elif choice == self.timestamp_list[2]:
            self.selected_timestamp = self.update_timestamp
            return
        elif choice == self.timestamp_list[3]:
            self.selected_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return
        elif choice == self.timestamp_list[4]:
            self.entry_custom_timestamp.configure(state="normal", fg_color=STYLE["ENTRY"], placeholder_text=(
                datetime.now().strftime("%B %d, %Y %I:%M:%S %p")))
            return
        elif choice == self.timestamp_list[0]:
            self.selected_timestamp = None
            return


if __name__ == "__main__":
    app = App()

    # App Icon
    iconpath = ImageTk.PhotoImage(file=resource_path("assets/genzai.png"))
    app.wm_iconbitmap()
    app.iconphoto(False, iconpath)

    app.mainloop()
