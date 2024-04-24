
import java.util.Scanner;

public class EjercicioLibro {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Dijite el ID del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Digete el valor del libro: ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Indique si el envio es gratuito (true/false): ");
        boolean envioGratis = entrada.nextBoolean();

        System.out.println(nombreLibro + "  #" + idLibro);
        System.out.println("Precio del libro:  $" + precioLibro);
        System.out.println("El envio del libro es gratis? : " + envioGratis);

    }

}
