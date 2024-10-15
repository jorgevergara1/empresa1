--Creacion de la base de datos
CREATE DATABASE IF NOT EXISTS app_empresa_bd;

--Usar la base de datos recien creada
USE app_empresa_bd;

--creacion de la tabla usuarios
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    fecha_creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--creacion de la tabla empleados con una relacion 1.1
CREATE TABLE empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empleado VARCHAR(100) NOT NULL,
    apellidoS_empleado VARCHAR(100) NOT NULL,
    tipo_identidad VARCHAR(50) NOT NULL,
    n_identidad VARCHAR(50) NOT NULL,
    fecha_nacimiento TIMESTAMP,
    sexo CHAR(1) NOT NULL,
    gupo_rh VARCHAR(3) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL,
    profesion VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    foto_perfil VARCHAR(255),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT UNIQUE,--Relacion uno a uno
    CONSTRAINT fk_usuario FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE ON UPDATE CASCADE
);