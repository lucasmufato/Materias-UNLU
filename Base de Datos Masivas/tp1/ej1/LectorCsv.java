package tp1.ej1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class LectorCsv {
	
	protected static String pathCsv= "";
	protected ArrayList< HashMap<String,String> > lista;
	protected String[] columnas = {"id","medio","provincia","ciudad","direccion","tipo de medio","especialidad"};
	
	public LectorCsv(String pathcsv, String[] campos){
		LectorCsv.pathCsv= pathcsv;
		this.columnas= campos;
	}
	
	public boolean existeArchivo(String path){
		File archivo = new File(path);
		if(archivo.exists()){
			return true;
		}else{
			return false;
		}
	}
	
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
		    line = br.readLine();
		    while(line!=null){
			    Integer prev=0;
			    Integer next=line.indexOf(";", prev);
			    HashMap<String,String> hash= new HashMap<String,String>();
			    for(int i=0; i<columnas.length; i++){
			    	hash.put(columnas[i], line.substring(prev, next));
			    	prev= ++next;
			    	next= line.indexOf(";", prev);
			    }
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

	public void mostrarLeido(){
		for(int i=0;i<20;i++){
			System.out.println( this.lista.get(i) );
		}
	}
	
	public ArrayList<HashMap<String, String>> getLista() {
		return lista;
	}

	public void setLista(ArrayList<HashMap<String, String>> lista) {
		this.lista = lista;
	}
}
