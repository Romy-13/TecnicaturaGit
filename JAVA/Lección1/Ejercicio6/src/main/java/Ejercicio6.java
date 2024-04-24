
import java.util.Scanner;

public class Ejercicio6 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo;
        float luis;
        float juan;
        float total;
        System.out.println("Digite la cantidad de dinero que tiene Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());

        luis = guillermo / 2;
        juan = (luis + guillermo) / 2;
        total = luis + guillermo + juan;
        System.out.println("\nEl dinero de Luis es: $" + luis);
        System.out.println("\nEl dinero de Juan es: $ " + juan);
        System.out.println("\nEl total del dinero entre los tres es: $" + total);
        

    }
}
