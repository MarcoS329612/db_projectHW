import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Usamos ttk para widgets modernos
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
        # Configuración inicial del grid para que sea responsive
        self.grid(row=0, column=0, sticky="nsew")  # El grid ocupará todo el espacio disponible
        self.columnconfigure(0, weight=1)  # La columna 0 se expandirá
        self.rowconfigure(0, weight=1)  # La fila 0 se expandirá

        # Título
        title_label = tk.Label(self, text="Inicio de Sesión", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, pady=20, sticky="n", padx=20)

        # Campo de email
        email_label = tk.Label(self, text="Email:")
        email_label.grid(row=1, column=0, padx=20, sticky="w")
        email_entry = ttk.Entry(self, textvariable=self.email_var)
        email_entry.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        # Campo de contraseña
        pass_label = tk.Label(self, text="Contraseña:")
        pass_label.grid(row=3, column=0, padx=20, sticky="w")
        pass_entry = ttk.Entry(self, textvariable=self.contraseña_var, show="*")
        pass_entry.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

        # Botones
        login_button = ttk.Button(self, text="Ingresar", command=self.login)
        login_button.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        register_button = ttk.Button(self, text="Registrarse", command=self.controller.mostrar_registro)
        register_button.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

        # Hacer que el campo de contraseña tenga un tamaño mínimo (opcional)
        pass_entry.bind("<Configure>", lambda e: self.set_minimum_size(pass_entry))

    def login(self):
        email = self.email_var.get()
        contraseña = self.contraseña_var.get()
        usuario = validar_usuario(email, contraseña)
        if usuario:
            self.controller.usuario_actual = Usuario.from_db_row(usuario)
            messagebox.showinfo("Éxito", f"Bienvenido, {self.controller.usuario_actual.nombre}")
            self.controller.mostrar_seleccion_pelicula()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def set_minimum_size(self, widget):
        # Configurar un tamaño mínimo para los widgets
        widget.config(width=30)

