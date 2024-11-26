# gui/ticket_confirmation.py
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
        self.label_confirmacion = tk.Label(self, text="", font=("Helvetica", 16))
        self.label_confirmacion.pack(pady=20)

        tk.Button(self, text="Confirmar Compra", command=self.confirmar_compra).pack(pady=10)
        tk.Button(self, text="Cancelar", command=self.controller.mostrar_seleccion_pelicula).pack()

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
