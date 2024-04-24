
public class EjercicioWhile {

    public static void main(String[] args) {
        //ciclo while
        var conteo = 0; //Inferencia de tipo
        while (conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //vamos aumentando en uno la variable
        }
        //ciclo do while
        var contador = 0;
        do {
            System.out.println("contador = " + contador);            
            contador++;
        } while (contador <= 7);
        
        
        //ciclo for
        //uso de las palabras break y continue junto a la etiquetas(labels)
        
        for (var contando = 0; contando < 7; contando++) {
            if(contando % 2 == 0){
            }
            System.out.println("contando = " + contando);
            break;
        }
        for (var contando = 0; contando < 7; contando++) {
            if(contando % 2 != 0){
                continue;//vamos a la siguiente iteración
            }
            System.out.println("contando = " + contando);
            
        }
        //Etiquetas Labels
        inicio:
        for (var contando = 0; contando < 7; contando++) {
            if(contando % 2 == 0){
                continue inicio;
            }
             System.out.println("contando = " + contando);
                
            
        }
    }
}
