# models/schedule.py
class Horario:
    def __init__(self, id_horario, id_pelicula, fecha_hora, sala):
        self.id_horario = id_horario
        self.id_pelicula = id_pelicula
        self.fecha_hora = fecha_hora
        self.sala = sala

    @classmethod
    def from_db_row(cls, row):
        return cls(
            id_horario=row['id_horario'],
            id_pelicula=row['id_pelicula'],
            fecha_hora=row['fecha_hora'],
            sala=row['sala']
        )

    def __str__(self):
        return f"Horario(id_horario={self.id_horario}, id_pelicula={self.id_pelicula}, fecha_hora={self.fecha_hora}, sala={self.sala})"
