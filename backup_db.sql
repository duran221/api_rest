--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-05-01 01:53:43

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
-- TOC entry 217 (class 1259 OID 16412)
-- Name: asignaturas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.asignaturas (
    codigo_asignatura integer NOT NULL,
    codigo_docente integer NOT NULL,
    nombre_asignatura character varying(50) NOT NULL,
    numero_creditos numeric(2,0) NOT NULL
);


ALTER TABLE public.asignaturas OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16411)
-- Name: asignaturas_codigo_asignatura_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.asignaturas_codigo_asignatura_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.asignaturas_codigo_asignatura_seq OWNER TO postgres;

--
-- TOC entry 3355 (class 0 OID 0)
-- Dependencies: 216
-- Name: asignaturas_codigo_asignatura_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.asignaturas_codigo_asignatura_seq OWNED BY public.asignaturas.codigo_asignatura;


--
-- TOC entry 215 (class 1259 OID 16400)
-- Name: docentes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.docentes (
    codigo_docente integer NOT NULL,
    documento character varying(30),
    nombres character varying(50) NOT NULL,
    apellidos character varying(50) NOT NULL,
    fecha_nacimiento timestamp without time zone NOT NULL,
    edad numeric(3,0) NOT NULL,
    genero character varying(50) NOT NULL,
    direccion character varying(200),
    salario numeric NOT NULL,
    CONSTRAINT docentes_check CHECK (((salario > (0)::numeric) AND ((edad >= (0)::numeric) AND (edad <= (130)::numeric))))
);


ALTER TABLE public.docentes OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16399)
-- Name: docentes_codigo_docente_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.docentes_codigo_docente_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.docentes_codigo_docente_seq OWNER TO postgres;

--
-- TOC entry 3356 (class 0 OID 0)
-- Dependencies: 214
-- Name: docentes_codigo_docente_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.docentes_codigo_docente_seq OWNED BY public.docentes.codigo_docente;


--
-- TOC entry 218 (class 1259 OID 16423)
-- Name: estudiantes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estudiantes (
    documento character varying(30) NOT NULL,
    nombres character varying(50) NOT NULL,
    apellidos character varying(50) NOT NULL,
    fecha_nacimiento timestamp without time zone NOT NULL,
    edad numeric(4,0) NOT NULL,
    genero character varying(50) NOT NULL,
    direccion character varying(200),
    promedio real
);


ALTER TABLE public.estudiantes OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16428)
-- Name: estudiantes_asignaturas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estudiantes_asignaturas (
    codigo_asignatura integer NOT NULL,
    documento_estudiante character varying(30) NOT NULL,
    fecha_registro timestamp without time zone NOT NULL,
    nota_asignatura real
);


ALTER TABLE public.estudiantes_asignaturas OWNER TO postgres;

--
-- TOC entry 3187 (class 2604 OID 16415)
-- Name: asignaturas codigo_asignatura; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignaturas ALTER COLUMN codigo_asignatura SET DEFAULT nextval('public.asignaturas_codigo_asignatura_seq'::regclass);


--
-- TOC entry 3186 (class 2604 OID 16403)
-- Name: docentes codigo_docente; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.docentes ALTER COLUMN codigo_docente SET DEFAULT nextval('public.docentes_codigo_docente_seq'::regclass);


--
-- TOC entry 3347 (class 0 OID 16412)
-- Dependencies: 217
-- Data for Name: asignaturas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.asignaturas (codigo_asignatura, codigo_docente, nombre_asignatura, numero_creditos) FROM stdin;
543	1234	Sociales	4
2234	5435	Historia	1
\.


--
-- TOC entry 3345 (class 0 OID 16400)
-- Dependencies: 215
-- Data for Name: docentes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.docentes (codigo_docente, documento, nombres, apellidos, fecha_nacimiento, edad, genero, direccion, salario) FROM stdin;
1234	342324	Cristian	Duran	1980-08-12 00:00:00	22	M	Calle 23	2000.4
5435	1098310693	Alex	Ronaldos	1994-08-12 00:00:00	25	M	Calle 11	30000
\.


--
-- TOC entry 3348 (class 0 OID 16423)
-- Dependencies: 218
-- Data for Name: estudiantes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estudiantes (documento, nombres, apellidos, fecha_nacimiento, edad, genero, direccion, promedio) FROM stdin;
1093234	Carolina	Infante	1999-08-12 00:00:00	14	F	Calle 23	12.4
10934422	Carolina	Infante	1999-08-12 00:00:00	14	F	Calle 23	12.4
109344223	Alex	Infante	1999-08-12 00:00:00	14	F	Calle 23	12.4
1098310693	Cristiano	Ronaldos	1994-08-12 00:00:00	10	M	Calle 11	12.4
\.


--
-- TOC entry 3349 (class 0 OID 16428)
-- Dependencies: 219
-- Data for Name: estudiantes_asignaturas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estudiantes_asignaturas (codigo_asignatura, documento_estudiante, fecha_registro, nota_asignatura) FROM stdin;
543	109344223	2023-05-01 01:03:41.160839	3.4
2234	109344223	2023-05-01 01:04:40.553066	5
\.


--
-- TOC entry 3357 (class 0 OID 0)
-- Dependencies: 216
-- Name: asignaturas_codigo_asignatura_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.asignaturas_codigo_asignatura_seq', 1, false);


--
-- TOC entry 3358 (class 0 OID 0)
-- Dependencies: 214
-- Name: docentes_codigo_docente_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.docentes_codigo_docente_seq', 1, false);


--
-- TOC entry 3194 (class 2606 OID 16417)
-- Name: asignaturas asignaturas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignaturas
    ADD CONSTRAINT asignaturas_pkey PRIMARY KEY (codigo_asignatura);


--
-- TOC entry 3190 (class 2606 OID 16410)
-- Name: docentes docentes_documento_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.docentes
    ADD CONSTRAINT docentes_documento_key UNIQUE (documento);


--
-- TOC entry 3192 (class 2606 OID 16408)
-- Name: docentes docentes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.docentes
    ADD CONSTRAINT docentes_pkey PRIMARY KEY (codigo_docente);


--
-- TOC entry 3198 (class 2606 OID 16432)
-- Name: estudiantes_asignaturas estudiantes_asignaturas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estudiantes_asignaturas
    ADD CONSTRAINT estudiantes_asignaturas_pkey PRIMARY KEY (codigo_asignatura, documento_estudiante);


--
-- TOC entry 3196 (class 2606 OID 16427)
-- Name: estudiantes estudiantes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estudiantes
    ADD CONSTRAINT estudiantes_pkey PRIMARY KEY (documento);


--
-- TOC entry 3199 (class 2606 OID 16418)
-- Name: asignaturas asignaturas_codigo_docente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignaturas
    ADD CONSTRAINT asignaturas_codigo_docente_fkey FOREIGN KEY (codigo_docente) REFERENCES public.docentes(codigo_docente);


--
-- TOC entry 3200 (class 2606 OID 16433)
-- Name: estudiantes_asignaturas estudiantes_asignaturas_codigo_asignatura_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estudiantes_asignaturas
    ADD CONSTRAINT estudiantes_asignaturas_codigo_asignatura_fkey FOREIGN KEY (codigo_asignatura) REFERENCES public.asignaturas(codigo_asignatura);


--
-- TOC entry 3201 (class 2606 OID 16438)
-- Name: estudiantes_asignaturas estudiantes_asignaturas_documento_estudiante_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estudiantes_asignaturas
    ADD CONSTRAINT estudiantes_asignaturas_documento_estudiante_fkey FOREIGN KEY (documento_estudiante) REFERENCES public.estudiantes(documento);


-- Completed on 2023-05-01 01:53:43

--
-- PostgreSQL database dump complete
--

