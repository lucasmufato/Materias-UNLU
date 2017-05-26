package tp1.ej2;

import java.util.ArrayList;

public class Carrera {
	
	private String nombre;
	private ArrayList<Integer> codigos;
	
	public Carrera(String nombre, Integer codigo){
		this.nombre=nombre;
		this.codigos= new ArrayList<Integer>();
		this.codigos.add(codigo);
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public ArrayList<Integer> getCodigos() {
		return codigos;
	}

	public void setCodigos(ArrayList<Integer> codigos) {
		this.codigos = codigos;
	}
	
	public void agregarCodigo(Integer codigo){
		this.codigos.add(codigo);
	}
	
	@Override
	public boolean equals(Object o){
		try{
			if( ((Carrera)o ).getNombre().equals(this.nombre) ){
				return true;
			}else{
				return false;
			}
		}catch(Exception e){
			return false;
		}
	}
	
	@Override
	public String toString(){
		String codigos=" | codigos: ";
		for(Integer i:this.codigos){
			codigos=codigos+i+"-";
		}
		return "nombre: "+this.nombre+codigos;
	}
}
