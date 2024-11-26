# gui/movie_selection.py
import tkinter as tk
from app.database.queries import obtener_peliculas

class MovieSelection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.peliculas = []
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Seleccione una Película", font=("Helvetica", 16)).pack(pady=20)
        self.frame_peliculas = tk.Frame(self)
        self.frame_peliculas.pack()

        self.refresh()

    def refresh(self):
        # Limpiar los widgets existentes
        for widget in self.frame_peliculas.winfo_children():
            widget.destroy()

        # Obtener las películas y crear botones
        self.peliculas = obtener_peliculas()
        if self.peliculas:
            for pelicula in self.peliculas:
                tk.Button(
                    self.frame_peliculas,
                    text=pelicula['titulo'],  # Accediendo a 'titulo' usando la clave del diccionario
                    command=lambda p=pelicula: self.seleccionar_pelicula(p)
                ).pack(pady=5)
        else:
            tk.Label(self.frame_peliculas, text="No hay películas disponibles.").pack()

    def seleccionar_pelicula(self, pelicula):
        # Navegar a la selección de horarios
        self.controller.mostrar_seleccion_horario(pelicula)
