# app/gui/add_edit_funcion.py

import tkinter as tk
from tkinter import messagebox
from app.database import queries

class AddEditFuncionWindow:
    def __init__(self, parent, refresh_callback, funcion=None):
        self.parent = parent
        self.refresh_callback = refresh_callback
        self.funcion = funcion

        self.window = tk.Toplevel(self.parent)
        self.window.title("Agregar Película" if funcion is None else "Editar Película")
        self.window.geometry('800x600')

        self.frame = tk.Frame(self.window)
        self.frame.pack(padx=20, pady=20)

        # Fetch movies and salas to populate dropdowns
        self.movies = queries.get_movies()
        self.salas = queries.get_salas()

        # Labels and Inputs
        tk.Label(self.frame, text="Película:").grid(row=0, column=0, sticky='e')
        tk.Label(self.frame, text="Sala:").grid(row=1, column=0, sticky='e')
        tk.Label(self.frame, text="Horario (YYYY-MM-DD HH:MM):").grid(row=2, column=0, sticky='e')

        self.movie_var = tk.StringVar()
        self.sala_var = tk.StringVar()
        self.horario_entry = tk.Entry(self.frame)

        # Movie Dropdown
        movie_options = [f"{movie.PeliculaID} - {movie.Titulo}" for movie in self.movies]
        self.movie_menu = tk.OptionMenu(self.frame, self.movie_var, *movie_options)
        self.movie_menu.grid(row=0, column=1)

        # Sala Dropdown
        sala_options = [f"{sala.SalaID} - {sala.TipoSala}" for sala in self.salas]
        self.sala_menu = tk.OptionMenu(self.frame, self.sala_var, *sala_options)
        self.sala_menu.grid(row=1, column=1)

        self.horario_entry.grid(row=2, column=1)

        # Pre-fill data if editing
        if self.funcion:
            self.movie_var.set(f"{self.funcion.pelicula_id} - {self.funcion.pelicula_titulo}")
            self.sala_var.set(f"{self.funcion.sala_id} - {self.funcion.sala_tipo}")
            self.horario_entry.insert(0, str(self.funcion.horario))

        # Buttons
        action_text = "Agregar" if funcion is None else "Actualizar"
        self.action_button = tk.Button(self.frame, text=action_text, command=self.save_funcion)
        self.action_button.grid(row=3, column=0, pady=10)

        self.cancel_button = tk.Button(self.frame, text="Cancelar", command=self.window.destroy)
        self.cancel_button.grid(row=3, column=1)

    def save_funcion(self):
        pelicula_selection = self.movie_var.get()
        sala_selection = self.sala_var.get()
        horario = self.horario_entry.get()

        if not pelicula_selection or not sala_selection or not horario:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        # Extract IDs from selection
        pelicula_id = int(pelicula_selection.split(' - ')[0])
        sala_id = int(sala_selection.split(' - ')[0])

        if self.funcion:
            # Update existing funcion
            success = queries.update_funcion(
                self.funcion.funcion_id, pelicula_id, sala_id, horario
            )
            if success:
                messagebox.showinfo("Éxito", "Función actualizada")
                self.refresh_callback()
                self.window.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar la función")
        else:
            # Add new funcion
            success = queries.add_funcion(
                pelicula_id, sala_id, horario
            )
            if success:
                messagebox.showinfo("Éxito", "Función agregada")
                self.refresh_callback()
                self.window.destroy()
            else:
                messagebox.showerror("Error", "No se pudo agregar la función")
