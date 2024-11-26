# models/ticket.py

class Boleto:
    def __init__(self, id_boleto, id_usuario, id_horario, fecha_compra):
        self.id_boleto = id_boleto
        self.id_usuario = id_usuario
        self.id_horario = id_horario
        self.fecha_compra = fecha_compra

    @classmethod
    def from_db_row(cls, row):
        return cls(
            id_boleto=row['id_boleto'],
            id_usuario=row['id_usuario'],
            id_horario=row['id_horario'],
            fecha_compra=row['fecha_compra']
        )

    def __str__(self):
        return f"Boleto(id_boleto={self.id_boleto}, id_usuario={self.id_usuario}, id_horario={self.id_horario}, fecha_compra={self.fecha_compra})"
