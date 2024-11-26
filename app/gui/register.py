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
        # Título
        tk.Label(self, text="Registro de Usuario", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=20)

        # Campo Nombre
        tk.Label(self, text="Nombre:").grid(row=1, column=0, sticky="e", padx=10)
        tk.Entry(self, textvariable=self.nombre_var).grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Campo Email
        tk.Label(self, text="Email:").grid(row=2, column=0, sticky="e", padx=10)
        tk.Entry(self, textvariable=self.email_var).grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Campo Contraseña
        tk.Label(self, text="Contraseña:").grid(row=3, column=0, sticky="e", padx=10)
        tk.Entry(self, textvariable=self.contraseña_var, show="*").grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # Botones
        tk.Button(self, text="Registrarse", command=self.registrar).grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        tk.Button(self, text="Volver", command=self.controller.mostrar_login).grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # Configurar expansión de columnas
        self.grid_columnconfigure(1, weight=1)

    def registrar(self):
        nombre = self.nombre_var.get().strip()
        email = self.email_var.get().strip()
        contraseña = self.contraseña_var.get().strip()

        # Verificar si todos los campos están llenos
        if not nombre or not email or not contraseña:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        # Validar formato de email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showwarning("Advertencia", "Por favor ingresa un email válido.")
            return

        # Registrar usuario
        usuario_registrado = registrar_usuario(nombre, email, contraseña)
        if usuario_registrado:
            messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            self.controller.mostrar_login()
        else:
            messagebox.showerror("Error", "Hubo un problema al registrar el usuario.")
