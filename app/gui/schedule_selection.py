# gui/schedule_selection.py
import tkinter as tk
from app.database.queries import obtener_horarios_por_pelicula

class ScheduleSelection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pelicula = None
        self.horarios = []
        self.create_widgets()

    def create_widgets(self):
        self.label_titulo = tk.Label(self, text="", font=("Helvetica", 16))
        self.label_titulo.pack(pady=20)

        self.frame_horarios = tk.Frame(self)
        self.frame_horarios.pack()

    def set_pelicula(self, pelicula):
        self.pelicula = pelicula
        self.label_titulo.config(text=f"Horarios para {self.pelicula['titulo']}")
        self.refresh()

    def refresh(self):
        # Limpiar los widgets existentes
        for widget in self.frame_horarios.winfo_children():
            widget.destroy()

        # Obtener los horarios de la película seleccionada
        self.horarios = obtener_horarios_por_pelicula(self.pelicula['id_pelicula'])
        if self.horarios:
            for horario in self.horarios:
                texto_horario = f"{horario['fecha_hora']} - Sala {horario['sala']}"
                tk.Button(
                    self.frame_horarios,
                    text=texto_horario,
                    command=lambda h=horario: self.seleccionar_horario(h)
                ).pack(pady=5)
        else:
            tk.Label(self.frame_horarios, text="No hay horarios disponibles.").pack()

    def seleccionar_horario(self, horario):
        # Aquí iría la lógica para comprar el boleto
        self.controller.mostrar_confirmacion(horario)
