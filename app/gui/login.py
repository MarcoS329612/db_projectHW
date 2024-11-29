# app/gui/login.py
import tkinter as tk
from tkinter import messagebox
from app.database import queries
from app.models.user import User
from app.gui.movie_selection import MovieSelectionWindow

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry('800x600')

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        tk.Label(self.frame, text="Correo:").grid(row=0, column=0, sticky='e')
        tk.Label(self.frame, text="Contraseña:").grid(row=1, column=0, sticky='e')

        self.email_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.email_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.frame, text="Ingresar", command=self.login)
        self.login_button.grid(row=2, column=0, pady=10)

        self.register_button = tk.Button(self.frame, text="Registrarse", command=self.open_register)
        self.register_button.grid(row=2, column=1)

    def login(self):
        correo = self.email_entry.get()
        contrasena = self.password_entry.get()
        try:
            user_data = queries.authenticate_user(correo, contrasena)
            if user_data:
                user = User(user_data.UsuarioID, user_data.Nombre, user_data.Correo)
                self.root.destroy()
                root = tk.Tk()
                app = MovieSelectionWindow(root, user)
                root.mainloop()
            else:
                messagebox.showerror("Error", "Credenciales inválidas")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during login: {e}")
            print(f"Login error: {e}")


    def open_register(self):
        self.root.destroy()
        from app.gui.register import RegisterWindow  # Import inside function
        root = tk.Tk()
        app = RegisterWindow(root)
        root.mainloop()