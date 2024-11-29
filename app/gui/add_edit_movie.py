import tkinter as tk
from tkinter import messagebox
from app.database import queries
from app.models.movie import Movie

class AddEditMovieWindow:
    def __init__(self, parent, refresh_callback, movie=None):
        self.parent = parent
        self.refresh_callback = refresh_callback
        self.movie = movie

        self.window = tk.Toplevel(self.parent)
        self.window.title("Agregar Película" if movie is None else "Editar Película")
        self.window.geometry('800x600')  # Cambiado self.root a self.window

        self.frame = tk.Frame(self.window)  # Eliminadas las comillas
        self.frame.pack(padx=20, pady=20)   # Eliminadas las comillas

        # Labels and Entries
        labels = ["Título:", "Clasificación:", "Duración (min):", "Sinopsis:", "Fecha de Estreno (YYYY-MM-DD):", "Género:"]
        self.entries = []

        for i, label_text in enumerate(labels):
            tk.Label(self.frame, text=label_text).grid(row=i, column=0, sticky='e')
            entry = tk.Entry(self.frame)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        # Pre-fill data if editing
        if self.movie:
            self.entries[0].insert(0, self.movie.titulo)
            self.entries[1].insert(0, self.movie.clasificacion)
            self.entries[2].insert(0, str(self.movie.duracion))
            self.entries[3].insert(0, self.movie.sinopsis or "")
            self.entries[4].insert(0, str(self.movie.fecha_estreno) if self.movie.fecha_estreno else "")
            self.entries[5].insert(0, self.movie.genero or "")

        # Buttons
        action_text = "Agregar" if movie is None else "Actualizar"
        self.action_button = tk.Button(self.frame, text=action_text, command=self.save_movie)
        self.action_button.grid(row=len(labels), column=0, pady=10)

        self.cancel_button = tk.Button(self.frame, text="Cancelar", command=self.window.destroy)
        self.cancel_button.grid(row=len(labels), column=1)

    def save_movie(self):
        titulo = self.entries[0].get()
        clasificacion = self.entries[1].get()
        duracion = self.entries[2].get()
        sinopsis = self.entries[3].get()
        fecha_estreno = self.entries[4].get()
        genero = self.entries[5].get()

        # Basic validation
        if not titulo or not clasificacion or not duracion:
            messagebox.showwarning("Advertencia", "Título, Clasificación y Duración son obligatorios")
            return

        try:
            duracion = int(duracion)
        except ValueError:
            messagebox.showwarning("Advertencia", "Duración debe ser un número entero")
            return

        if self.movie:
            # Update existing movie
            success = queries.update_movie(
                self.movie.pelicula_id, titulo, clasificacion, duracion, sinopsis, fecha_estreno, genero
            )
            if success:
                messagebox.showinfo("Éxito", "Película actualizada")
                self.refresh_callback()
                self.window.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar la película")
        else:
            # Add new movie
            success = queries.add_movie(
                titulo, clasificacion, duracion, sinopsis, fecha_estreno, genero
            )
            if success:
                messagebox.showinfo("Éxito", "Película agregada")
                self.refresh_callback()
                self.window.destroy()
            else:
                messagebox.showerror("Error", "No se pudo agregar la película")
