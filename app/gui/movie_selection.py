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
        
        # Usamos un Frame que se organizará con grid
        self.frame_peliculas = tk.Frame(self)
        self.frame_peliculas.pack(fill="both", expand=True, padx=20, pady=10)

        # Configurar la responsividad
        self.frame_peliculas.columnconfigure(0, weight=1, uniform="equal")  # Columna que se ajustará

        # Llamamos a refresh para cargar las películas
        self.refresh()

    def refresh(self):
        # Limpiar los widgets existentes
        for widget in self.frame_peliculas.winfo_children():
            widget.destroy()

        # Obtener las películas y crear botones
        self.peliculas = obtener_peliculas()

        if self.peliculas:
            # Usamos grid para distribuir las películas en un diseño de varias columnas
            for index, pelicula in enumerate(self.peliculas):
                # Determinar la fila y columna donde colocar el botón
                row = index // 2  # Dos botones por fila
                col = index % 2   # Alternar entre las dos columnas

                tk.Button(
                    self.frame_peliculas,
                    text=pelicula['titulo'],  # Accediendo al título de la película
                    command=lambda p=pelicula: self.seleccionar_pelicula(p),
                    width=20, height=2  # Definir tamaño fijo de los botones
                ).grid(row=row, column=col, padx=10, pady=10, sticky="ew")

        else:
            tk.Label(self.frame_peliculas, text="No hay películas disponibles.").pack()

    def seleccionar_pelicula(self, pelicula):
        # Navegar a la selección de horarios
        self.controller.mostrar_seleccion_horario(pelicula)
