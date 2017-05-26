package tp1.ej2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

import tp1.ej1.LectorCsv;

public class LectorTxt extends LectorCsv {

	public LectorTxt(String pathcsv, String[] campos) {
		super(pathcsv, campos);
	}
	
	@Override
	public ArrayList< HashMap<String,String> > leerArchivo(){
		
		if (!this.existeArchivo(pathCsv) ){
			System.err.println("no se encontro el archivo: "+pathCsv);
			return null;
		}
		
		ArrayList< HashMap<String,String> > lista = new ArrayList< HashMap<String,String> >();
		
		try(
			BufferedReader br = new BufferedReader(new FileReader(pathCsv)))
			//BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(pathCsv), "UTF8")))
			{
		    String line = br.readLine();
		    while(line!=null){
			    HashMap<String,String> hash= new HashMap<String,String>();
			    String nro= line.substring(0, 15).trim();
			    String nombre = line.substring(16).trim();
			    hash.put("nro", nro);
			    hash.put("nombre", nombre);
			    lista.add(hash);
			    line = br.readLine();
		    }
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
		System.out.println("LectorCsv-: "+lista.size()+" lineas leidas correctamente");
		this.lista=lista;
		return lista;
	}
}
