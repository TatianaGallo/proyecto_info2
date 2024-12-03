# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:57:43 2024

@author: tatia
"""

import mysql.connector

# Configuración de conexión
config = {
    'host': '127.0.0.1',      # Servidor local
    'user': 'root',           # Usuario root
    'password': '',           # Sin contraseña
    'database': 'trabajo_final'  # Seleccionar la base de datos 
}

try:
    # Intentar la conexión
    conexion = mysql.connector.connect(**config)

    if conexion.is_connected():
        print("Conexión exitosa a MySQL")
        cursor = conexion.cursor()

        # Crear la tabla 'Usuarios'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                contraseña VARCHAR(100) NOT NULL,
                rol ENUM('medico', 'paciente') NOT NULL,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("Tabla Usuarios creada")

        # Crear la tabla 'Medicos'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Medicos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_usuario INT,
                nombre VARCHAR(100),
                email VARCHAR(100) UNIQUE,
                contraseña VARCHAR(100)
            );
        """)
        print("Tabla Medicos creada")

        # Crear la tabla 'Pacientes'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pacientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_usuario INT,
                nombre VARCHAR(100),
                email VARCHAR(100) UNIQUE,
                contraseña VARCHAR(100)
            );
        """)
        print("Tabla Pacientes creada")

        # Crear la tabla 'Citas'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Citas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                
                fecha DATE NOT NULL,
                hora TIME NOT NULL,
                descripcion TEXT
                
            );
        """)
        print("Tabla Citas creada")

except mysql.connector.Error as error:
    print(f"Error al crear las tablas: {error}")

finally:
    # Cerrar conexión si fue establecida
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

