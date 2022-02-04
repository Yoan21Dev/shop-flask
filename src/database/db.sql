-- CREATE TABLE IF NOT EXISTS productos(
--     id int(4) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
--     img_url CHAR(50),
--     precios int not NULL,
--     caracteristicas VARCHAR NULL,
--     nombre VARCHAR null ,
--     PRIMARY KEY(id)
-- );


-- CREATE TABLE if NOT EXISTS customer(
--     id tinyint not NULL AUTO_INCREMENT,
--     nombre VARCHAR(4) not NULL,
--     PRIMARY KEY(id)
-- );

-- CREATE TABLE if NOT EXISTS carrito(
--     id tinyint not NULL AUTO_INCREMENT,
--     productos_id tinyint(4) not NULL,
--     customer_id tinyint(4),
--     PRIMARY KEY(id),

--        FOREIGN KEY productos_id (productos_id)
--      REFERENCES productos(id),

--         FOREIGN KEY customer_id (custome_id)
--      REFERENCES customer(id),
    
-- )
-- CREATE TABLE carrito(
--     id int not NULL AUTO_INCREMENT PRIMARY KEY,
--     productos_id int not NULL,
--     customer_id int NOT NULL,
 
--        FOREIGN KEY productos_id (productos_id)
--      REFERENCES productos(id),

--         FOREIGN KEY customer_id (customer_id)
--      REFERENCES customer(id)
    
-- )
CREATE TABLE IF NOT EXISTS productos(
    id int UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
    img_url VARCHAR(50),
    precios int not NULL,
    caracteristicas VARCHAR(20) NULL,
    nombre  VARCHAR (10) null ,
    PRIMARY KEY(id)
);


CREATE TABLE if NOT EXISTS customer(
    id int not NULL AUTO_INCREMENT,
    nombre VARCHAR(10) not NULL,
    PRIMARY KEY(id)
);

CREATE TABLE if NOT EXISTS carrito(
    id int not NULL AUTO_INCREMENT,
    productos_id int not NULL,
    customer_id int not null,
    PRIMARY KEY(id)   
);
alter TABLE carrito add CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customer(id);
alter TABLE carrito add CONSTRAINT fk_productos FOREIGN KEY (productos_id) REFERENCES productos(id);




CREATE TABLE IF NOT EXISTS productos(
    id int UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
    img_url VARCHAR(50),
    precios int not NULL,
    caracteristicas VARCHAR(20) NULL,
    nombre  VARCHAR (10) null ,
    PRIMARY KEY(id)
);

CREATE TABLE if NOT EXISTS customer(
    id int not NULL AUTO_INCREMENT,
    nombre VARCHAR(10) not NULL,
    PRIMARY KEY(id)
);

CREATE TABLE if NOT EXISTS carrito(
    id int not NULL AUTO_INCREMENT,
    productos_id int not NULL,
    customer_id int not null,
    PRIMARY KEY(id)   
);

alter TABLE carrito add CONSTRAINT fk_productos_id_carrito FOREIGN KEY (productos_id) REFERENCES productos(id);
