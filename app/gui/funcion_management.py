import tkinter as tk
from tkinter import messagebox
from app.database import queries
from app.models.funcion import Funcion
from app.gui.add_edit_funcion import AddEditFuncionWindow

class FuncionManagementWindow:
    def __init__(self, root, user, movie=None):  # Agregamos movie si es necesario
        self.root = root
        self.user = user
        self.movie = movie  # Solo si necesitas regresar a ScheduleSelectionWindow
        self.root.title("Administrar Funciones")
        self.root.geometry('800x600')

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.funciones = self.load_funciones()

        self.funcion_listbox = tk.Listbox(self.frame, width=70, height=15)
        self.populate_funcion_list()
        self.funcion_listbox.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.frame, text="Agregar Función", command=self.add_funcion)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.frame, text="Editar Función", command=self.edit_funcion)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.frame, text="Eliminar Función", command=self.delete_funcion)
        self.delete_button.pack(pady=5)

        # Add "Volver" button
        self.back_button = tk.Button(self.frame, text="Volver", command=self.go_back)
        self.back_button.pack(pady=5)

    def load_funciones(self):
        funcion_rows = queries.get_funciones()
        return [Funcion.from_db_row(row) for row in funcion_rows]

    def populate_funcion_list(self):
        self.funcion_listbox.delete(0, tk.END)
        for funcion in self.funciones:
            display_text = f"ID: {funcion.funcion_id}, Película: {funcion.pelicula_titulo}, Sala: {funcion.sala_tipo}, Horario: {funcion.horario}"
            self.funcion_listbox.insert(tk.END, display_text)

    def add_funcion(self):
        def refresh_funciones():
            self.funciones = self.load_funciones()
            self.populate_funcion_list()

        AddEditFuncionWindow(self.root, refresh_funciones)

    def edit_funcion(self):
        selected_index = self.funcion_listbox.curselection()
        if selected_index:
            selected_funcion = self.funciones[selected_index[0]]

            def refresh_funciones():
                self.funciones = self.load_funciones()
                self.populate_funcion_list()

            AddEditFuncionWindow(self.root, refresh_funciones, funcion=selected_funcion)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una función para editar")

    def delete_funcion(self):
        selected_index = self.funcion_listbox.curselection()
        if selected_index:
            selected_funcion = self.funciones[selected_index[0]]
            confirm = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la función '{selected_funcion.funcion_id}'?")
            if confirm:
                success, error_message = queries.delete_funcion(selected_funcion.funcion_id)
                if success:
                    messagebox.showinfo("Éxito", "Función eliminada")
                    self.funciones.pop(selected_index[0])
                    self.populate_funcion_list()
                else:
                    messagebox.showerror("Error", error_message)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una función para eliminar")

    def go_back(self):
        self.root.destroy()
        from app.gui.schedule_selection import ScheduleSelectionWindow  # Import inside function to avoid circular import
        root = tk.Tk()
        if self.movie:
            app = ScheduleSelectionWindow(root, self.user, self.movie)
        else:
            from app.gui.movie_selection import MovieSelectionWindow
            app = MovieSelectionWindow(root, self.user)
        root.mainloop()
