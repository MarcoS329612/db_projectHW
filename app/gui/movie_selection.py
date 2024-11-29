# gui/movie_selection.py

import tkinter as tk
from app.database import queries
from app.models.movie import Movie
from app.gui.schedule_selection import ScheduleSelectionWindow
from app.gui.movie_management import MovieManagementWindow

class MovieSelectionWindow:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title("Selección de Película")
        self.root.geometry('800x600')

        self.movies = [Movie.from_db_row(row) for row in queries.get_movies()]

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.movie_listbox = tk.Listbox(self.frame, width=50, height=15)
        for movie in self.movies:
            self.movie_listbox.insert(tk.END, f"{movie.titulo} - {movie.genero}")
        self.movie_listbox.pack(side=tk.LEFT)

        self.select_button = tk.Button(self.frame, text="Seleccionar", command=self.select_movie)
        self.select_button.pack(pady=10)

        # Remove admin check to allow all users to manage movies
        self.manage_button = tk.Button(self.frame, text="Administrar Películas", command=self.manage_movies)
        self.manage_button.pack(pady=5)


    def manage_movies(self):
        self.root.destroy()
        root = tk.Tk()
        app = MovieManagementWindow(root, self.user)
        root.mainloop()

    def select_movie(self):
        selected_index = self.movie_listbox.curselection()
        if selected_index:
            selected_movie = self.movies[selected_index[0]]
            self.root.destroy()
            root = tk.Tk()
            app = ScheduleSelectionWindow(root, self.user, selected_movie)
            root.mainloop()

