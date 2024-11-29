# app/gui/register.py

import tkinter as tk
from tkinter import messagebox
from app.database import queries

class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro")
        self.root.geometry('800x600')

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Nombre:").grid(row=0, column=0, sticky='e')
        tk.Label(self.frame, text="Correo:").grid(row=1, column=0, sticky='e')
        tk.Label(self.frame, text="Contraseña:").grid(row=2, column=0, sticky='e')

        self.name_entry = tk.Entry(self.frame)
        self.email_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame, show="*")

        self.name_entry.grid(row=0, column=1)
        self.email_entry.grid(row=1, column=1)
        self.password_entry.grid(row=2, column=1)

        self.register_button = tk.Button(self.frame, text="Registrarse", command=self.register)
        self.register_button.grid(row=3, column=0, pady=10)

        self.back_button = tk.Button(self.frame, text="Volver", command=self.go_back)
        self.back_button.grid(row=3, column=1)

# app/gui/register.py

    def register(self):
        nombre = self.name_entry.get()
        correo = self.email_entry.get()
        contrasena = self.password_entry.get()

        try:
            if queries.register_user(nombre, correo, contrasena):
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                self.go_back()
            else:
                messagebox.showerror("Error", "No se pudo registrar el usuario")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during registration: {e}")
            print(f"Registration error: {e}")

    def go_back(self):
        self.root.destroy()
        from app.gui.login import LoginWindow  # Moved import here
        root = tk.Tk()
        app = LoginWindow(root)
        root.mainloop()