import tkinter as tk
from tkinter import ttk, messagebox

class CyclistRegistrationApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Cyclist Registration")
        self.cyclists = []

        # Create GUI widgets
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(column=0, row=0)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(column=1, row=0)

        self.surname_label = tk.Label(root, text="Surname:")
        self.surname_label.grid(column=0, row=1)

        self.surname_entry = tk.Entry(root)
        self.surname_entry.grid(column=1, row=1)

        self.gender_label = tk.Label(root, text="Gender:")
        self.gender_label.grid(column=0, row=2)

        self.gender_var = tk.StringVar()
        self.gender_combo = ttk.Combobox(root, textvariable=self.gender_var)
        self.gender_combo['values'] = ('Male', 'Female', 'Other')
        self.gender_combo.grid(column=1, row=2)

        self.add_button = tk.Button(root, text="Add Cyclist", command=self.add_cyclist)
        self.add_button.grid(column=1, row=3)

        self.edit_button = tk.Button(root, text="Edit Cyclist", command=self.edit_cyclist)
        self.edit_button.grid(column=1, row=4)

        self.delete_button = tk.Button(root, text="Delete Cyclist", command=self.delete_cyclist)
        self.delete_button.grid(column=1, row=5)

        self.list_label = tk.Label(root, text="Registered Cyclists:")
        self.list_label.grid(column=0, row=6)

        self.cyclist_list = tk.Text(root, height=10, width=40)
        self.cyclist_list.grid(column=0, row=7, columnspan=2)

    def add_cyclist(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        gender = self.gender_var.get()

        if name and surname and gender:
            self.cyclists.append((name, surname, gender))
            self.update_list()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def edit_cyclist(self):
        try:
            index = self.cyclist_list.get('1.0', tk.END).split('\n').index(
                f"{self.name_entry.get()} {self.surname_entry.get()} ({self.gender_var.get()})"
            ) - 1
            self.cyclists[index] = (self.name_entry.get(), self.surname_entry.get(), self.gender_var.get())
            self.update_list()
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Cyclist not found.")

    def delete_cyclist(self):
        try:
            index = self.cyclist_list.get('1.0', tk.END).split('\n').index(
                f"{self.name_entry.get()} {self.surname_entry.get()} ({self.gender_var.get()})"
            ) - 1
            del self.cyclists[index]
            self.update_list()
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Cyclist not found.")

    def update_list(self):
        self.cyclist_list.delete('1.0', tk.END)
        for cyclist in self.cyclists:
            self.cyclist_list.insert(tk.END, f"{cyclist[0]} {cyclist[1]} ({cyclist[2]})\n")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.gender_var.set('')

if "_name_ "== "_main_":
    root = tk.Tk()
    app = CyclistRegistrationApp(root)
    root.mainloop()