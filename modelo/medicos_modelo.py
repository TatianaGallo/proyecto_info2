# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:17:35 2024

@author: tatia
"""

from modelo.conexion import ConexionDB

class ModeloMedicos:
    def __init__(self):
        
        self.db = ConexionDB()

    def agregar_medico(self, id_usuario, nombre, email, contraseña):
        # Inserta el médico en la tabla Medicos
        consulta = "INSERT INTO Medicos (id_usuario, nombre, email, contraseña) VALUES (%s, %s, %s, %s)"
        self.db.ejecutar_consulta(consulta, (id_usuario, nombre, email, contraseña))
        self.db.commit()

    def obtener_medicos(self):
        # Obtiene todos los médicos registrados en la tabla Medicos
        consulta = "SELECT * FROM Medicos"
        return self.db.ejecutar_consulta(consulta).fetchall()



    # Método para iniciar sesión del médico
    def iniciar_sesion_medico(self, email, contraseña):
        consulta = "SELECT * FROM Medicos WHERE email = %s AND contraseña = %s"
        medico = self.db.ejecutar_consulta(consulta, (email, contraseña)).fetchone()

        if medico:
            return medico  # Devuelve la información del médico si es válido
        else:
            return None  # Retorna None si no se encuentra el médico

        
        
