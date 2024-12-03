from modelo.conexion import ConexionDB

class ModeloCitas:
    def __init__(self):
        self.db = ConexionDB()

    def agregar_cita(self, id_usuario, fecha, hora, descripcion):
        consulta = "INSERT INTO Citas (id_paciente, fecha, hora, descripcion) VALUES (%s, %s, %s, %s)"
        self.db.ejecutar_consulta(consulta, (id_usuario, fecha, hora, descripcion))
        self.db.commit()

    def obtener_citas_paciente(self, id_usuario):
        consulta = "SELECT * FROM Citas WHERE id_paciente = %s"
        return self.db.ejecutar_consulta(consulta, (id_usuario,)).fetchall()
