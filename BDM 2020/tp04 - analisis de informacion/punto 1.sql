-- punto A
select m.id as id, m.nombre as nombre , c.nombre as ciudad, e.descripcion as especialidad, tm.descripcion as tipo from medios m
    inner join ciudades c on m.id_ciudad = c.id
    inner join especialidades e on m.id_especialidad = e.id
    inner join tipo_medio tm on m.id_tipo_medio = tm.id;

-- punto B
select m.id as id, m.nombre as nombre , c.nombre as ciudad, e.descripcion as especialidad, tm.descripcion as tipo from medios m
    inner join ciudades c on m.id_ciudad = c.id
    inner join provincias p on p.id = c.id_provincia
    inner join especialidades e on m.id_especialidad = e.id
    inner join tipo_medio tm on m.id_tipo_medio = tm.id
    where p.nombre = 'cordoba';

-- punto C
select m.id as id, m.nombre as nombre , c.nombre as ciudad, e.descripcion as especialidad, tm.descripcion as tipo from medios m
    inner join ciudades c on m.id_ciudad = c.id
    inner join especialidades e on m.id_especialidad = e.id
    inner join tipo_medio tm on m.id_tipo_medio = tm.id
    where m.nombre like 'M%'