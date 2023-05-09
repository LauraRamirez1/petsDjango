-- SQLite

--DELETE FROM core_cliente;
--DELETE FROM core_mascota;
--DELETE FROM core_producto;
--DELETE FROM core_servicio;


INSERT INTO core_cliente (nombre, telefono, correo, password) 
VALUES ('Mario Hugo', 56955242628, 'luis@gmail.com', 1234qwer);
INSERT INTO core_cliente (nombre, telefono, correo, password) 
VALUES ('Margarita Saldaña', 56955452387, 'salda@gmail.com', 7854nhtg);
INSERT INTO core_cliente (nombre, telefono, correo, password) 
VALUES ('Germán Ubiergo', 56955887766, 'germaubi@gmail.com', 6787bnjk);
INSERT INTO core_cliente (nombre, telefono, correo, password) 
VALUES ('Valentina Sanhueza', 5695646745, 'uydfgg@gmail.com', 4356dfgg);
INSERT INTO core_cliente (nombre, telefono, correo, password) 
VALUES ('Germán Ubiergo', 56955887766, 'germaubi@gmail.com', 4321reqw);


INSERT INTO core_mascota (nombreMascota, edadMascota, razaMascota, nombre_id) 
VALUES ('Copicopi', 12, 'Chihuahua', 6);
INSERT INTO core_mascota (nombreMascota, edadMascota, razaMascota, nombre_id) 
VALUES ('Elemento', 3, 'Pastor Alemán', 6);
INSERT INTO core_mascota (nombreMascota, edadMascota, razaMascota, nombre_id) 
VALUES ('Adjetivo', 5, 'Mestizo', 7);
INSERT INTO core_mascota (nombreMascota, edadMascota, razaMascota, nombre_id) 
VALUES ('Mente en Blanco', 11, 'Husky', 7);
INSERT INTO core_mascota (nombreMascota, edadMascota, razaMascota, nombre_id) 
VALUES ('Chaucha', 12, 'Bulldog', 8);
INSERT INTO core_mascota (nombreMascota, edadMascota, razaMascota, nombre_id) 
VALUES ('Coliforme', 9, 'Poodle', 9);
INSERT INTO core_mascota (nombreMascota, edadMascota, razaMascota, nombre_id) 
VALUES ('Tepotepo', 8, 'Golden Retriever', 9);
INSERT INTO core_mascota (nombreMascota, edadMascota, razaMascota, nombre_id) 
VALUES ('Yo no fui', 8, 'Golden Retriever', 10);


INSERT INTO core_producto (nombreProducto, precioProducto, descripcionProducto) 
VALUES ('Furminator', 12990, 'Peine para perro');
INSERT INTO core_producto (nombreProducto, precioProducto, descripcionProducto) 
VALUES ('Shampoo', 4990, 'Shampoo de avena para perro');
INSERT INTO core_producto (nombreProducto, precioProducto, descripcionProducto) 
VALUES ('Cortauña', 5500, 'Cortauña para gato o perro pequeño');
INSERT INTO core_producto (nombreProducto, precioProducto, descripcionProducto) 
VALUES ('Pelota plástica', 6000, 'Pelota plástica durable');
INSERT INTO core_producto (nombreProducto, precioProducto, descripcionProducto) 
VALUES ('Kong grande', 15990, 'Kong portagolosinas grande para perros');


INSERT INTO core_servicio (nombreServicio, precioServicio, descripcionServicio) 
VALUES ('Peluquería caninos', 15990, 'Servicio de peluquería para perros de todos los tamaños');
INSERT INTO core_servicio (nombreServicio, precioServicio, descripcionServicio) 
VALUES ('Peluquería felinos', 10990, 'Servicio de peluquería para gatos');
INSERT INTO core_servicio (nombreServicio, precioServicio, descripcionServicio) 
VALUES ('Corte de uñas caninos', 7900, 'Corte de uñas para perros');
INSERT INTO core_servicio (nombreServicio, precioServicio, descripcionServicio) 
VALUES ('Corte de uñas felinos', 5900, 'Corte de uñas para gatos');
INSERT INTO core_servicio (nombreServicio, precioServicio, descripcionServicio) 
VALUES ('Paseo de perros pequeños', 12990, 'Servicio de paseo de perros pequeños');
INSERT INTO core_servicio (nombreServicio, precioServicio, descripcionServicio) 
VALUES ('Paseo de perros medianos y grandes', 15990, 'Servicio de paseo de perros medianos y grandes');