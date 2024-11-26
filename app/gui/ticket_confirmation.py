import tkinter as tk
from tkinter import messagebox
from app.database.queries import comprar_boleto

class TicketConfirmation(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.horario = None
        self.create_widgets()

    def create_widgets(self):
        # Título de confirmación
        self.label_confirmacion = tk.Label(self, text="", font=("Helvetica", 16))
        self.label_confirmacion.grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="w")

        tk.Button(self, text="Confirmar Compra", command=self.confirmar_compra).grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        tk.Button(self, text="Cancelar", command=self.controller.mostrar_seleccion_pelicula).grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        # Aseguramos que las columnas se expandan
        self.grid_columnconfigure(0, weight=1, uniform="equal")
        self.grid_columnconfigure(1, weight=1, uniform="equal")

    def set_boleto(self, horario):
        self.horario = horario
        texto = f"Confirmar compra para:\n{self.horario['fecha_hora']} - Sala {self.horario['sala']}"
        self.label_confirmacion.config(text=texto)

    def confirmar_compra(self):
        if comprar_boleto(self.controller.usuario_actual.id_usuario, self.horario['id_horario']):
            messagebox.showinfo("Éxito", "Boleto comprado correctamente")
            self.controller.mostrar_seleccion_pelicula()
        else:
            messagebox.showerror("Error", "No se pudo completar la compra")
