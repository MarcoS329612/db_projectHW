# database/queries.py
from app.database.connection import get_connection
# app/database/queries.py

def get_movies():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT PeliculaID, Titulo, Clasificacion, Duracion, Genero, Sinopsis, FechaEstreno
        FROM Peliculas
    """)
    movies = cursor.fetchall()
    conn.close()
    return movies

def get_schedules(pelicula_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Funciones.FuncionID, Funciones.Horario, Funciones.PeliculaID, Funciones.SalaID, Salas.TipoSala
        FROM Funciones
        JOIN Salas ON Funciones.SalaID = Salas.SalaID
        WHERE Funciones.PeliculaID = ?
    """, pelicula_id)
    schedules = cursor.fetchall()
    conn.close()
    return schedules


def authenticate_user(correo, contrasena):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT UsuarioID, Nombre, Correo FROM Usuarios
        WHERE Correo = ? AND Contraseña = ?
    """, correo, contrasena)
    user = cursor.fetchone()
    conn.close()
    return user

def register_user(nombre, correo, contrasena):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Usuarios (Nombre, Correo, Contraseña)
            VALUES (?, ?, ?)
        """, nombre, correo, contrasena)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error registering user: {e}")
        return False
    finally:
        conn.close()

def purchase_ticket(usuario_id, funcion_id, total_price, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Verificar boletos disponibles
        available_tickets = get_available_tickets(funcion_id)
        if quantity > available_tickets:
            print("No hay asientos disponibles")
            return False

        # Proceder con la compra
        for _ in range(quantity):
            cursor.execute("""
                INSERT INTO Boletos (UsuarioID, FuncionID, Precio)
                VALUES (?, ?, ?)
            """, usuario_id, funcion_id, total_price / quantity)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error purchasing tickets: {e}")
        return False
    finally:
        conn.close()


def add_movie(titulo, clasificacion, duracion, sinopsis, fecha_estreno, genero):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Peliculas (Titulo, Clasificacion, Duracion, Sinopsis, FechaEstreno, Genero)
            VALUES (?, ?, ?, ?, ?, ?)
        """, titulo, clasificacion, duracion, sinopsis, fecha_estreno, genero)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding movie: {e}")
        return False
    finally:
        conn.close()

def update_movie(pelicula_id, titulo, clasificacion, duracion, sinopsis, fecha_estreno, genero):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE Peliculas
            SET Titulo = ?, Clasificacion = ?, Duracion = ?, Sinopsis = ?, FechaEstreno = ?, Genero = ?
            WHERE PeliculaID = ?
        """, titulo, clasificacion, duracion, sinopsis, fecha_estreno, genero, pelicula_id)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating movie: {e}")
        return False
    finally:
        conn.close()
# In app/database/queries.py

def delete_movie(pelicula_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Check for related functions
        cursor.execute("""
            SELECT COUNT(*) AS FunctionCount
            FROM Funciones
            WHERE PeliculaID = ?
        """, pelicula_id)
        function_count = cursor.fetchone().FunctionCount

        if function_count > 0:
            # Inform the caller that deletion cannot proceed
            return False, "La película tiene funciones asociadas y no se puede eliminar."

        # Proceed to delete the movie
        cursor.execute("""
            DELETE FROM Peliculas WHERE PeliculaID = ?
        """, pelicula_id)
        conn.commit()
        return True, None
    except Exception as e:
        print(f"Error deleting movie: {e}")
        return False, str(e)
    finally:
        conn.close()

# app/database/queries.py

def get_funciones():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Funciones.FuncionID, Funciones.Horario, Peliculas.PeliculaID, Peliculas.Titulo,
               Salas.SalaID, Salas.TipoSala
        FROM Funciones
        JOIN Peliculas ON Funciones.PeliculaID = Peliculas.PeliculaID
        JOIN Salas ON Funciones.SalaID = Salas.SalaID
    """)
    funciones = cursor.fetchall()
    conn.close()
    return funciones

def add_funcion(pelicula_id, sala_id, horario):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Funciones (PeliculaID, SalaID, Horario)
            VALUES (?, ?, ?)
        """, pelicula_id, sala_id, horario)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding funcion: {e}")
        return False
    finally:
        conn.close()

def update_funcion(funcion_id, pelicula_id, sala_id, horario):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE Funciones
            SET PeliculaID = ?, SalaID = ?, Horario = ?
            WHERE FuncionID = ?
        """, pelicula_id, sala_id, horario, funcion_id)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating funcion: {e}")
        return False
    finally:
        conn.close()

def delete_funcion(funcion_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Check for related tickets
        cursor.execute("""
            SELECT COUNT(*) AS TicketCount
            FROM Boletos
            WHERE FuncionID = ?
        """, funcion_id)
        ticket_count = cursor.fetchone().TicketCount

        if ticket_count > 0:
            # Inform the caller that deletion cannot proceed
            return False, "La función tiene boletos vendidos y no se puede eliminar."

        # Proceed to delete the function
        cursor.execute("""
            DELETE FROM Funciones WHERE FuncionID = ?
        """, funcion_id)
        conn.commit()
        return True, None
    except Exception as e:
        print(f"Error deleting funcion: {e}")
        return False, str(e)
    finally:
        conn.close()

def get_salas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SalaID, Capacidad, TipoSala
        FROM Salas
    """)
    salas = cursor.fetchall()
    conn.close()
    return salas

def get_sala_price(sala_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT Precio FROM Salas WHERE SalaID = ?
        """, sala_id)
        row = cursor.fetchone()
        if row:
            return row.Precio
        else:
            return 0.0
    except Exception as e:
        print(f"Error fetching sala price: {e}")
        return 0.0
    finally:
        conn.close()

def purchase_ticket(usuario_id, funcion_id, total_price, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        for _ in range(quantity):
            cursor.execute("""
                INSERT INTO Boletos (UsuarioID, FuncionID, Precio)
                VALUES (?, ?, ?)
            """, usuario_id, funcion_id, total_price / quantity)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error purchasing tickets: {e}")
        return False
    finally:
        conn.close()

def get_available_tickets(funcion_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Obtener la capacidad total de la sala
        cursor.execute("""
            SELECT Salas.Capacidad
            FROM Funciones
            JOIN Salas ON Funciones.SalaID = Salas.SalaID
            WHERE Funciones.FuncionID = ?
        """, funcion_id)
        capacity_row = cursor.fetchone()
        capacity = capacity_row.Capacidad if capacity_row else 0

        # Obtener el número de boletos vendidos
        cursor.execute("""
            SELECT COUNT(*) AS SoldTickets
            FROM Boletos
            WHERE FuncionID = ?
        """, funcion_id)
        sold_tickets_row = cursor.fetchone()
        sold_tickets = sold_tickets_row.SoldTickets if sold_tickets_row else 0

        # Calcular boletos disponibles
        available_tickets = capacity - sold_tickets
        return max(available_tickets, 0)
    except Exception as e:
        print(f"Error fetching available tickets: {e}")
        return 0
    finally:
        conn.close()

# In app/database/queries.py

def delete_movie_and_related(pelicula_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Delete tickets associated with functions of the movie
        cursor.execute("""
            DELETE Boletos FROM Boletos
            JOIN Funciones ON Boletos.FuncionID = Funciones.FuncionID
            WHERE Funciones.PeliculaID = ?
        """, pelicula_id)

        # Delete functions associated with the movie
        cursor.execute("""
            DELETE FROM Funciones WHERE PeliculaID = ?
        """, pelicula_id)

        # Delete the movie
        cursor.execute("""
            DELETE FROM Peliculas WHERE PeliculaID = ?
        """, pelicula_id)
        conn.commit()
        return True, None
    except Exception as e:
        print(f"Error deleting movie and related records: {e}")
        return False, str(e)
    finally:
        conn.close()
