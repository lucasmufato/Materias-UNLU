package tp1.ej1;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;

public class LectorBD {	
	
	protected Connection c;
	
	public LectorBD(String nombreBD,String user,String password){
	      try {
	         Class.forName("org.postgresql.Driver");
	         c = DriverManager.getConnection("jdbc:postgresql://localhost:5432/"+nombreBD,user, password);
	      } catch (Exception e) {
	    	 System.out.println("LectorBD-: error al conectar con la BD");
	         e.printStackTrace();
	         System.exit(-1);
	      }
	      System.out.println("LectorBD-: me conecte bien a la BD");
	}
	
	public ArrayList<Dato> leerTabla2Columnas(String tabla, String columna2,boolean tercerDato){
		//el booleano tercer dato es para saber si tiene q leer 2 o 3 datos, si es verdadero lee 3 datos
		ArrayList<Dato> respuesta=null;
		if(c!=null){
			respuesta = new ArrayList<Dato>();
			try{
				Statement stmt = c.createStatement();
		        ResultSet rs = stmt.executeQuery( "SELECT * FROM "+tabla+";" );
		        System.out.println("LectorBD-: leyendo "+tabla);
		        while ( rs.next() ) {
		           int id = rs.getInt("id");
		           String  nombre = rs.getString(columna2);
		           if(tercerDato){
		        	   int provincia = rs.getInt("id_provincia");
		        	   respuesta.add(new Dato(id,nombre,provincia));
		           }else{
		        	   respuesta.add(new Dato(id,nombre));
		           }
		        }
		        rs.close();
		        stmt.close();
			}catch(SQLException e){
				System.out.println("LectorBD-: error al leer tabla +"+tabla);
				e.printStackTrace();
				this.cerrarConexion();
			}
			System.out.println("LectorBD-: tabla: "+tabla+" leida");
		}
		return respuesta;
	}

	public boolean guardarEnBD(HashMap<String, String> h) {
		Statement stmt = null;
		Integer idCiudad = this.buscarCrearCiudad( h.get("ciudad"),h.get("provincia"));
		try{
			//c.setAutoCommit(false);
			stmt = c.createStatement();
	        String sql = "INSERT INTO MEDIOS (NOMBRE,ID_ESPECIALIDAD,ID_TIPO_MEDIO,DIRECCION,ID_CIUDAD) VALUES (";
	        String datos = "'"+h.get("medio")+"',";
	        if(h.get("especialidad")!=null){
	        	datos+= h.get("especialidad");
	        }else{
	        	datos+= "null";
	        }
	        if(h.get("tipo de medio")!=null){
	        	datos+= ","+h.get("tipo de medio");
	        }else{
	        	datos+= ","+"null";
	        }
	        if(h.get("direccion")!=null){
	        	datos+= ",'"+h.get("direccion")+"'";
	        }else{
	        	datos+= ","+"null";
	        }
	        //ciudad de prueba
	        datos+= ","+idCiudad+");";
	        //System.out.println("el query quedo: ");
	        //System.out.println(sql+datos);
	        stmt.executeUpdate(sql+datos);
	        stmt.close();
	        //c.commit();
		}catch(SQLException e){
			System.out.println("LectorBD-: error al guardar dato: "+h);
			e.printStackTrace();
			this.cerrarConexion();
			return false;
		}
		return true;
	}	
	
	private Integer buscarCrearCiudad(String ciudad, String provincia){
		Integer idCiudad=null;
		if(ciudad==null || provincia==null){
			return null;
		}
		try{
			Statement stmt = c.createStatement();
	        ResultSet rs = stmt.executeQuery( "SELECT * FROM CIUDADES C WHERE c.nombre ='"+ciudad+"' AND c.id_provincia="+provincia+";");
	        c.setAutoCommit(false);
	        
	        if(rs.next()){
	        	//si hay un siguiente valor, existe esa ciudad, entonces devuelvo el id de la ciudad
	        	 idCiudad = rs.getInt("id");
	        	 rs.close();
	        	 return idCiudad;
	        }else{
	        	//si no hay resultado, la ciudad no existe entonces tengo q crearla
	        	rs.close();
	        	stmt =c.createStatement();
	        	String sql = "INSERT INTO CIUDADES (NOMBRE,ID_PROVINCIA) VALUES ('"+ciudad+"',"+provincia+");";
	        	//System.out.println("EJECUTANDO: "+sql);
	        	stmt.executeUpdate(sql);
		        stmt.close();
		        c.commit();
		        //ahora que guarde la nueva ciudad, busco que ID le dio la BD, para eso hago una llamada recursiva y devuelvo el resultado
		        //cuando hago la recursion, lo primero q hace es busca si la ciudad existe, y como la acabo de crear, me va a devolver el id
		        return this.buscarCrearCiudad(ciudad, provincia);
	        }
		}catch(SQLException e){
			System.out.println("LectorBD-: error al guardar la ciudad: "+ciudad+" con provincia id: "+provincia);
			e.printStackTrace();
			this.cerrarConexion();
		}
		
		return idCiudad;
	}
	
	public void cerrarConexion(){
		try {
			c.close();
		} catch (SQLException e) {
			//nada
		}
	}
}