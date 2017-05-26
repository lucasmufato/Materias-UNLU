package tp1.ej2;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import tp1.ej1.LectorBD;

public class LectorBD2 extends LectorBD {
	
	private static String query1="select cc1.legajo1,cc1.cursadas,cc2.promedio_aprobadas,cc1.plan,cc3.cantidad_aprobadas"
			+ " from ("
			+ "	select legajo as legajo1, count(asignatura) as cursadas, plan_estudios as plan "
			+ "	from cursadas1_2003 "
			+ "	group by legajo,plan_estudios )"
			+ " cc1 left join ( "
			+ "	select legajo as legajo2, avg(calificacion) as promedio_aprobadas "
			+ "	from cursadas1_2003 "
			+ "	where calificacion<>0 "
			+ "	group by legajo ) cc2"
			+ " on (cc1.legajo1 = cc2.legajo2) inner join("
			+ "select legajo as legajo3, count(condicion) as cantidad_aprobadas "
			+ "from cursadas1_2003 "
			+ "where condicion in ('R','P')"
			+ "group by legajo"
			+ ") cc3 on (cc1.legajo1 = cc3.legajo3)"
			+ " group by legajo1, cursadas, promedio_aprobadas,plan, cantidad_aprobadas"
			+ " order by legajo1 asc"; 
	
	public LectorBD2(String nombreBD, String user, String password) {
		super(nombreBD, user, password);
	}
	
	public ArrayList<Estudiante> leerLegajoCursadasPromedio(){
		Statement stmt;
		Estudiante estudiante;
		ArrayList<Estudiante> lista = new ArrayList<Estudiante>();
		try {
			stmt = c.createStatement();
			 ResultSet rs = stmt.executeQuery( query1 );
			 while ( rs.next() ) {
		           Integer legajo = rs.getInt("legajo1");
		           Integer cursadas = rs.getInt("cursadas");
		           Double promedio = rs.getDouble("promedio_aprobadas");
		           Integer nroCarrera = rs.getInt("plan");
		           Integer aprobadas = rs.getInt("cantidad_aprobadas");
		           estudiante = new Estudiante(legajo,cursadas,promedio,nroCarrera,aprobadas);
		           lista.add(estudiante);
		        }
		} catch (SQLException e) {
			e.printStackTrace();
			this.cerrarConexion();
			return null;
		}
		return lista;
	}

	public void guardarEstudiantes(ArrayList<Estudiante> estudiantes) {
		Statement stmt;
		try {
			for(Estudiante e: estudiantes){
				//c.setAutoCommit(false);
				stmt = c.createStatement();
		        String sql = "INSERT INTO RENDIMIENTO_ESTUDIANTES (LEGAJO,COD_CARRERA,NOMBRE_CARRERA,CANTIDAD_CURSADAS,CANTIDAD_APROBADAS,PROMEDIO) VALUES ("
		        		+ e.getLegajo()+","
		        		+ e.getNroCarrera()+",'"
		        		+ e.getNombreCarrera()+"',"
		        		+ e.getCursadas()+","
		        		+ e.getAprobadads()+","
		        		+ e.getPromedio()
		        		+ ");";
		        stmt.executeUpdate(sql);
		        stmt.close();
		        //c.commit();
		        //System.out.println(sql);
			}
		} catch (SQLException e) {
			e.printStackTrace();
			this.cerrarConexion();
		}
	}

}
