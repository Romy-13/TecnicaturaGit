
import java.util.Scanner;


//Ejercicio clase 8: Rectángulo
//Se solicita calcular el área y el perímetro de un rectángulo,
//para esto deberemos crear las variables:
//Alto (int)
//Ancho (int)
//El usuario debe proporcionar los valores de alto,
//ancho y después se debe imprimir el resultado
public class clase8 {

    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite la altura del rectángulo: ");
        int alto = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el ancho del rectángulo: ");
        int ancho = Integer.parseInt(entrada.nextLine());
        //Fórmula
        var area = alto * ancho;
        var perimetro = (alto + ancho) * 2;
        var resultado1 = area;
        var resultado2 = perimetro;
        
        System.out.println("El área del rectángulo es: = " + resultado1);
        System.out.println("El perímetro del rectángulo es  = " + resultado2);
        
        //Ejercicio: El mayor de 2 números(Operador Ternario)
        System.out.println("Digite un número: ");
        var num1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite otro número: ");
        var num2 = Integer.parseInt(entrada.nextLine());
        var resultado = (num1 > num2) ? "num1" : "num2";
        System.out.println("El mayor es  = " + resultado);
        
        
        
    }

    
 
}
