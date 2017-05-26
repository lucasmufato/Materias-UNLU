package tp1.ej2;

public class Estudiante {
	private Integer legajo;
	private Integer cursadas;
	private Integer aprobadads;
	private Double promedio;
	private Integer nroCarrera;
	private String nombreCarrera;
	
	public Estudiante(Integer legajo, Integer cursadas, Double promedio,Integer planEstudios,Integer aprobadas){
		this.legajo=legajo;
		this.cursadas=cursadas;
		this.promedio=promedio;
		this.nroCarrera=planEstudios;
		this.aprobadads=aprobadas;
	}
	
	public Integer getLegajo() {
		return legajo;
	}
	public void setLegajo(Integer legajo) {
		this.legajo = legajo;
	}
	public Integer getCursadas() {
		return cursadas;
	}
	public void setCursadas(Integer cursadas) {
		this.cursadas = cursadas;
	}
	public Integer getAprobadads() {
		return aprobadads;
	}

	public void setAprobadads(Integer aprobadads) {
		this.aprobadads = aprobadads;
	}

	public Double getPromedio() {
		return promedio;
	}
	public void setPromedio(Double promedio) {
		this.promedio = promedio;
	}
	public Integer getNroCarrera() {
		return nroCarrera;
	}
	public void setNroCarrera(Integer nroCarrera) {
		this.nroCarrera = nroCarrera;
	}
	public String getNombreCarrera() {
		return nombreCarrera;
	}
	public void setNombreCarrera(String nombreCarrera) {
		this.nombreCarrera = nombreCarrera;
	}
	
	@Override
	public String toString(){
		return 	"legajo: "+ this.legajo + " nroCarrera: " +this.nroCarrera +" nombreC:"+this.nombreCarrera +" cursadas:"+
				this.cursadas +" aprobadas: "+this.aprobadads +" promedio: "+this.promedio;
	}
}
