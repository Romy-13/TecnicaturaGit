
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo",57.000, false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre()); 
        System.out.println("persona1 = " + persona1);
        //Modificar a través de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre);//Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre()); 
        System.out.println("persona1 = " + persona1);
    }   
    
}
