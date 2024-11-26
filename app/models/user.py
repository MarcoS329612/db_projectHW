# models/user.py

class Usuario:
    def __init__(self, id_usuario, nombre, email, contraseña):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    @classmethod
    def from_db_row(cls, row):
        return cls(
            id_usuario=row['id_usuario'],
            nombre=row['nombre'],
            email=row['email'],
            contraseña=row['contraseña']
        )

    def __str__(self):
        return f"Usuario({self.id_usuario}, {self.nombre}, {self.email})"
