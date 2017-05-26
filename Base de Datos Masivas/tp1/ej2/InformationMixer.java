package tp1.ej2;

import java.util.ArrayList;
import java.util.HashMap;

public class InformationMixer {
	
	private LectorBD2 lector;
	private ArrayList<HashMap<String, String>> registros;
	private ArrayList<Carrera> carreras;
	private ArrayList<Estudiante> estudiantes;
	
	public void setRegistros(ArrayList<HashMap<String, String>> datos) {
		registros=datos;
		carreras= new ArrayList<Carrera>();
	}
	
	public void mostrarRegistros(){
		for(HashMap<String,String> h: registros){
			System.out.println(h.get("nro")+" - "+h.get("nombre"));
		}
	}

	public void analizarRegistros() {
		Carrera c;
		//por cada carrera
		for(HashMap<String,String> h: registros){
			Integer nro = Integer.parseInt( h.get("nro") );
			c= new Carrera(h.get("nombre"),nro);
			//me fijo si ya esta en la lista
			if(this.carreras.contains(c)){
				//si esta en la lista, agrego el nuevo codigo a la carrera que ya estaba
				Carrera carreraExistente=this.carreras.get( this.carreras.indexOf(c) );
				carreraExistente.agregarCodigo(nro);
			}else{
				//sino esta la agrego;
				this.carreras.add(c);
			}
		}
		
	}
	
	public boolean levantarDatosBD(){
		this.lector= new LectorBD2("tp1_ej2","lucas","lucas");
		this.estudiantes = lector.leerLegajoCursadasPromedio();
		if(this.estudiantes==null){
			this.lector.cerrarConexion();
			return false;
		}else{
			return true;
		}
	}
	
	public void mesclarDatos(){
		//por cada estudiante que tengo
		for(Estudiante e: this.estudiantes){
			Integer carrera=e.getNroCarrera();
			Integer index=0;
			boolean encontrado=false;
			//le busco el nombre de la carrera dado su plan
			while(!encontrado){
				//itero en la lista de carrera y pregunto si en la lista de nro de carrera de esa carrera 
				//esta el nro de carrera de este estudiante
				if( this.carreras.get(index).getCodigos().contains(carrera) ){
					//si esta, entonces le pongo ese nombre de carrera y acomo el nro de la carrera
					encontrado=true;
					String nombreCarrera=this.carreras.get(index).getNombre();
					e.setNombreCarrera(nombreCarrera);
					e.setNroCarrera( carrera/100 );
				}else{
					index++;
				}
			}
			index=0;
		}
	}
	
	public void guardarNuevosDatos(){
		this.lector.guardarEstudiantes(this.estudiantes);
	}
	
	public void mostrarCarreras(){
		for(Carrera c: this.carreras){
			System.out.println(c.toString());
		}
	}

	public void mostrarEstudiantes() {
		for(Estudiante e:this.estudiantes){
			System.out.println( e.toString() );
		}
	}
}
