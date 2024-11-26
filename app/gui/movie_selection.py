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
        self.frame_peliculas.pack(fill="both", expand=True, padx=20, pady=10)

        self.frame_peliculas.columnconfigure(0, weight=1, uniform="equal")  

        self.refresh()

    def refresh(self):
        for widget in self.frame_peliculas.winfo_children():
            widget.destroy()

        self.peliculas = obtener_peliculas()

        if self.peliculas:
            for index, pelicula in enumerate(self.peliculas):
                row = index // 2  # Dos botones por fila
                col = index % 2   # Alternar entre las dos columnas

                tk.Button(
                    self.frame_peliculas,
                    text=pelicula['titulo'], 
                    command=lambda p=pelicula: self.seleccionar_pelicula(p),
                    width=20, height=2 
                ).grid(row=row, column=col, padx=10, pady=10, sticky="ew")

        else:
            tk.Label(self.frame_peliculas, text="No hay películas disponibles.").pack()

    def seleccionar_pelicula(self, pelicula):
        self.controller.mostrar_seleccion_horario(pelicula)
