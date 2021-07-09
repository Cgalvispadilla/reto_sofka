Reto Sofka
Pasos de funcionamiento:

#1. Primero Creas la base de dato postgreSql con la siguiente sentencia SQL
   

CREATE DATABASE reto_db
WITH
OWNER = postgres
ENCODING = 'UTF8'
LC_COLLATE = 'Spanish_Colombia.1252'
LC_CTYPE = 'Spanish_Colombia.1252'
TABLESPACE = pg_default
CONNECTION LIMIT = -1;


2. Crear la tabla con que trabajara el programa con la siguiente sentencia SQL
-- Table: public.podio

-- DROP TABLE public.podio;

CREATE TABLE public.podio(
id_podio integer NOT NULL DEFAULT nextval('podio_id_podio_seq'::regclass),
primero character varying(240) COLLATE pg_catalog."default",
segundo character varying(240) COLLATE pg_catalog."default",
tercero character varying(240) COLLATE pg_catalog."default",
cantidad integer,
CONSTRAINT podio_pkey PRIMARY KEY (id_podio)
)
TABLESPACE pg_default;

ALTER TABLE public.podio
OWNER to postgres;

3. ya habiendo creado la base de datos y la tabla en consola corra \env\Scripts\activate.bat para que active el entorno virtual de Python

4. Corra el archivo main.py y use el programa
