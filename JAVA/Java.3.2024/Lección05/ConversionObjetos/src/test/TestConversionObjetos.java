
package test;

import domain.*;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO);
        //System.out.println("empleado = "+ empleado);
        //System.out.println(empleado.obtenerDetalles());//si queremos acceder al método escritor
        //empleado.getTipoEscritura();//No se puede hacer
        //Downcasting
        //((Escritor)empleado).getTipoEscritura();//Tenemos 2 opciones, ésta es una
        Escritor escritor = (Escritor)empleado;//Esta es la segunda opción
        escritor.getTipoEscritura();
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
}
