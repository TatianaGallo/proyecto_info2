from modelo.conexion import ConexionDB

class ModeloUsuarios:
    def __init__(self):
        self.db = ConexionDB()

    def crear_usuario(self, nombre, email, contraseña, rol):
        consulta = "INSERT INTO Usuarios (nombre, email, contraseña, rol) VALUES (%s, %s, %s, %s)"
        self.db.ejecutar_consulta(consulta, (nombre, email, contraseña, rol))
        self.db.commit()
        
        # Obtener el id generado en la columna 'id' (campo AUTO_INCREMENT)
        id_usuario = self.db.cursor.lastrowid
        return id_usuario  # Devolver el id generado

    def leer_usuario(self, email, contraseña):
        consulta = "SELECT * FROM Usuarios WHERE email = %s AND contraseña = %s"
        return self.db.ejecutar_consulta(consulta, (email, contraseña)).fetchone()
