
package domain;


public class Gerente extends Empleado{
    private String departamentos;
    
    public Gerente(String nombre, double sueldo, String departamentos){
        super(nombre, sueldo);
        this.departamentos = departamentos;
    }
    
    //Sobre Escribimos los métodos
    @Override
    public String obtenerDetalles(){
        return super.obtenerDetalles()+", Departamento: "+this.departamentos;
    }
}
