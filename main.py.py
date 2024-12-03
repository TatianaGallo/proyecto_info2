import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from vista.login import Ui_MainWindow  # Convertido desde .ui
from controlador.usuarios_controlador import ControladorUsuarios
from controlador.citas_controlador import ControladorCitas  # Importamos el controlador de citas
from PyQt5.QtWidgets import QDialog
from vista.citas import Ui_Dialog  # Suponiendo que tienes el archivo .ui convertido a .py
from PyQt5 import QtCore, QtGui, QtWidgets


class LoginVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controlador_usuarios = ControladorUsuarios()
        self.controlador_citas = ControladorCitas()  

        self.ui.pushButton_iniciarSesion.clicked.connect(self.iniciar_sesion)
        self.ui.pushButton_registrar.clicked.connect(self.registrar_usuario)

        

    def iniciar_sesion(self):
        email = self.ui.lineEdit_email.text()
        contraseña = self.ui.lineEdit_contrasena.text()
        rol = "paciente" if self.ui.radioButton_paciente.isChecked() else "medico"
        try:
            usuario = self.controlador_usuarios.iniciar_sesion(email, contraseña, rol)
            QMessageBox.information(self, "Éxito", f"Bienvenido {usuario[1]}")
            
            id_paciente = usuario[0]
            self.abrir_ventana_citas(id_paciente)
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
            
    def abrir_ventana_citas(self, id_paciente):
        ventana_citas = VentanaCitas(id_paciente)
        ventana_citas.exec_()

    def registrar_usuario(self):
        nombre = self.ui.lineEdit_nombre.text()
        email = self.ui.lineEdit_email.text()
        contraseña = self.ui.lineEdit_contrasena.text()
        rol = "paciente" if self.ui.radioButton_paciente.isChecked() else "medico"
        try:
            self.controlador_usuarios.registrar_usuario(nombre, email, contraseña, rol)
            QMessageBox.information(self, "Éxito", "Usuario registrado exitosamente")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
            

            
    



class VentanaCitas(QDialog):
    def __init__(self, id_paciente):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.id_paciente = id_paciente
        
        self.controlador_citas = ControladorCitas()

       
        self.ui.fecha_cita.setDate(QtCore.QDate.currentDate())  # Fecha actual por defecto
        self.ui.tiempo_cita.setTime(QtCore.QTime.currentTime())  # Hora actual por defecto

        # Conectamos el botón de guardar cita a la función correspondiente
        self.ui.pushButton_guardar_cita.clicked.connect(self.guardar_cita)

    def guardar_cita(self):
        fecha = self.ui.fecha_cita.date().toString("yyyy-MM-dd")
        hora = self.ui.tiempo_cita.time().toString("HH:mm")
        descripcion = self.ui.texto_descripcion.toPlainText()

        try:
            # Llamamos al controlador para guardar la cita
            self.controlador_citas.agregar_cita(self.id_paciente, fecha, hora, descripcion)
            QMessageBox.information(self, "Éxito", "Cita guardada exitosamente")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = LoginVentana()
    ventana.show()
    sys.exit(app.exec_())


