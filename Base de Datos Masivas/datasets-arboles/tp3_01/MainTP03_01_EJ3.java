package tp3_01;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

import tp1.ej1.LectorCsv;

public class MainTP03_01_EJ3 {

	public static void main(String[] args) {
		String[] campos = {"pronostico","temperatura","humedad","viento","asado"};
		LectorCsv lector= new LectorCsv("asado.csv",campos);
		ArrayList< HashMap<String,String> >registros = lector.leerArchivo();
		ArbolDecision arbol = new ArbolDecision();
		arbol.setRegistros(registros);
		arbol.setHeaders(  new ArrayList<String>(Arrays.asList(campos)) );
		arbol.armarArbol();
		//Double entropia =arbol.calcularEntropiaDelDataset();
		//System.out.println("la entropia del dataset es: "+entropia);
		arbol.imprimirArbol();
		
		System.out.println();
		System.out.println();
		System.out.println("EL PROGRAMA FINALIZO EXITOSAMENTE!!");
	}

}
