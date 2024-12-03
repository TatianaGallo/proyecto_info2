from modelo.pacientes_modelo import ModeloPacientes

class ControladorPacientes:
    def __init__(self):
        self.modelo = ModeloPacientes()

    def agregar_paciente(self, id_usuario, nombre, email, contraseña):
        self.modelo.agregar_paciente(id_usuario, nombre, email, contraseña)

    def obtener_pacientes(self):
        return self.modelo.obtener_pacientes()


