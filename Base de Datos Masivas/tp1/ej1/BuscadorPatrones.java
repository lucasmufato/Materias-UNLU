package tp1.ej1;

import java.util.ArrayList;
import java.util.HashMap;

public class BuscadorPatrones {
	
	private ArrayList< HashMap<String,String> > lista;
	private LectorBD lector;
	
	//tendrian q sacarse de un archivo o BD
	private ArrayList<Dato> nombresProvincias;
	private ArrayList<Dato> nombresEspecialidades;
	private ArrayList<Dato> nombresTipoMedios;
	
	
	public BuscadorPatrones(ArrayList< HashMap<String,String> > lista){
		this.lista=lista;
		System.out.println("BuscadorPatrones-: fui creado");
	}
	
	public boolean levantarDatos(){
		
		this.lector = new LectorBD("tp1_medios","lucas","lucas");
		this.nombresProvincias = lector.leerTabla2Columnas("provincias","nombre",false);
		this.nombresEspecialidades = lector.leerTabla2Columnas("especialidades","descripcion",false);
		this.nombresTipoMedios = lector.leerTabla2Columnas("tipo_medio","descripcion",false);
		return true;
	}
	
	public boolean chequearTodo(){
		//metodo que normaliza los nombres de las provincias, ciudades, etc
		if(this.lista==null){
			return false;
		}
		
		//this.mostrarPosibilidades();
		System.out.println("BuscadorPatrones-: procesando");
		
		for(HashMap<String,String> h: this.lista){
			//arranco por chequear el nombre de la provincia y 
			this.chequearDato(h,this.nombresProvincias,"provincia");
			
			//ahora trato el tipo de medio y la especialidad
			this.chequearDato(h,nombresTipoMedios,"tipo de medio");
			
			//ahora trato las especialidades
			this.chequearDato(h,this.nombresEspecialidades,"especialidad");
			
			//si el nombre tiene el caracter ' lo borro y si la direccion tambien la tiene la borro 
			h.replace("medio", h.get("medio").replace("'", ""));
			h.replace("direccion", h.get("direccion").replace("'", ""));
			
			//chequeo la direccion
			if(h.get("direccion").equals("*") || h.get("direccion").equals("") || h.get("direccion").equals(";")){
				h.replace("direccion", null);
			}
			
			//TODO guarda la ciudad si no esta en la BD y relacionarla con la provincia
			
			//ahora guardo el dato en la BD
			if ( this.lector.guardarEnBD(h) ){
				System.out.println("guardado con exito");
			}else{
				break;
			}
		}
		this.lector.cerrarConexion();
		return true;
	}
	
	private void chequearDato(HashMap<String,String> h,ArrayList<Dato> nombresBien,String campo){
		String p= h.get(campo);
		double parecido=100;
		int mayor=-1;
		//busco el nombre de la provincia con el cual tiene el mayor "parecido"
		for(int i=0; i<nombresBien.size();i++){
			double j = Levenshtein.distance(p, nombresBien.get(i).getNombre());
			if( j < parecido){
				parecido = j;
				mayor=i;
			}
		}
		
		//ahora reemplazo la ciudad si esta tiene *, poniendole el nombre de la provincia
		if(h.get(campo).equals("*") || h.get(campo).equals("") || h.get(campo).equals(";")){
			if(campo.equals("provincia")){
				//si estoy tocando las provincias
				h.replace("ciudad", null);
				h.replace("provincia", null);
			}else{
				System.out.println("para el id: "+h.get("id")+ " no se encontro matcheo para el campo: "+campo+"="+h.get(campo)+" , se reemplaza por null");
				h.replace(campo, null);
			}
		}else{
			//muestro q palabra cambio por cual otra
			//System.out.println(h.get(campo)+" -> "+nombresBien.get(mayor).getNombre());
			h.replace(campo, nombresBien.get(mayor).getId().toString());
		}
		
		// si la ciudad esta vacia pongo el nombre de la provincia
		if(h.get("ciudad")!=null){
			if( h.get("ciudad").equals("") || h.get("ciudad").equals("*") || h.get("ciudad").equals(";") ){
				h.replace("ciudad",  nombresBien.get(mayor).getNombre());
			}
		}
		
	}
	
	protected void mostrarPosibilidades(){
		ArrayList<String> provinciasLeidas= new ArrayList<String>();
		ArrayList<String> tiposMediosLeidos= new ArrayList<String>();
		ArrayList<String> especialidades= new ArrayList<String>();
		for(HashMap<String,String> h: this.lista){
			//por cada provincia en la lista de hashmaps, me fijo si esta en la lista, si no esta la agrego
			String p= h.get("provincia");
			if(!provinciasLeidas.contains(p)){
				provinciasLeidas.add(p);
			}
			if(p.equals("*")){
				System.out.println("pronvincia: * en la fila: "+h.get("id"));
			}
			p = h.get("tipo de medio");
			if(!tiposMediosLeidos.contains(p)){
				tiposMediosLeidos.add(p);
			}
			
			p = h.get("especialidad");
			if(!especialidades.contains(p)){
				especialidades.add(p);
			}
		}
		//ahora muestro todas las provincias que tengo
		System.out.println("BuscadorPatrones-:");
		System.out.println("Las provincias leidas son: ");
		for(String s: provinciasLeidas){
			System.out.println(s);
		}
		System.out.println("Fin provincias leidas, total: "+provinciasLeidas.size());
		System.out.println();
		
		System.out.println("Las tipo de medios leidos son: ");
		for(String s: tiposMediosLeidos){
			System.out.print('"'+s+'"'+",");
		}
		System.out.println("Fin tipo de medios leidos, total: "+tiposMediosLeidos.size());
		System.out.println();
		
		System.out.println("Las especialidades leidas son: ");
		for(String s: especialidades){
			System.out.print('"'+s+'"'+",");
		}
		System.out.println("Fin especialidades leidas, total: "+especialidades.size());
		System.out.println();
	}
}
