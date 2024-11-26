# gui/login.py
import tkinter as tk
from tkinter import messagebox
from app.database.queries import validar_usuario
from app.models.user import Usuario

class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.email_var = tk.StringVar()
        self.contraseña_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Inicio de Sesión", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self, text="Email:").pack()
        tk.Entry(self, textvariable=self.email_var).pack()

        tk.Label(self, text="Contraseña:").pack()
        tk.Entry(self, textvariable=self.contraseña_var, show="*").pack()

        tk.Button(self, text="Ingresar", command=self.login).pack(pady=10)
        tk.Button(self, text="Registrarse", command=self.controller.mostrar_registro).pack()

    def login(self):
        email = self.email_var.get()
        contraseña = self.contraseña_var.get()
        usuario = validar_usuario(email, contraseña)
        if usuario:
            # `usuario` ahora es un diccionario, podemos crear la instancia de Usuario directamente
            self.controller.usuario_actual = Usuario.from_db_row(usuario)
            messagebox.showinfo("Éxito", f"Bienvenido, {self.controller.usuario_actual.nombre}")
            self.controller.mostrar_seleccion_pelicula()
        else:
            messagebox.showerror("Error", "Email o contraseña incorrectos")
