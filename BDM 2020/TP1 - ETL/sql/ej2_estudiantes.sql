create table planes(
    id_plan int primary key,
    codigo_plan int,
    codigo_carrera int,
    nombre_carrera varchar(200)
);

create table ciudades(
    id_ciudad int primary key,
    codigo_postal int,
    nombre_ciudad varchar(200),
    provincia varchar(50)
);

create table sedes(
    id_sede serial primary key,
    sede varchar(200)
);

create table sexo(
    id_sexo int primary key,
    sexo varchar(20)
);

create table cohorte(
    id_cohortes serial primary key,
    cohorte int
);

create table rendimiento_academico(
    id_estudiante int primary key ,
    id_plan int,
    id_sede int,
    id_ciudad int,
    id_sexo int,
    id_cohorte int,
    cantidad_cursadas int,
    cantidad_aprobadas int,
    promedio double precision,

    foreign key (id_plan) references planes(id_plan) on delete cascade,
    foreign key (id_sede) references sedes(id_sede) on delete cascade,
    foreign key (id_ciudad) references ciudades(id_ciudad) on delete cascade,
    foreign key (id_sexo) references sexo(id_sexo) on delete cascade,
    foreign key (id_cohorte) references cohorte(id_cohortes) on delete cascade
);

CREATE TABLE cursadas_2003_etl (
    id_estudiante integer,
    asignatura integer,
    condicion text,
    calificacion integer
);

insert into sexo(id_sexo, sexo) VALUES (1, 'M'), (2, 'F'), (3, 'O');

insert into sedes(sede) VALUES ('C.R. CHIVILCOY'), ('C.R. CAMPANA'), ('D.A. PERGAMINO'),('D.A. MERLO'),('D.A. ESCOBAR'),
('D.A. S.FERNANDO'),('D.A. MERCEDES'),('D.A. MORENO'),('CTERA'),('C.R. SAN MIGUEL'),('D.A. PILAR'),('ESP.ESTR.Y C.I.'),
('D.A. 9 DE JULIO'),('D.A. C. FEDERAL'),('D.A. UN.P.MERC.'),('SEDE LUJAN');

insert into cohorte (cohorte)
select i from generate_series(1990, 2030) as t(i);