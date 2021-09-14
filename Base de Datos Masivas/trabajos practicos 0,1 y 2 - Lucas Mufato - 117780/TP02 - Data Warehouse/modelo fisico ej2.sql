create table sexo(
	id_sexo integer not null,
	descripcion char(10),
	primary key(id_sexo)
);

create table condicion(
	id_condicion integer not null,
	descripcion varchar(20),
	primary key(id_condicion)
);

create table ingreso(
	id_ingreso integer not null,
	fecha date,
	primary key(id_ingreso)
);

create table carrera(
	id_carrera integer not null,
	descripcion char(20),
	primary key(id_carrera)
);

create table plan(
	id_plan integer not null,
	fk_carrera integer not null,
	descripcion char(20),
	
	primary key(id_plan),
	foreign key(fk_carrera) references carrera(id_carrera)
);

create table sede(
	id_sede integer not null,
	descripcion char(20),
	primary key(id_sede)
);

create table estudiante(
	fk_sexo integer not null,
	fk_condicion integer not null,
	fk_año_ingreso integer not null,
	fk_plan integer not null,
	fk_sede integer not null,
	cantidad integer,
	
	foreign key(fk_sexo) references sexo(id_sexo),
	foreign key(fk_condicion) references condicion(id_condicion),
	foreign key(fk_año_ingreso) references ingreso(id_ingreso),
	foreign key(fk_plan) references plan(id_plan),
	foreign key(fk_sede) references sede(id_sede)	
);
