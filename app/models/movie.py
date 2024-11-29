# app/models/movie.py

class Movie:
    def __init__(self, pelicula_id, titulo, clasificacion, duracion, genero, sinopsis=None, fecha_estreno=None):
        self.pelicula_id = pelicula_id
        self.titulo = titulo
        self.clasificacion = clasificacion
        self.duracion = duracion
        self.genero = genero
        self.sinopsis = sinopsis
        self.fecha_estreno = fecha_estreno

    @classmethod
    def from_db_row(cls, row):
        return cls(
            row.PeliculaID, row.Titulo, row.Clasificacion, row.Duracion, row.Genero,
            sinopsis=row.Sinopsis, fecha_estreno=row.FechaEstreno
        )
