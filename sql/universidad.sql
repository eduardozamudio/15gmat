--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Ubuntu 14.1-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: asignatura; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.asignatura (
    id_asignatura character varying(100) NOT NULL,
    nombre character varying(200) NOT NULL,
    anio numeric(1,0) NOT NULL,
    semestre numeric(1,0) NOT NULL,
    tipo character varying(100) NOT NULL,
    creditos smallint,
    grado character varying(100) NOT NULL
);


ALTER TABLE public.asignatura OWNER TO postgres;

--
-- Name: calificaciones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.calificaciones (
    id_estudiante character varying(100) NOT NULL,
    id_asignatura character varying(100) NOT NULL,
    edicion character varying(100) NOT NULL,
    calificacion numeric(5,2) NOT NULL
);


ALTER TABLE public.calificaciones OWNER TO postgres;

--
-- Name: estudiante; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estudiante (
    nombre character varying(100) NOT NULL,
    numero_telefono character varying(50) NOT NULL,
    direccion character varying(200),
    id_estudiante character varying(20) NOT NULL
);


ALTER TABLE public.estudiante OWNER TO postgres;

--
-- Data for Name: asignatura; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.asignatura (id_asignatura, nombre, anio, semestre, tipo, creditos, grado) FROM stdin;
15GMAT	Programación III: Bases de datos y programación	2	1	Obligatoria	6	GMAT
\.


--
-- Data for Name: calificaciones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.calificaciones (id_estudiante, id_asignatura, edicion, calificacion) FROM stdin;
30233132	15GMAT	Octubre 2021	9.00
29441979	15GMAT	Octubre 2021	8.00
\.


--
-- Data for Name: estudiante; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estudiante (nombre, numero_telefono, direccion, id_estudiante) FROM stdin;
Eduardo	+549 3764 206786	Posadas, Misiones, Argentina	29441979
María	+11 34 963986422	España	30233132
\.


--
-- Name: asignatura asignatura_nombre_grado_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT asignatura_nombre_grado_key UNIQUE (nombre, grado);


--
-- Name: asignatura asignatura_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT asignatura_pkey PRIMARY KEY (id_asignatura);


--
-- Name: calificaciones calificaciones_id_estudiante_id_asignatura_edicion_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.calificaciones
    ADD CONSTRAINT calificaciones_id_estudiante_id_asignatura_edicion_key UNIQUE (id_estudiante, id_asignatura, edicion);


--
-- Name: estudiante estudiante_id_estudiante_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estudiante
    ADD CONSTRAINT estudiante_id_estudiante_key UNIQUE (id_estudiante);


--
-- Name: calificaciones fk_calificaciones_asignatura; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.calificaciones
    ADD CONSTRAINT fk_calificaciones_asignatura FOREIGN KEY (id_asignatura) REFERENCES public.asignatura(id_asignatura);


--
-- Name: calificaciones fk_calificaciones_estudiante; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.calificaciones
    ADD CONSTRAINT fk_calificaciones_estudiante FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(id_estudiante);


--
-- PostgreSQL database dump complete
--

