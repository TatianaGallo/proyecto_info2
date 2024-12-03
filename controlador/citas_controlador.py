from modelo.citas_modelo import ModeloCitas
from modelo.pacientes_modelo import ModeloPacientes

class ControladorCitas:
    def __init__(self):
        self.modelo = ModeloCitas()
        self.modelo_pacientes = ModeloPacientes()

    def agregar_cita(self, id_paciente, fecha, hora, descripcion):
        # Obtener el id_usuario correspondiente al id_paciente
        id_usuario = self.modelo_pacientes.obtener_paciente_por_id(id_paciente)
        
        if id_usuario:
            # Agregar la cita con el id_usuario, no el id_paciente
            self.modelo.agregar_cita(id_usuario, fecha, hora, descripcion)
        else:
            print("Paciente no encontrado.")

    def obtener_citas_paciente(self, id_paciente):
        # Obtén el id_usuario del paciente
        paciente = self.modelo_pacientes.obtener_paciente_por_id(id_paciente)
        if paciente:
            id_usuario = paciente['id_usuario']
            return self.modelo.obtener_citas_paciente(id_usuario)
        return []

