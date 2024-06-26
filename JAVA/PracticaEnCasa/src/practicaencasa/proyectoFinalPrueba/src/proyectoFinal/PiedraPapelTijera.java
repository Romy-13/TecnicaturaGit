

package proyectoFinal;


import java.util.Random;
import java.util.Scanner;

public  class PiedraPapelTijera {

    public static void main(String[] args) {
        //Creamos una clase Scanner para ingresar los datos por teclado
        try (Scanner entrada = new Scanner(System.in)) {
            // Random para generar un número entero aleatorio entre ciertos límites 
            Random random = new Random();
            // Creamos nuestras variables enteras
            int jugador, computadora, resultadoJugador = 0, resultadoComputadora = 0;
            // Imprimimos el inicio del juego
            System.out.println("Bienvenidos al Juego de Piedra, Papel y Tijera");
            System.out.println(" ");
            // Para el desarrollo del juego utilizamos un Ciclo for para las 3 rondas
            for (int ronda = 1; ronda <= 3; ronda++) {
                // Imprimimos la primer ronda  y las opciones que debe elegir el jugador
                System.out.println("\nRonda " + ronda);
                System.out.println("Elije una opción:");
                System.out.println(" ");
                System.out.println("1. para Piedra");
                System.out.println("2. para Papel");
                System.out.println("3. para Tijera");
                
                // Leer la elección del jugador
                jugador = Integer.parseInt(entrada.nextLine());
                System.out.println("");
                
                // Mostramos la elección del jugador con un ciclo if e imprimimos 
                if (jugador >= 1 && jugador <= 3) {
                    System.out.println("Elegiste " + jugador);
                    System.out.println("Jugador elige: " + getOpcion(jugador));
                } else {
                    System.out.println("Opción no válida");
                    continue; // Volver al inicio del ciclo si la opción es inválida
                }
                
                // Generamos la elección aleatoria de la computadora e imprimimos
                computadora = random.nextInt(3) + 1;
                System.out.println("Computadora elige: " + getOpcion(computadora));
                
                // Determinar el resultado de la ronda y actualizar los puntos
                int resultadoRonda = determinarResultado(jugador, computadora);
                if (resultadoRonda == 1) {
                    resultadoJugador++;
                } else if (resultadoRonda == -1) {
                    resultadoComputadora++;
                }
                
                // Mostrar el resultado de la ronda
                switch (resultadoRonda) {
                    case 0 -> System.out.println("Empate en esta ronda.");
                    case 1 -> System.out.println("Jugador gana esta ronda.");
                    case -1 -> System.out.println("Computadora gana esta ronda.");
                    default -> {
                    }
                }
            }   // Determinar al ganador general
            System.out.println("\n--- Resultado Final ---");
            System.out.println("Puntos del Jugador: " + resultadoJugador);
            System.out.println("Puntos de la Computadora: " + resultadoComputadora);
            if (resultadoJugador > resultadoComputadora) {
                System.out.println("¡Jugador gana el juego!");
            } else if (resultadoJugador < resultadoComputadora) {
                System.out.println("¡Computadora gana el juego!");
            } else {
                System.out.println("El juego termina en empate.");
            }
            System.out.println("¡¡¡FIN DEL JUEGO!!!");
            // Cerrar el escáner
        }
    }

    // Función para obtener la opción seleccionada como cadena
    public static String getOpcion(int opcion) {
        return switch (opcion) {
            case 1 -> "Piedra";
            case 2 -> "Papel";
            case 3 -> "Tijera";
            default -> "Opción no válida";
        };
    }

    // Función para determinar el resultado de la ronda
    public static int determinarResultado(int jugador, int computadora) {
        if (jugador == computadora) {
            return 0; // Empate
        } else if ((jugador == 1 && computadora == 3) || (jugador == 2 && computadora == 1) || (jugador == 3 && computadora == 2)) {
            return 1; // Jugador gana
        } else {
            return -1; // Computadora gana
        }
    }

}
