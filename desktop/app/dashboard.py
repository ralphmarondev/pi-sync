from functools import partial

import customtkinter as ctk
import requests

from constants import BASE_URL


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.frame_width = 75
        self.frame_padding = 20
        self.default_container_width = (self.frame_width + self.frame_padding) * 2 + 40

        self.grid_container = ctk.CTkFrame(self, width=self.default_container_width)
        self.grid_container.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        self.grid_container.grid_propagate(False)

        self.door_data = []
        self.door_widgets = {}

        self.fetch_and_create_door_grid()
        self.update_door_states()

    def fetch_and_create_door_grid(self):
        url = f'{BASE_URL}doors/'
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.door_data = response.json()
            print(f"Fetched {len(self.door_data)} doors")  # ✅ DEBUG
            self.create_door_grid()
        except Exception as e:
            print(f'Error fetching door data: {e}')

    def create_door_grid(self):
        if not self.door_data:
            print("No door data to display.")
            return

        for index, door in enumerate(self.door_data):
            col = index % 2
            row = index // 2

            border_color = "green" if door["is_open"] else "red"
            print(f"Creating door '{door['name']}' with status {door['is_open']} ({border_color})")  # ✅ DEBUG

            outer_frame = ctk.CTkFrame(
                self.grid_container,
                corner_radius=10,
                border_width=2,
                border_color=border_color,
                fg_color="transparent",
                bg_color='transparent'
            )
            outer_frame.grid(row=row, column=col, padx=10, pady=10, sticky="n")
            outer_frame.configure(width=self.frame_width, height=self.frame_width)
            outer_frame.grid_propagate(False)

            inner_frame = ctk.CTkFrame(outer_frame, fg_color="transparent")
            inner_frame.pack(expand=True, fill="both", padx=10, pady=10)

            label = ctk.CTkLabel(
                inner_frame,
                text=f"{door['name']}\n{'Open' if door['is_open'] else 'Closed'}",
                font=("Arial", 14),
                width=self.frame_width,
                height=self.frame_width
            )
            label.pack(expand=True)

            # Bind click to toggle
            for widget in (outer_frame, inner_frame, label):
                widget.bind("<Button-1>", partial(self.on_door_click, door["id"]))

            self.door_widgets[door["id"]] = {
                "frame": outer_frame,
                "label": label,
                "data": door
            }

    def on_door_click(self, door_id, event=None):
        print(f"Door {door_id} clicked.")

        door_widget = self.door_widgets.get(door_id)
        if not door_widget:
            print(f"No widget found for door {door_id}")
            return

        door_data = door_widget["data"]
        current_state = door_data["is_open"]
        action = "close" if current_state else "open"
        url = f"{BASE_URL}door/{action}/{door_id}/"

        try:
            response = requests.post(url)
            response.raise_for_status()
            result = response.json()

            if result.get("success"):
                # Update state and UI
                door_data["is_open"] = result["is_open"]
                new_status = "Open" if result["is_open"] else "Closed"
                new_color = "green" if result["is_open"] else "red"

                door_widget["label"].configure(text=f"{door_data['name']}\n{new_status}")
                door_widget["frame"].configure(border_color=new_color)

                print(f"Door {door_id} successfully {action}ed.")
            else:
                print(f"Failed to {action} door {door_id}: {result.get('message')}")

        except requests.RequestException as e:
            print(f"Error trying to {action} door {door_id}: {e}")

    def update_door_states(self):
        url = f'{BASE_URL}doors/'
        try:
            response = requests.get(url)
            response.raise_for_status()
            new_data = response.json()

            for new_door in new_data:
                door_id = new_door["id"]
                if door_id in self.door_widgets:
                    door_widget = self.door_widgets[door_id]
                    current_data = door_widget["data"]

                    # Update only if state changed
                    if current_data["is_open"] != new_door["is_open"]:
                        current_data["is_open"] = new_door["is_open"]
                        new_status = "Open" if new_door["is_open"] else "Closed"
                        new_color = "green" if new_door["is_open"] else "red"

                        door_widget["label"].configure(text=f"{new_door['name']}\n{new_status}")
                        door_widget["frame"].configure(border_color=new_color)
                        print(f"Auto-updated door {new_door['name']} to {new_status}")

        except requests.RequestException as e:
            print(f"Auto-refresh failed: {e}")

        # Keep the loop going every 3 seconds
        self.after(3000, self.update_door_states)
