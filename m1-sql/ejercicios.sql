CREATE DATABASE m1_caso_practico;

USE m1_caso_practico;

CREATE TABLE CLIENTES (
id_cliente INT PRIMARY KEY,
nombre VARCHAR(50),
apellido VARCHAR(50),
email VARCHAR(100),
telefono VARCHAR(30),
direccion VARCHAR(100)
);

CREATE TABLE PRODUCTOS (
id_producto INT PRIMARY KEY,
nombre VARCHAR(50),
descripcion TEXT,
precio DECIMAL(10, 2),
stock INT
);

CREATE TABLE PEDIDOS (
id_pedido INT PRIMARY KEY,
id_client INT,
fecha DATE
);

CREATE TABLE DETALLES_PEDIDOS (
id_detalle_pedido INT PRIMARY KEY AUTO_INCREMENT,
id_pedido INT,
id_producto INT,
cantidad INT,
fecha DATE
);


INSERT INTO clientes (id_cliente, nombre, apellido, email, telefono, direccion) VALUES
(001, 'Malala', 'Kamory', 'malala.kamory@gmail.com', '624498083', 'Calle de los Tejedores 15'),
(002, 'Fitiavana', 'Nirina', 'fitia.nirina@gmail.com', '643216542', 'Calle de Candilejas  58'),
(003, 'Youssouf', 'Bangoura', 'youssouf.bangoura@gmail.com', '665482462', 'calle de Camarena 145'),
(004, 'Maria angeles', 'Rubia', 'mangeles.rubia@gmail.com', '625431526', 'Calle de Mijas 67'),
(005, 'Juan', 'Benito', 'juan.benito@gmail.com', '6987596420', 'Calle del Cozazón 35');


INSERT INTO productos (id_producto, nombre, descripcion, precio, stock) VALUES
(201, 'Aspirador', 'uso manual, con sensor de huellas', 24.99, 15),
(202, 'Lector DNI Electrónico', 'Inteligente, compatible con PC', 11.99, 102),
(203, 'Kindle', 'Pantalla tactil y alta resolución,  waterproof', 123.99, 37),
(204, 'Cerradura electrónica', 'Inteligente, contraseña huellas', 117.08, 9),
(205, 'Patinete eléctrico', 'robusto, 25km/h, autonomía 25km', 699.99, 47),
(206, 'Pulsera de actividad', 'Contador de paso, 10 días, sumergible', 64.67, 203),
(207, 'Disco duro externo', '8T, 3.5, USB 3.0, contraseña', 179.99, 12),
(208, 'Iphone 14', '612 GB, waterproof, inteligente', 1289.00, 5),
(209, 'Televisor Mini LED', 'retroiluminación mini Led, 65X95X/P', 1999.00, 20),
(210, 'Playstation 5', 'Sensor de voz, con mando inalámbrico DualSense', 489.99, 36);


INSERT INTO pedidos (id_pedido, id_client, fecha) VALUES
(303, 203, '2023-03-25'),
(304, 204, '2023-07-29'),
(305, 205, '2023-12-31');


INSERT INTO detalles_pedidos (id_detalle_pedido, id_pedido, id_producto, fecha) VALUES
(401, 301, 201, '2023-04-24'),
(402, 302, 202, '2023-09-10'),
(403, 303, 203, '2023-03-23'),
(404, 304, 204, '2023-12-12'),
(405, 305, 205, '2023-12.10'),
(406, 306, 206, '2023-09-27'),
(407, 307, 207, '2023-11-13'),
(408, 308, 208, '2023-01-01'),
(409, 309, 209, '2023-12-24'),
(410, 310, 209, '2023-04-22');



SELECT * FROM clientes ORDER BY apellido ASC;

SELECT * FROM productos WHERE stock < 10;

SELECT * FROM pedidos WHERE id_client = 204;


SELECT id_pedido, SUM(24.99 * 15) AS total_venta
FROM detalles_pedidos
GROUP BY id_pedido;


SELECT id_pedido, COUNT(DISTINCT id_producto) AS cantidad_productos
FROM detalles_pedidos
GROUP BY id_pedido
ORDER BY cantidad_productos DESC
LIMIT 10;