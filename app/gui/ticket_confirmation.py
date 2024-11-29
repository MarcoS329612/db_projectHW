import tkinter as tk
from tkinter import messagebox
from app.database import queries

class TicketConfirmationWindow:
    def __init__(self, root, user, movie, schedule):
        self.root = root
        self.user = user
        self.movie = movie
        self.schedule = schedule
        self.root.title("Confirmación de Boletos")
        self.root.geometry('800x600')

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        # Fetch the Sala price
        self.sala_price = queries.get_sala_price(schedule.SalaID)

        # Fetch available tickets
        self.available_tickets = queries.get_available_tickets(schedule.FuncionID)

        # Labels and Inputs
        info = (
            f"Película: {movie.titulo}\n"
            f"Horario: {schedule.Horario}\n"
            f"Sala: {schedule.TipoSala}\n"
            f"Precio por boleto: ${self.sala_price:.2f}\n"
            f"Boletos disponibles: {self.available_tickets}"
        )
        tk.Label(self.frame, text=info).grid(row=0, column=0, columnspan=2)

        tk.Label(self.frame, text="Cantidad de boletos:").grid(row=1, column=0, sticky='e')
        self.ticket_quantity_entry = tk.Entry(self.frame)
        self.ticket_quantity_entry.insert(0, "1")  # Default to 1 ticket
        self.ticket_quantity_entry.grid(row=1, column=1)

        # Total Price Label
        self.total_price_label = tk.Label(self.frame, text=f"Precio total: ${self.sala_price:.2f}")
        self.total_price_label.grid(row=2, column=0, columnspan=2)

        # Update total price when quantity changes
        self.ticket_quantity_entry.bind("<KeyRelease>", self.update_total_price)

        self.confirm_button = tk.Button(self.frame, text="Confirmar Compra", command=self.confirm_purchase)
        self.confirm_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.back_button = tk.Button(self.frame, text="Volver", command=self.go_back)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=10)

    def update_total_price(self, event=None):
        try:
            quantity = int(self.ticket_quantity_entry.get())
            if quantity < 1 or quantity > self.available_tickets:
                raise ValueError
            total_price = self.sala_price * quantity
            self.total_price_label.config(text=f"Precio total: ${total_price:.2f}")
            self.confirm_button.config(state=tk.NORMAL)
        except ValueError:
            self.total_price_label.config(text="Precio total: ---")
            self.confirm_button.config(state=tk.DISABLED)

    def confirm_purchase(self):
        try:
            quantity = int(self.ticket_quantity_entry.get())
            if quantity < 1:
                raise ValueError("La cantidad debe ser al menos 1")
            if quantity > self.available_tickets:
                raise ValueError("La cantidad supera los boletos disponibles")

            total_price = self.sala_price * quantity
            # Process the purchase
            success = queries.purchase_ticket(self.user.usuario_id, self.schedule.FuncionID, total_price, quantity)
            if success:
                messagebox.showinfo("Éxito", "Compra realizada correctamente")
                self.root.destroy()
                from app.gui.movie_selection import MovieSelectionWindow
                root = tk.Tk()
                app = MovieSelectionWindow(root, self.user)
                root.mainloop()            
            else:
                messagebox.showerror("Error", "No se pudo completar la compra")
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    def go_back(self):
        self.root.destroy()
        from app.gui.schedule_selection import ScheduleSelectionWindow  # Importar dentro del método
        root = tk.Tk()
        app = ScheduleSelectionWindow(root, self.user, self.movie)
        root.mainloop()
