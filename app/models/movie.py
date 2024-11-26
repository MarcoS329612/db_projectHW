# main.py
import tkinter as tk
from app.gui.login import Login
from app.gui.register import Register
from app.gui.movie_selection import MovieSelection
from app.gui.schedule_selection import ScheduleSelection
from app.gui.ticket_confirmation import TicketConfirmation

class CineApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CineApp")
        self.geometry("800x600")
        self.resizable(False, False)
        self.usuario_actual = None
        self.mostrar_login()

    def mostrar_login(self):
        self.limpiar_ventana()
        login = Login(self, self)
        login.pack()

    def mostrar_registro(self):
        self.limpiar_ventana()
        registro = Register(self, self)
        registro.pack()

    def mostrar_seleccion_pelicula(self):
        self.limpiar_ventana()
        seleccion = MovieSelection(self, self)
        seleccion.pack()

    def mostrar_seleccion_horario(self, pelicula):
        self.limpiar_ventana()
        horario = ScheduleSelection(self, self, pelicula)
        horario.pack()

    def mostrar_confirmacion(self, boleto):
        self.limpiar_ventana()
        confirmacion = TicketConfirmation(self, self, boleto)
        confirmacion.pack()

    def limpiar_ventana(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = CineApp()
    app.mainloop()
