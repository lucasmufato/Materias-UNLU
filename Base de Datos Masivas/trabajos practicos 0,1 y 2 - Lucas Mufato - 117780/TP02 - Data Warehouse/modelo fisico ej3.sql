create table cliente(
	codigo_cliente integer not null,
	razon_social varchar(20),
	CUIT varchar(20),
	saldo_cuenta real,
	condicion varchar(20),
	
	primary key(codigo_cliente)
);

create table producto(
	codigo_producto integer not null,
	descripcion	varchar(100),
	categoria varchar(20),
	marca varchar(40),
	especificaciones varchar(200),
	precio_unitario real,
	
	primary key(codigo_producto)
);

create table trimestre(
	id_trimestre integer not null,
	descripcion varchar(20),
	
	primary key(id_trimestre)
);

create table fecha(
	id_fecha integer  not null,
	dia integer,
	mes integer,
	año integer,
	fk_trimestre integer,
	
	primary key(id_fecha),
	foreign key(fk_trimestre) references trimestre(id_trimestre)
);

create table venta(
	fk_cliente integer not null,
	fk_producto integer not null,
	fk_fecha integer not null,
	unidades_vendidas integer,
	monto_total real,
	
	foreign key(fk_cliente) references cliente(codigo_cliente),
	foreign key(fk_producto) references producto(codigo_producto),
	foreign key(fk_fecha) references fecha(id_fecha)
);
