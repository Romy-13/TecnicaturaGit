
package test;

import domain.Persona;

public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5, 6, 7, 9};//Sintaxis resumida
        //for (int i = 0; i < edad.length; i++){//Sintaxis resumida del ciclo for
        for (int edad: edades){//Sintaxix del forEach
            System.out.println("edad = "+edad);
        } 
         
        Persona personas[] = {new Persona("Romina"), new Persona("Carla"), new Persona("Javier")};
         
        //ForEach
        for(Persona persona: personas){
            System.out.println("persona = "+ persona);
            
        }
         
         
            
        
        
    }
}
