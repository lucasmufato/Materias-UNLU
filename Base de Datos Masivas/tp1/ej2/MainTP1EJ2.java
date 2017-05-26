package tp1.ej2;

import tp1.ej1.LectorCsv;

public class MainTP1EJ2 {

	public static void main(String[] args) {
		System.out.println("Ejercicio NRO 2 - Lucas Mufato");
		String []campos= {"nro","nombre"};
		LectorCsv lector = new LectorTxt("01-02-planes.txt",campos);
		
		InformationMixer informationMixer = new InformationMixer();
		informationMixer.setRegistros( lector.leerArchivo() );
		//informationMixer.mostrarRegistros();
		informationMixer.analizarRegistros();
		//informationMixer.mostrarCarreras();
		if( informationMixer.levantarDatosBD() ){
			informationMixer.mesclarDatos();
			informationMixer.guardarNuevosDatos();
			//informationMixer.mostrarEstudiantes();
			System.out.println();
			System.out.println("FIN EXITOSO");
		}else{
			System.out.println();
			System.out.println("ERROR AL LEER DE LA BD, FIN DE EJECUCION");
		}
	}

}
