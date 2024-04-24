package Ejercicio4;

import java.util.Scanner;

public class Ejercicio4 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número entre 0 y 10: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var calificacion = "Desconocida";
        switch (numero) {
            case 10:
                calificacion = "A";
                break;
            case 9:
                calificacion = "B";
                break;
            case 8:
                calificacion = "C";
                break;
            case 7:
                calificacion = "D";
                break;
            case 6:
                calificacion = "F";
        }
        System.out.println("calificacion = " + calificacion);
    }
}
