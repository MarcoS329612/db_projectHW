# app/gui/movie_management.py

import tkinter as tk
from tkinter import messagebox
from app.database import queries
from app.models.movie import Movie
from app.gui.add_edit_movie import AddEditMovieWindow

class MovieManagementWindow:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title("Administrar Películas")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.movies = self.load_movies()

        self.movie_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.populate_movie_list()
        self.movie_listbox.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.frame, text="Agregar Película", command=self.add_movie)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.frame, text="Editar Película", command=self.edit_movie)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.frame, text="Eliminar Película", command=self.delete_movie)
        self.delete_button.pack(pady=5)

        self.back_button = tk.Button(self.frame, text="Volver", command=self.go_back)
        self.back_button.pack(pady=5)

    def load_movies(self):
        movie_rows = queries.get_movies()
        return [Movie.from_db_row(row) for row in movie_rows]

    def populate_movie_list(self):
        self.movie_listbox.delete(0, tk.END)
        for movie in self.movies:
            self.movie_listbox.insert(tk.END, f"{movie.titulo} - {movie.genero}")

    def add_movie(self):
        def refresh_movies():
            self.movies = self.load_movies()
            self.populate_movie_list()

        AddEditMovieWindow(self.root, refresh_movies)

    def edit_movie(self):
        selected_index = self.movie_listbox.curselection()
        if selected_index:
            selected_movie = self.movies[selected_index[0]]

            def refresh_movies():
                self.movies = self.load_movies()
                self.populate_movie_list()

            AddEditMovieWindow(self.root, refresh_movies, movie=selected_movie)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una película para editar")

    def delete_movie(self):
        selected_index = self.movie_listbox.curselection()
        if selected_index:
            selected_movie = self.movies[selected_index[0]]
            confirm = messagebox.askyesno(
                "Confirmar",
                f"'{selected_movie.titulo}' tiene funciones asociadas. ¿Desea eliminar la película y todas sus funciones y boletos asociados?"
            )
            if confirm:
                success, error_message = queries.delete_movie_and_related(selected_movie.pelicula_id)
                if success:
                    messagebox.showinfo("Éxito", "Película y registros asociados eliminados")
                    self.movies.pop(selected_index[0])
                    self.populate_movie_list()
                else:
                    messagebox.showerror("Error", error_message)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una película para eliminar")

    def go_back(self):
        self.root.destroy()
        from app.gui.movie_selection import MovieSelectionWindow
        root = tk.Tk()
        app = MovieSelectionWindow(root, self.user)
        root.mainloop()
