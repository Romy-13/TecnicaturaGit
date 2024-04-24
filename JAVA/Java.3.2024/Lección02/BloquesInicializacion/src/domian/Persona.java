package domian;

public class Persona {
    private final int idPersona;
    private static int contadorPersona;
    
    static{//Bloque de inicializacion estático
        System.out.println("Ejecución del bloque estático");
        ++Persona.contadorPersona;
        //idPersona = 10; No es un atributo statico, por eso tenemos un error
    }
    {//Bloque de inicialización NO estático(contexto dinámico)
        System.out.println("Ejecución del bloque NO estático");
        this.idPersona = Persona.contadorPersona++;//Incrementamos el atributo
        
    }
    //Los bloques de inicialización se ejecuta antes del constructor
    
    public Persona(){
        System.out.println("Ejecución del constructor");
    }
    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
    
}
