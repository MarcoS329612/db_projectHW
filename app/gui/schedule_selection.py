# gui/schedule_selection.py

import tkinter as tk
from app.database import queries
from app.gui.ticket_confirmation import TicketConfirmationWindow


class ScheduleSelectionWindow:
    def __init__(self, root, user, movie):
        self.root = root
        self.user = user
        self.movie = movie
        self.root.title("Selección de Horario")
        self.root.geometry('800x600')

        self.schedules = queries.get_schedules(movie.pelicula_id)

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.schedule_listbox = tk.Listbox(self.frame, width=50, height=15)
        for schedule in self.schedules:
            self.schedule_listbox.insert(tk.END, f"{schedule.Horario} - {schedule.TipoSala}")
        self.schedule_listbox.pack(side=tk.LEFT)

        self.select_button = tk.Button(self.frame, text="Seleccionar", command=self.select_schedule)
        self.select_button.pack(pady=10)

        self.manage_funciones_button = tk.Button(self.frame, text="Administrar Funciones", command=self.manage_funciones)
        self.manage_funciones_button.pack(pady=5)
            
        self.back_button = tk.Button(self.frame, text="Volver", command=self.go_back)
        self.back_button.pack(pady=10)  # Cambiado a pack()

    def select_schedule(self):
        selected_index = self.schedule_listbox.curselection()
        if selected_index:
            selected_schedule = self.schedules[selected_index[0]]
            self.root.destroy()
            root = tk.Tk()
            app = TicketConfirmationWindow(root, self.user, self.movie, selected_schedule)
            root.mainloop()
        else:
            tk.messagebox.showwarning("Advertencia", "Seleccione un horario")

    def manage_funciones(self):
        self.root.destroy()
        from app.gui.funcion_management import FuncionManagementWindow  # Importar dentro del método
        root = tk.Tk()
        app = FuncionManagementWindow(root, self.user)
        root.mainloop()

    def go_back(self):
        self.root.destroy()
        from app.gui.movie_selection import MovieSelectionWindow  # Importar dentro del método
        root = tk.Tk()
        app = MovieSelectionWindow(root, self.user)
        root.mainloop()
