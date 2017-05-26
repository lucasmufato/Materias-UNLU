package tp3_01;

import java.util.ArrayList;
import java.util.HashMap;

public class ArbolDecision {
	
	private ArrayList<HashMap<String, String>> dataset;
	private Nodo raiz;
	private Double entropiaDelDataset;
	private ArrayList<String> headers;
	private String valorObjetivo="asado";
	private Integer tamaño;
	private String valorPositivo="si";
	
	//chequea q esten lo datos necesarios
	//inicia las llamadas recursivas para armar el arbol
	public boolean armarArbol(){
		if(this.dataset==null){
			return false;
		}
		if(this.dataset.size()==0){
			return false;
		}
		if(this.headers==null){
			return false;
		}
		//this.calcularEntropiaDelDataset(this.dataset);
		this.raiz = new Nodo();
		return this.calcularNodo(this.raiz,headers,(ArrayList<HashMap<String, String>>) this.dataset.clone());
	}
	
	private boolean calcularNodo(Nodo nodo, ArrayList<String> campos,ArrayList<HashMap<String, String>> d){
		//para cada campo calculo la ganancia de informacion
		if(campos.size()==1){
			//si solo queda el resultado
			Integer cantidadPositivos = this.contarPositivosValorAtributo(campos.get(0), "si", d);
			Double result= ( (double)(cantidadPositivos * 100) )/( (double) d.size());
			if(result >= 50){
				nodo.setValorFinal("si");
			}else{
				nodo.setValorFinal("no");
			}
			return true;
		}
		//hago un vector que va a tener la ganancia de informacion por cada campo
		Double []ganaciasInformacion = new Double[campos.size()];
		for(int i=0; i<campos.size();i++){
			ganaciasInformacion[i]=this.gananciaInformacion(campos.get(i), d);
		}
		//obtengo el sub indice del campo con la maxima ganacia de informacion
		Integer subIndex = this.getMaximoGananciaInformacion(ganaciasInformacion);
		//valores posibles para ese atributo
		ArrayList<String> valores = this.getTiposDeValores(campos.get(subIndex), d);
		//por cada valor para ese campo
		for(String s: valores){
			//creo un rama en el nodo actual
			Nodo nuevoNodo= new Nodo();
			nodo.setHijo(nuevoNodo,s);	//apunta al nuevo nodo y le pasa la condicion s ej: valor="soleado"
			nodo.setAtributoDecision(campos.get(subIndex));
			//creo el hijo, ahora preparo los datos para la llamada recursiva
			ArrayList<String> nuevosCampos = (ArrayList<String>) campos.clone();
			nuevosCampos.remove(campos.get(subIndex));//saco el atribuo que analise recien
			ArrayList<HashMap<String, String>> nuevosDatos = (ArrayList<HashMap<String, String>>) d.clone();
			this.dejarAtributosConValor(campos.get(subIndex),s,nuevosDatos);	//del dataset dejo solo aquellos que el atributo seleccionado y con valor s ej: atributo"pronostico" valor "soleado"
			this.calcularNodo(nuevoNodo, nuevosCampos, nuevosDatos);	//llamada recursiva
		}
		
		return true;
	}

	//para poder probar llamando desde afuera
	public Double calcularEntropiaDelDataset(){
		return calcularEntropiaDelDataset(this.dataset);
	}
	
	//calcula la entropai para todo el dataset
	private Double calcularEntropiaDelDataset(ArrayList<HashMap<String, String>> d){
		this.tamaño = d.size();
		Integer cantidadPositivos = this.contarPositivosValorAtributo(this.valorObjetivo,this.valorPositivo,d);
		Integer cantidadNegativos = this.tamaño - cantidadPositivos;
		Double divNegativos = (double) ((double)cantidadNegativos/(double)this.tamaño);
		Double divPositivos = (double) ((double)cantidadPositivos/(double)this.tamaño);
		return (Double)( (-(divNegativos) * log(divNegativos,2) )-( (divPositivos) * log(divPositivos,2) ) );
	}

	//calcula la entropia para un tipo de valor en un campo
	private Double calcularEntropia(String campo,String valor,ArrayList<HashMap<String, String>> d) {
		Integer repeticiones = this.contarValorAtributo(campo, valor,d);
		Integer cantidadPositivos = this.contarPositivosValorAtributo(campo,valor,d);
		Integer cantidadNegativos = repeticiones - cantidadPositivos;
		Double divNegativos = (double) ((double)cantidadNegativos/(double)repeticiones);
		Double divPositivos = (double) ((double)cantidadPositivos/(double)repeticiones);
		return (Double)( (-(divNegativos) * log(divNegativos,2) )-( (divPositivos) * log(divPositivos,2) ) );
	}

	//calcula la ganancia de informacion de un atributo
	public Double gananciaInformacion(String atributo,ArrayList<HashMap<String, String>> d){
		//calculo la parte de la sumatoria
		Double sumatoria= new Double(0);
		//obtengo los valores para un atributo. ej: pronostico, tipo de valores: lluvioso, nublado, soleado
		ArrayList<String> tiposDeValores = this.getTiposDeValores(atributo,d);
		//adentro del for hago la parte de la sumatoria
		for(String s : tiposDeValores){
			Double Sv= (double) this.contarValorAtributo(atributo,s,d);	//seria el Sv de la formula
			Double division = (d.size()/ Sv);				// la parte de la division
			sumatoria += division * this.calcularEntropia(atributo, s,d);		//calculo la entropia y se la multiplico a la division, y se la sumo a la sumatoria
		}
		return (this.calcularEntropiaDelDataset(d) - sumatoria);
	}
	
	//cuenta la cantidad de veces q esta ese valor de ese atributo
	private Integer contarValorAtributo(String campo, String valor,ArrayList<HashMap<String, String>> d){
		Integer contador = new Integer(0);
		for(HashMap<String,String> h: d){
			if(h.get(campo).equals(valor)){
				contador++;
			}
		}
		return contador;
	}
	
	//devuelve una lista con los distintos valores para un atributo
	private ArrayList<String> getTiposDeValores(String atributo,ArrayList<HashMap<String, String>> d) {
		ArrayList<String> valores = new ArrayList<String>();
		for(HashMap<String,String> h: d){
			String s= h.get(atributo);
			if(!valores.contains(s)){
				valores.add(s);
			}
		}
		return valores;
	}
	
	//devuelve la cantidad de veces que aparece ese valor de ese campo con el valor positivo en la columna del valor objetivo
	//ej: valor objetivo=asado, valor positivo=si, campo=pronostico, valor=soleado.
	//PRONOSTICO | ASADO
	//lluvioso	| no
	//soleado	| si
	//soleado	| si
	//el metodo devuelve 2
	private Integer contarPositivosValorAtributo(String campo, String valor,ArrayList<HashMap<String, String>> d) {
		Integer contador=new Integer(0);
		for(HashMap<String,String> h: d){
			String s= h.get(campo);
			if(s.equals(valor)){
				contador++;
			}
		}
		return contador;
	}
	
	public void setRegistros(ArrayList<HashMap<String, String>> registros) {
		this.dataset=registros;
	}
	
	private static Float log(double x, double base){
	    return (float) (Math.log(x) / Math.log(base));
	}

	public void setHeaders(ArrayList<String> campos) {
		this.headers= campos;
	}
	
	//metodo que busca el maximo de ganancia de informacion y devuelve el subIndice del mismo
	private Integer getMaximoGananciaInformacion(Double[] gananciasInformacion) {
		Double max = gananciasInformacion[0];
		Integer p=new Integer(0);
		for(int s=0;s<gananciasInformacion.length;s++){
			if(gananciasInformacion[s]>max){
				max=gananciasInformacion[s];
				p=s;
			}
		}
		return p;
	}

	private void dejarAtributosConValor(String atributo, String valor,ArrayList<HashMap<String, String>> datos) {
		for(int i=0; i<datos.size();i++){
			HashMap<String, String> tupla = datos.get(i);
			//obtengo la tupla
			if(!tupla.get(atributo).equals(valor)){
				//si esa tupla NO tiene el valor "soleado" para el atributo "pronostico" la borro
				datos.remove(i);
				i--;
			}
		}
	}
	
	public void imprimirArbol(){
		System.out.println("");
		System.out.println("A CONTINUACION SE IMPRIMIRA EL ARBOL RESULTANTE");
		System.out.println("");
		System.out.println("RAIZ");
		System.out.println("");
		this.raiz.imprimite("");
	}
	
}//fin de la clase
