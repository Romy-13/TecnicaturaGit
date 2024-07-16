import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while(true) {//ciclo infinito
            System.out.println("******** Aplicación Calculadora *******");
            mostrarMenu();
            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {
                    ejecutarOperacion(operacion, entrada);
                }//Fin del if
                else if (operacion == 5) {
                    System.out.println("Hasta pronto...");
                    break;//rompe el ciclo y sale
                } else {
                    System.out.println("Opción erronea: " + operacion);
                }
                //Imprimimos un salto de linea
                System.out.println();
            }catch (Exception e){//Fin try, comienzo catch
                System.out.println("Ocurrio un error: "+ e.getMessage());
                System.out.println();
            }//Fin catch
        }//fin while
    }//Fin main

    private static void mostrarMenu(){
        //Mostramos el menú
        System.out.println("""
                    1. Suma
                    2. Resta
                    3. Multiplicacion
                    4. Division
                    5. Salir
                    """);
        System.out.println("Operación a realizar: ");
    }//Fin método mostrarMenu

    private static void ejecutarOperacion(int operacion, Scanner entrada){
        System.out.print("Digite el valor para el operando1: ");
        var operando1 = Double.parseDouble(entrada.nextLine());
        System.out.print("Digite el valor para el operando2: ");
        var operando2 = Double.parseDouble(entrada.nextLine());
        double resultado;
        switch (operacion) {
            case 1 -> {// SUMA
                resultado = operando1 + operando2;
                System.out.println("Resultado de la suma: " + resultado);
            }
            case 2 -> {//RESTA
                resultado = operando1 - operando2;
                System.out.println("Resultado de la resta: " + resultado);
            }
            case 3 -> {//MULTIPLICACIÓN
                resultado = operando1 * operando2;
                System.out.println("Resultado de la multiplicación es: " + resultado);
            }
            case 4 -> {//DIVISIÓN
                resultado = operando1 / operando2;
                System.out.println("Resultado de la división: " + resultado);
            }
            default -> System.out.println("Opción erronea: " + operacion);
        }//Fin swith
    }//Fin método ejecutarOperacion
}//Fin clase
