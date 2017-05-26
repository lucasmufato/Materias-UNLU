package tp1.ej1;

public class MainTP1EJ1 {

	public static void main(String[] args) {
		System.out.println("Ejercicio NRO 1 - Lucas Mufato");
		String[] columnas = {"id","medio","provincia","ciudad","direccion","tipo de medio","especialidad"};
		LectorCsv lector = new LectorCsv("01-01-medios.csv",columnas);
		BuscadorPatrones bp;
		lector.leerArchivo();
		//lector.mostrarLeido();
		bp = new BuscadorPatrones( lector.getLista() );
		bp.levantarDatos();
		bp.chequearTodo();
		System.out.println();
		System.out.println("---------------------------------------------------------------");
		System.out.println();
		System.out.println("El programa finalizo exitosamente");
		System.out.println();
		System.out.println("---------------------------------------------------------------");
	}

}
