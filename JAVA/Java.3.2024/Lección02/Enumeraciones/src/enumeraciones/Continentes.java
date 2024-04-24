
package enumeraciones;

public enum Continentes {
    AFRICA(54,"1.460 billones"),
    EUROPA(50, "741.651 billones"),
    ASIA(44, "1.9 billones"),
    AMERICA(34, "150.2 millones"),
    OCEANIA(14,"1.2 billones");
    
    private final int paises;
    private String habitantes;
    
    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }
    //Método Get
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
        return this.habitantes;
    }
}
