# app/models/funcion.py

class Funcion:
    def __init__(self, funcion_id, pelicula_id, sala_id, horario, pelicula_titulo, sala_tipo):
        self.funcion_id = funcion_id
        self.pelicula_id = pelicula_id
        self.sala_id = sala_id
        self.horario = horario
        self.pelicula_titulo = pelicula_titulo
        self.sala_tipo = sala_tipo

    @classmethod
    def from_db_row(cls, row):
        return cls(
            funcion_id=row.FuncionID,
            pelicula_id=row.PeliculaID,
            sala_id=row.SalaID,
            horario=row.Horario,
            pelicula_titulo=row.Titulo,
            sala_tipo=row.TipoSala
        )
