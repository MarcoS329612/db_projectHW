import pyodbc

def get_connection():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 18 for SQL Server};'
            'SERVER=DELL-LATITUDE-M;'
            'DATABASE=CineDB;'
            'TrustServerCertificate=yes;'
            'Trusted_Connection=yes;'
        )
        return connection
    except pyodbc.Error as e:
        print("Error en la conexión:", e)
        return None
