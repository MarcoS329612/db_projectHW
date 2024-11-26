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

        self.contenedor = tk.Frame(self)
        self.contenedor.pack(fill="both", expand=True)

        self.frames = {}
        for F in (Login, Register, MovieSelection, ScheduleSelection, TicketConfirmation):
            frame = F(parent=self.contenedor, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_login()

    def mostrar_frame(self, contenedor):
        frame = self.frames[contenedor]
        frame.tkraise()

    def mostrar_login(self):
        self.mostrar_frame(Login)

    def mostrar_registro(self):
        self.mostrar_frame(Register)

    def mostrar_seleccion_pelicula(self):
        self.frames[MovieSelection].refresh()
        self.mostrar_frame(MovieSelection)

    def mostrar_seleccion_horario(self, pelicula):
        self.frames[ScheduleSelection].set_pelicula(pelicula)
        self.mostrar_frame(ScheduleSelection)

    def mostrar_confirmacion(self, boleto):
        self.frames[TicketConfirmation].set_boleto(boleto)
        self.mostrar_frame(TicketConfirmation)

if __name__ == "__main__":
    app = CineApp()
    app.mainloop()
