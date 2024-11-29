# app/models/user.py

class User:
    def __init__(self, usuario_id, nombre, correo):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.correo = correo
