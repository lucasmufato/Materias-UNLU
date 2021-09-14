create table especialidades(
	id serial not null,
	descripcion varchar(100) not null,
	primary key(id)
);

create table tipo_medio(
	id serial not null,
	descripcion varchar(100) not null,
	primary key(id)
);

create table provincias(
	id serial not null,
	nombre varchar(200) not null,
	primary key(id)
);

create table ciudades(
	id serial not null,
	nombre varchar(200) not null,
	id_provincia integer,
	
	primary key(id),
	foreign key(id_provincia) references provincias(id) on delete cascade
);

create table medios(
	id serial not null,
	nombre varchar(200) not null,
	id_especialidad integer,
	id_tipo_medio integer,
	direccion varchar(300),
	id_ciudad integer,
	
	primary key(id),
	foreign key (id_especialidad) references especialidades(id) on delete cascade,
	foreign key (id_tipo_medio) references tipo_medio(id) on delete cascade,
	foreign key (id_ciudad) references ciudades(id) on delete cascade
);

/* poblo la base de datos */

insert into especialidades (descripcion)
SELECT *
FROM unnest(ARRAY['interes general','salud','economia','politica','mujer','deportes','educacion','countries','judiciales','ciencia / salud','ecologia','tendencias','construccion','decoracion','musica','tecnologia','automoviles','tendencia','manualidades','cocina','infantil','agro','turismo','guia','espectaculos','paisajismo','cultura','adolescentes','estilo de vida','maternidad','consumo','masculina','ciencia/salud','vinos','eventos','agropecuario','propiedades','religion','policiales','cine','juegos ','musica','salud mental','folclore','autos','historia','astrologia','transportes','obras estatales','meteorologia','medio ambiente','tv por cable','moda','bicicletas','negocios','electronica','arte','folklore','fotografia','humor','entretenimiento','ofertas','transporte','guia de cursos','agroindustria','juridico','informatica','salud/ciencia','salud','folcklore','diexismo','folckore','interes general','clima','intimidades','medios','automovilismo','clasificados','andinismo','musica clasica','disco pub','bailable','hockey','musica  ','cultural y musical','guia','esqui','turismo y gral','regional','religion','gremio prensa','judicial','economia ','armas','comunicacion','legislacion','arquitectura','empresas','juegos','computacion','derecho','espectaculo','editorial','barrial','consumidores','publicidad','geografia','industria','belleza','vivienda','gastronomia','salud animal','familia','exparcimiento','animales','masculino','salud ambiental','empleos','sastre']);

insert into tipo_medio (descripcion)
SELECT *
FROM unnest(ARRAY['digital','agencia','periodico','television','radio','revista','periodico mens.','r','diario','television','blog','radio ','periodico semanal','semanal','digial','portal','guia','suplementos']);

insert into provincias (nombre)
SELECT *
FROM unnest(ARRAY['capital federal','buenos aires','tierra del fuego', 'santa cruz','chubut','rio negro','neuquen','la pampa','mendoza', 'san luis','cordoba','santa fe','san juan','la rioja','catamarca','corrientes','misiones','chaco','formosa','tucuman','salta','jujuy','entre rios','santiago del estero']);
