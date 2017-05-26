package tp1.ej1;

public class Dato {
	
	private Integer id;
	private String nombre;
	private Integer nroProvincia;
	
	public Dato(Integer id, String nombre){
		this.id=id;
		this.nombre=nombre;
	}
	
	public Dato(Integer id, String nombre,Integer nroProvincia){
		this(id, nombre);
		this.nroProvincia=nroProvincia;
	}
	
	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	public Integer getNroProvincia() {
		return nroProvincia;
	}

	public void setNroProvincia(Integer nroProvincia) {
		this.nroProvincia = nroProvincia;
	}

	@Override
	public String toString(){
		return this.id+"-"+this.nombre+"-"+this.nroProvincia;
	}
	
	@Override
	public boolean equals(Object o){
		Dato otroDato = (Dato)o;
		if(otroDato.getId()==this.id){
			return true;
		}else{
			return false;
		}
		
	}
}