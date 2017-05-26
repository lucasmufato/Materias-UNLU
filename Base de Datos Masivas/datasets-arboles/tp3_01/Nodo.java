package tp3_01;

import java.util.ArrayList;

public class Nodo {
	
	private ArrayList<Nodo> hijos; //al nodo hijo que lleva cada rama
	private ArrayList<String> condicionRama; //arreglo de condiciones, ej: atributoDecison="lluviosos"
	private String atributoDecision; //nombre del atributo que voy a usar para las ramas
	private String ValorFinal;
	
	public Nodo(){
		this.hijos= new ArrayList<Nodo>();
		this.condicionRama = new ArrayList<String>();
		this.ValorFinal=null;
		this.atributoDecision=null;
	}
	
	@Override
	public boolean equals(Object o){		
		return true;
	}

	public void setHijo(Nodo nuevoNodo, String s) {
		this.hijos.add(nuevoNodo);
		this.condicionRama.add(s);
	}

	public void setAtributoDecision(String atributo) {
		this.atributoDecision=atributo;
	}

	public void setValorFinal(String valor) {
		this.ValorFinal=valor;
	}

	public void imprimite(String tabulacion) {
		if(this.ValorFinal!=null){
			System.out.println(tabulacion+"-"+ValorFinal);
		}else{
			System.out.println(tabulacion+this.atributoDecision);
			for(int i=0; i<this.hijos.size();i++){
				System.out.println( tabulacion+this.condicionRama.get(i) );
				String new_tab ="    "+tabulacion;
				this.hijos.get(i).imprimite(new_tab);
			}
		}
	}
}
