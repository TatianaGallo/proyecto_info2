import mysql.connector

class ConexionDB:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="trabajo_final"
        )
        self.cursor = self.conexion.cursor()

    def ejecutar_consulta(self, consulta, parametros=None):
        self.cursor.execute(consulta, parametros or ())
        return self.cursor

    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()
