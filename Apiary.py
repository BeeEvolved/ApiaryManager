import tkinter as tk
from tkinter import messagebox
import datetime
import pickle


class Hive:
    def __init__(self, name, location, notes, genetics):
        self.name = name
        self.location = location
        self.notes = notes
        self.genetics = genetics
        self.tasks = []


class Task:
    def __init__(self, name, date_added):
        self.name = name
        self.date_added = date_added
        self.is_completed = False
        self.completed_date = None


class ApiaryManager:
    def __init__(self):
        self.hives = []

    def add_hive(self, name, location, notes, genetics):
        new_hive = Hive(name, location, notes, genetics)
        self.hives.append(new_hive)

    def delete_hive(self, hive):
        self.hives.remove(hive)

    def update_hive(self, hive, name, location, notes, genetics):
        hive.name = name
        hive.location = location
        hive.notes = notes
        hive.genetics = genetics

    def add_task(self, hive, task_name):
        new_task = Task(task_name, datetime.datetime.now())
        hive.tasks.append(new_task)

    def mark_task_complete(self, task):
        task.is_completed = True
        task.completed_date = datetime.datetime.now()

    def sort_by_name(self):
        self.hives.sort(key=lambda hive: hive.name)

    def save_data(self, file_path):
        with open(file_path, "wb") as file:
            pickle.dump(self.hives, file)

    def load_data(self, file_path):
        try:
            with open(file_path, "rb") as file:
                self.hives = pickle.load(file)
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "No data file found. Starting with empty hive list.")


class App:
    def __init__(self):
        self.apiary_manager = ApiaryManager()

        self.root = tk.Tk()
        self.root.title("Apiary")
        self.root.configure(bg="black")

        self.hive_listbox = tk.Listbox(self.root, width=50, height=10, bg="black", fg="yellow", font=("Arial", 12))
        self.hive_listbox.pack()

        self.new_hive_frame = tk.Frame(self.root, bg="black")
        self.new_hive_frame.pack()

        self.new_hive_name_label = tk.Label(
            self.new_hive_frame, text="Hive Name:", bg="black", fg="yellow", font=("Arial", 12)
        )
        self.new_hive_name_label.grid(row=0, column=0, sticky="e")

        self.new_hive_name_entry = tk.Entry(
            self.new_hive_frame, width=40, bg="yellow", font=("Arial", 12)
        )
        self.new_hive_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.new_hive_location_label = tk.Label(
            self.new_hive_frame, text="Location:", bg="black", fg="yellow", font=("Arial", 12)
        )
        self.new_hive_location_label.grid(row=1, column=0, sticky="e")

        self.new_hive_location_entry = tk.Entry(
            self.new_hive_frame, width=40, bg="yellow", font=("Arial", 12)
        )
        self.new_hive_location_entry.grid(row=1, column=1, padx=10, pady=5)

        self.new_hive_genetics_label = tk.Label(
            self.new_hive_frame, text="Genetics:", bg="black", fg="yellow", font=("Arial", 12)
        )
        self.new_hive_genetics_label.grid(row=2, column=0, sticky="e")

        self.new_hive_genetics_entry = tk.Entry(
            self.new_hive_frame, width=40, bg="yellow", font=("Arial", 12)
        )
        self.new_hive_genetics_entry.grid(row=2, column=1, padx=10, pady=5)

        self.new_hive_notes_label = tk.Label(
            self.new_hive_frame, text="Notes:", bg="black", fg="yellow", font=("Arial", 12)
        )
        self.new_hive_notes_label.grid(row=3, column=0, sticky="ne")

        self.new_hive_notes_entry = tk.Text(
            self.new_hive_frame, width=30, height=8, bg="yellow", font=("Arial", 12)
        )
        self.new_hive_notes_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_hive_button = tk.Button(
            self.root, text="Add Hive", command=self.add_hive, bg="yellow", fg="black", font=("Arial", 12)
        )
        self.add_hive_button.pack(pady=10)

        self.hive_details_button = tk.Button(
            self.root,
            text="View Hive Details",
            command=self.view_hive_details,
            bg="yellow",
            fg="black",
            font=("Arial", 12),
        )
        self.hive_details_button.pack(pady=10)

        self.sort_button = tk.Button(
            self.root,
            text="Sort by Name",
            command=self.sort_hives_by_name,
            bg="yellow",
            fg="black",
            font=("Arial", 12),
        )
        self.sort_button.pack(pady=10)

        self.save_button = tk.Button(
            self.root,
            text="Save Data",
            command=self.save_data,
            bg="yellow",
            fg="black",
            font=("Arial", 12),
        )
        self.save_button.pack(pady=10)

        self.load_button = tk.Button(
            self.root,
            text="Load Data",
            command=self.load_data,
            bg="yellow",
            fg="black",
            font=("Arial", 12),
        )
        self.load_button.pack(pady=10)

        self.root.mainloop()

    def add_hive(self):
        name = self.new_hive_name_entry.get()
        location = self.new_hive_location_entry.get()
        genetics = self.new_hive_genetics_entry.get()
        notes = self.new_hive_notes_entry.get("1.0", tk.END)
        self.apiary_manager.add_hive(name, location, notes, genetics)
        self.refresh_hive_list()

    def view_hive_details(self):
        selected_index = self.hive_listbox.curselection()
        if selected_index:
            selected_hive = self.apiary_manager.hives[selected_index[0]]
            HiveDetailsWindow(selected_hive, self.apiary_manager)
        else:
            messagebox.showinfo("Error", "No hive selected.")

    def sort_hives_by_name(self):
        self.apiary_manager.sort_by_name()
        self.refresh_hive_list()

    def save_data(self):
        file_path = "apiary_data.pkl"
        self.apiary_manager.save_data(file_path)
        messagebox.showinfo("Save Successful", "Apiary data saved successfully.")

    def load_data(self):
        file_path = "apiary_data.pkl"
        self.apiary_manager.load_data(file_path)
        self.refresh_hive_list()
        messagebox.showinfo("Load Successful", "Apiary data loaded successfully.")

    def refresh_hive_list(self):
        self.hive_listbox.delete(0, tk.END)
        for hive in self.apiary_manager.hives:
            self.hive_listbox.insert(tk.END, hive.name)


class HiveDetailsWindow(tk.Toplevel):
    def __init__(self, hive, apiary_manager):
        super().__init__()
        self.hive = hive
        self.apiary_manager = apiary_manager

        self.title("Apiary - Hive Details")
        self.configure(bg="black")

        self.name_label = tk.Label(self, text="Name:", bg="black", fg="yellow", font=("Arial", 12))
        self.name_label.pack()
        self.name_entry = tk.Entry(self, width=40, bg="yellow", font=("Arial", 12))
        self.name_entry.insert(tk.END, self.hive.name)
        self.name_entry.pack()

        self.location_label = tk.Label(self, text="Location:", bg="black", fg="yellow", font=("Arial", 12))
        self.location_label.pack()
        self.location_entry = tk.Entry(self, width=40, bg="yellow", font=("Arial", 12))
        self.location_entry.insert(tk.END, self.hive.location)
        self.location_entry.pack()

        self.genetics_label = tk.Label(self, text="Genetics:", bg="black", fg="yellow", font=("Arial", 12))
        self.genetics_label.pack()
        self.genetics_entry = tk.Entry(self, width=40, bg="yellow", font=("Arial", 12))
        self.genetics_entry.insert(tk.END, self.hive.genetics)
        self.genetics_entry.pack()

        self.notes_label = tk.Label(self, text="Notes:", bg="black", fg="yellow", font=("Arial", 12))
        self.notes_label.pack()
        self.notes_text = tk.Text(self, width=30, height=10, bg="yellow", font=("Arial", 12))
        self.notes_text.insert(tk.END, self.hive.notes)
        self.notes_text.pack()

        self.add_task_label = tk.Label(self, text="Add Task:", bg="black", fg="yellow", font=("Arial", 12))
        self.add_task_label.pack()
        self.task_name_entry = tk.Entry(self, width=40, bg="yellow", font=("Arial", 12))
        self.task_name_entry.pack()
        self.add_task_button = tk.Button(self, text="Add", command=self.add_task, bg="yellow", fg="black", font=("Arial", 12))
        self.add_task_button.pack()

        self.tasks_label = tk.Label(self, text="Tasks:", bg="black", fg="yellow", font=("Arial", 12))
        self.tasks_label.pack()

        self.task_listbox = tk.Listbox(self, width=50, height=10, bg="yellow", fg="black", font=("Arial", 12))
        self.task_listbox.pack()

        self.mark_complete_button = tk.Button(
            self, text="Mark Complete", command=self.mark_task_complete, bg="yellow", fg="black", font=("Arial", 12)
        )
        self.mark_complete_button.pack()

        self.update_button = tk.Button(
            self, text="Update Hive", command=self.update_hive, bg="yellow", fg="black", font=("Arial", 12)
        )
        self.update_button.pack()

        self.delete_button = tk.Button(
            self, text="Delete Hive", command=self.delete_hive, bg="yellow", fg="black", font=("Arial", 12)
        )
        self.delete_button.pack()

        self.load_tasks()

    def add_task(self):
        task_name = self.task_name_entry.get()
        if task_name:
            self.apiary_manager.add_task(self.hive, task_name)
            self.load_tasks()
            self.task_name_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Error", "Task name cannot be empty.")

    def mark_task_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.hive.tasks[selected_index[0]]
            self.apiary_manager.mark_task_complete(selected_task)
            self.load_tasks()
        else:
            messagebox.showinfo("Error", "No task selected.")

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.hive.tasks:
            task_text = task.name + " (Added: " + str(task.date_added) + ")"
            if task.is_completed:
                task_text += " - Completed: " + str(task.completed_date)
            self.task_listbox.insert(tk.END, task_text)

    def update_hive(self):
        name = self.name_entry.get()
        location = self.location_entry.get()
        genetics = self.genetics_entry.get()
        notes = self.notes_text.get("1.0", tk.END)
        self.apiary_manager.update_hive(self.hive, name, location, notes, genetics)
        self.destroy()

    def delete_hive(self):
        result = messagebox.askyesno(
            "Confirm Delete", "Are you sure you want to delete this hive?\nThis action cannot be undone."
        )
        if result == tk.YES:
            self.apiary_manager.delete_hive(self.hive)
            self.destroy()


app = App()
