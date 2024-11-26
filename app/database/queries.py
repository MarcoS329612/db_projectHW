from app.database.connection import get_connection
from app.models.schedule import Horario
import datetime

def obtener_usuario_por_email(email):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row:
            columns = [column[0] for column in cursor.description]
            usuario = dict(zip(columns, row))
            conn.close()
            return usuario
        else:
            conn.close()
            return None
    else:
        return None

def registrar_usuario(nombre, email, contraseña):
    if obtener_usuario_por_email(email):
        # El usuario ya existe
        return False
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuarios (nombre, email, contraseña) VALUES (?, ?, ?)",
            (nombre, email, contraseña)
        )
        conn.commit()
        conn.close()
        return True
    else:
        return False

def validar_usuario(email, contraseña):
    usuario = obtener_usuario_por_email(email)
    if usuario and usuario['contraseña'] == contraseña:
        return usuario
    else:
        return None

def obtener_horarios_por_pelicula(id_pelicula):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Horarios WHERE id_pelicula = ? ORDER BY fecha_hora",
            (id_pelicula,)
        )
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        conn.close()

        horarios = [dict(zip(columns, row)) for row in rows]
        return horarios
    else:
        return []

def comprar_boleto(id_usuario, id_horario):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Boletos (id_usuario, id_horario, fecha_compra) VALUES (?, ?, ?)",
            (id_usuario, id_horario, datetime.datetime.now())
        )
        conn.commit()
        conn.close()
        return True
    else:
        return False

def obtener_peliculas(id_pelicula=None):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        if id_pelicula is not None:
            cursor.execute(
                "SELECT * FROM Peliculas WHERE id_pelicula = ? ORDER BY titulo",
                (id_pelicula,)
            )
        else:
            cursor.execute("SELECT * FROM Peliculas ORDER BY titulo")

        columns = [column[0] for column in cursor.description]  
        rows = cursor.fetchall()
        conn.close()

        peliculas = [dict(zip(columns, row)) for row in rows]
        return peliculas
    else:
        return []
