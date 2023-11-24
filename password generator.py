#password generator
#task 3


import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Password Length:", font=("Arial", 14, "bold italic")).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.length_entry = ttk.Entry(self.root, width=10, font=("Arial", 14, "bold italic"), justify="center")
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.length_entry.insert(0, "Type Here")
        self.length_entry.bind("<FocusIn>", lambda e: self.length_entry.delete(0, tk.END))
        self.length_entry.bind("<FocusOut>", lambda e: self.length_entry.insert(0, "Type Here") if not self.length_entry.get() else None)

        ttk.Style().configure('TButton', font=("Arial", 14, "bold italic"), padding=(10, 5), background='#FFA500', foreground='black')

        ttk.Button(self.root, text="Generate Password", command=self.generate_password, style='TButton', width=20).grid(row=1, column=0, columnspan=2, pady=20)
        
        # Display Generated Password
        self.password_display = ttk.Entry(self.root, state="readonly", font=("Arial", 18, "bold italic"), width=25)
        self.password_display.grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Button(self.root, text="Clear", command=self.clear_fields, style='TButton', width=20).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.destroy, style='TButton', width=20).grid(row=4, column=0, columnspan=2, pady=10)

        for child in self.root.winfo_children():
            child.grid_configure(padx=20)
        
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            if password_length <= 0:
                raise ValueError("Password length must be greater than 0.")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(password_length))

            # Update the existing password_display widget
            self.password_display.config(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state="readonly")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        self.length_entry.delete(0, tk.END)
        self.password_display.config(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()
