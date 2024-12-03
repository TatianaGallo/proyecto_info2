from modelo.conexion import ConexionDB

class ModeloPacientes:
    def __init__(self):
        self.db = ConexionDB()

    def agregar_paciente(self, id_usuario, nombre, email, contraseña):
        consulta = "INSERT INTO Pacientes (id_usuario, nombre, email, contraseña) VALUES (%s, %s, %s, %s)"
        self.db.ejecutar_consulta(consulta, (id_usuario, nombre, email, contraseña))
        self.db.commit()

    def obtener_pacientes(self):
        consulta = "SELECT * FROM Pacientes"
        return self.db.ejecutar_consulta(consulta).fetchall()

 

    # Método para iniciar sesión de paciente
    def iniciar_sesion_paciente(self, email, contraseña):
        consulta = "SELECT * FROM Pacientes WHERE email = %s AND contraseña = %s"
        paciente = self.db.ejecutar_consulta(consulta, (email, contraseña)).fetchone()

        if paciente:
            return paciente  # Devuelve la información del paciente si es válido
        else:
            return None  # Retorna None si no se encuentra el paciente
        
    def obtener_paciente_por_id(self, id_paciente):
        consulta = "SELECT * FROM Pacientes WHERE id_usuario = %s"
        paciente = self.db.ejecutar_consulta(consulta, (id_paciente,)).fetchone()
        
        if paciente:
            return paciente[4]
        return None

