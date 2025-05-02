import tkinter as tk
from tkinter import messagebox
import subprocess
import os

class DeliveryPlannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Delivery Route Planner")
        self.nodes = []
        self.positions = []
        self.planner_exe_path = "C:\\Users\\kharo\\desktop\\sem project\\sample_project\\planner.exe"

        # Verify planner.exe exists
        if not os.path.exists(self.planner_exe_path):
            messagebox.showerror("Error", f"planner.exe not found at {self.planner_exe_path}. Please ensure it exists and update the path in interface.py.")
            raise FileNotFoundError(f"planner.exe not found at {self.planner_exe_path}")

        # Set a larger default font for all widgets
        self.default_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")

        # Map selection frame
        map_frame = tk.Frame(root)
        map_frame.pack(pady=10)
        tk.Label(map_frame, text="Select Map:", font=self.default_font).pack()
        self.map_var = tk.StringVar(value="1")
        tk.Radiobutton(map_frame, text="Rajpur Town", variable=self.map_var, value="1", font=self.default_font).pack(anchor="w")
        tk.Radiobutton(map_frame, text="Clock Tower Area", variable=self.map_var, value="2", font=self.default_font).pack(anchor="w")
        tk.Button(map_frame, text="Show Map", command=self.show_map, font=self.button_font, width=15).pack(pady=5)

        # Canvas for map
        self.canvas = tk.Canvas(root, width=400, height=300, bg="white", borderwidth=2, relief="groove")
        self.canvas.pack(pady=10)

        # Start and end selection frame
        location_frame = tk.Frame(root)
        location_frame.pack(pady=10)
        
        tk.Label(location_frame, text="Start Location:", font=self.default_font).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.start_var = tk.StringVar()
        self.start_menu = tk.OptionMenu(location_frame, self.start_var, "")
        self.start_menu.config(font=self.default_font, width=15)
        self.start_menu.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(location_frame, text="End Location:", font=self.default_font).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.end_var = tk.StringVar()
        self.end_menu = tk.OptionMenu(location_frame, self.end_var, "")
        self.end_menu.config(font=self.default_font, width=15)
        self.end_menu.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(location_frame, text="Find Route", command=self.find_route, font=self.button_font, width=15).grid(row=2, column=0, columnspan=2, pady=10)

        # Result display
        self.result_label = tk.Label(root, text="", wraplength=350, font=self.default_font)
        self.result_label.pack(pady=10)

        # Save record frame
        save_frame = tk.Frame(root)
        save_frame.pack(pady=10)
        tk.Label(save_frame, text="Description:", font=self.default_font).pack()
        self.desc_entry = tk.Entry(save_frame, font=self.default_font, width=30)
        self.desc_entry.pack(pady=5)
        tk.Button(save_frame, text="Save Record", command=self.save_record, font=self.button_font, width=15).pack(pady=5)

        # View records button
        tk.Button(root, text="View Records", command=self.view_records, font=self.button_font, width=15).pack(pady=10)

    def show_map(self):
        self.canvas.delete("all")
        map_id = int(self.map_var.get())

        # Define node names based on map_id (matching graph.c)
        if map_id == 1:  # Rajpur Town
            self.nodes = ["Market", "School", "Hospital", "Park", "Temple", 
                         "Station", "Library", "Cafe", "Plaza", "Post Office"]
        else:  # Clock Tower Area
            self.nodes = ["Clock Tower", "Bank", "Gym", "Mall", "Church", 
                         "Bus Stop", "Clinic", "Bakery", "Garden", "Hotel"]

        # Get node positions
        self.positions = [[0, 0] for _ in range(10)]
        if map_id == 1:
            self.positions = [[50, 50], [150, 50], [250, 50], [50, 150], [150, 150],
                              [250, 150], [50, 250], [150, 250], [250, 250], [350, 250]]
        else:
            self.positions = [[50, 50], [150, 50], [250, 50], [50, 150], [150, 150],
                              [250, 150], [50, 250], [150, 250], [250, 250], [350, 250]]

        # Draw nodes
        for i, (x, y) in enumerate(self.positions):
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="lightblue")
            self.canvas.create_text(x, y+20, text=self.nodes[i], font=("Arial", 10))

        # Draw edges
        edges = [(0,1,5), (1,2,3), (0,3,4), (1,4,7), (2,5,6), (3,4,8), (4,5,5), (3,6,9), (5,8,4), (6,7,6), (7,8,3), (6,9,7)] if map_id == 1 else \
                [(0,1,6), (1,2,4), (0,3,5), (1,4,8), (2,5,7), (3,4,9), (4,5,3), (3,6,6), (5,8,5), (6,7,4), (7,8,3), (6,9,8)]
        
        print("Drawing edges:", edges)
        
        for u, v, w in edges:
            x1, y1 = self.positions[u]
            x2, y2 = self.positions[v]
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            offset = 10 if x1 == x2 else 0
            offset = -10 if y1 == y2 else offset
            self.canvas.create_text(mid_x + offset, mid_y + offset, text=str(w), font=("Arial", 8), fill="blue")

        # Update dropdowns
        menu_start = self.start_menu["menu"]
        menu_end = self.end_menu["menu"]
        menu_start.delete(0, "end")
        menu_end.delete(0, "end")
        
        for node in self.nodes:
            menu_start.add_command(label=node, command=lambda value=node: self.start_var.set(value))
            menu_end.add_command(label=node, command=lambda value=node: self.end_var.set(value))
        
        self.start_var.set(self.nodes[0] if self.nodes else "")
        self.end_var.set(self.nodes[1] if len(self.nodes) > 1 else "")
        
        self.start_menu.update()
        self.end_menu.update()

    def find_route(self):
        map_id = int(self.map_var.get())
        start = self.nodes.index(self.start_var.get()) if self.start_var.get() in self.nodes else -1
        end = self.nodes.index(self.end_var.get()) if self.end_var.get() in self.nodes else -1
        if start == -1 or end == -1:
            messagebox.showerror("Error", "Invalid start or end location")
            return

        try:
            result = subprocess.run([self.planner_exe_path, "find", str(map_id), str(start), str(end)], capture_output=True, text=True)
            print("find_route command result:", result)
            if result.returncode != 0:
                raise Exception(f"planner.exe find failed: {result.stderr}")
            lines = result.stdout.splitlines()
            if len(lines) < 2:
                messagebox.showerror("Error", "Failed to find route")
                return
            path, distance = lines[0], lines[1]
            self.result_label.config(text=f"Path: {path}\nDistance: {distance}")
            self.canvas.delete("path")
            path_nodes = [self.nodes.index(n) for n in path.split(" -> ")]
            for i in range(len(path_nodes)-1):
                u, v = path_nodes[i], path_nodes[i+1]
                x1, y1 = self.positions[u]
                x2, y2 = self.positions[v]
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2, tags="path")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to find route: {str(e)}")

    def save_record(self):
        map_id = int(self.map_var.get())
        map_name = "Rajpur Town" if map_id == 1 else "Clock Tower Area"
        desc = self.desc_entry.get()
        if not desc:
            messagebox.showerror("Error", "Description is required")
            return
        try:
            result = subprocess.run([self.planner_exe_path, "find", str(map_id), str(self.nodes.index(self.start_var.get())),
                                    str(self.nodes.index(self.end_var.get()))], capture_output=True, text=True)
            print("save_record find command result:", result)
            if result.returncode != 0:
                raise Exception(f"planner.exe find failed: {result.stderr}")
            lines = result.stdout.splitlines()
            if len(lines) < 2:
                messagebox.showerror("Error", "Failed to save route")
                return
            path, distance = lines[0], lines[1]
            save_command = [self.planner_exe_path, "save", map_name, path, distance, desc]
            print("Saving record with command:", save_command)
            result = subprocess.run(save_command)
            print("Save result:", result.returncode)
            if result.returncode == 0:
                messagebox.showinfo("Success", "Record saved")
            else:
                messagebox.showerror("Error", "Failed to save record")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save record: {str(e)}")

    def view_records(self):
        print("Entering view_records method")
        try:
            result = subprocess.run([self.planner_exe_path, "read"], capture_output=True, text=True)
            print("subprocess.run result:", result)
            if result.returncode != 0:
                raise Exception(f"planner.exe read failed: {result.stderr}")
            records = result.stdout
            print("Records from planner.exe:", records)
            win = tk.Toplevel(self.root)
            print("Toplevel window created")
            win.title("Delivery Records")

            # Create a frame to hold the Listbox and Scrollbar
            frame = tk.Frame(win)
            frame.pack(padx=10, pady=10, fill="both", expand=True)

            # Create the Scrollbar
            scrollbar = tk.Scrollbar(frame, orient="vertical")
            scrollbar.pack(side="right", fill="y")

            # Create the Listbox with a scrollbar
            listbox = tk.Listbox(frame, width=80, height=20, font=("Arial", 12), yscrollcommand=scrollbar.set)
            listbox.pack(side="left", fill="both", expand=True)

            # Link the Scrollbar to the Listbox
            scrollbar.config(command=listbox.yview)

            print("Listbox and Scrollbar created")
            if not records.strip():
                listbox.insert(tk.END, "No records found.")
                print("No records found")
            else:
                for line in records.splitlines():
                    if line.strip():
                        listbox.insert(tk.END, line)
                        print("Inserted record:", line)
            win.update()
            print("Toplevel window updated")
        except Exception as e:
            print("Error in view_records:", str(e))
            messagebox.showerror("Error", f"Failed to view records: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DeliveryPlannerGUI(root)
    root.mainloop()