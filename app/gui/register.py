# gui/register.py
import tkinter as tk
from tkinter import messagebox
from app.database.queries import registrar_usuario
import re

class Register(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.nombre_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.contraseña_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Registro de Usuario", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self, text="Nombre:").pack()
        tk.Entry(self, textvariable=self.nombre_var).pack()

        tk.Label(self, text="Email:").pack()
        tk.Entry(self, textvariable=self.email_var).pack()

        tk.Label(self, text="Contraseña:").pack()
        tk.Entry(self, textvariable=self.contraseña_var, show="*").pack()

        tk.Button(self, text="Registrarse", command=self.registrar).pack(pady=10)
        tk.Button(self, text="Volver", command=self.controller.mostrar_login).pack()

    def registrar(self):
        nombre = self.nombre_var.get().strip()
        email = self.email_var.get().strip()
        contraseña = self.contraseña_var.get().strip()

        # Verificar si todos los campos están llenos
        if not nombre or not email or not contraseña:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        # Verificar formato del email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showwarning("Advertencia", "Ingrese un email válido")
            return

        # Verificar longitud y complejidad de la contraseña
        if len(contraseña) < 6:
            messagebox.showwarning("Advertencia", "La contraseña debe tener al menos 6 caracteres")
            return

        if registrar_usuario(nombre, email, contraseña):
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            self.controller.mostrar_login()
        else:
            messagebox.showerror("Error", "El email ya está registrado")
