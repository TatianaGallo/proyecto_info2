from modelo.usuarios_modelo import ModeloUsuarios
from modelo.medicos_modelo import ModeloMedicos
from modelo.pacientes_modelo import ModeloPacientes

class ControladorUsuarios:
    def __init__(self):
        self.modelo_usuarios = ModeloUsuarios()
        self.modelo_medicos = ModeloMedicos()
        self.modelo_pacientes = ModeloPacientes()

    def registrar_usuario(self, nombre, email, contraseña, rol):
        # Verificar si los campos obligatorios no están vacíos
        if not nombre or not email or not contraseña:
            raise ValueError("Todos los campos son obligatorios")

        # Registrar en la tabla Usuarios
        id_usuario = self.modelo_usuarios.crear_usuario(nombre, email, contraseña, rol)

        # Después de registrar el usuario, insertar en la tabla correspondiente según el rol
        if rol == 'medico':
            # Registrar al médico en la tabla Medicos
            self.modelo_medicos.agregar_medico(id_usuario, nombre, email, contraseña)
        elif rol == 'paciente':
            # Registrar al paciente en la tabla Pacientes
            self.modelo_pacientes.agregar_paciente(id_usuario, nombre, email, contraseña)

    def iniciar_sesion(self, email, contraseña, rol):
        # Verificar el inicio de sesión según el rol
        if rol == 'medico':
            usuario = self.modelo_medicos.iniciar_sesion_medico(email, contraseña)
        elif rol == 'paciente':
            usuario = self.modelo_pacientes.iniciar_sesion_paciente(email, contraseña)

        if usuario:
            return usuario  # El usuario se encuentra y puede iniciar sesión
        else:
            raise ValueError("Correo electrónico o contraseña incorrectos")
        
        if not usuario:
            raise ValueError("Usuario o contraseña incorrectos")
        
        return usuario

