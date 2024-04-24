
import java.util.Scanner;

public class HolaMundo {

    private static int var;

    public static void main(String[] args) {
        /*  System.out.println("Hola mundo java"); 
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
         */

        //Var - inferencia de tipo en java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //souyv + tab
        //Para ejecutar shift + F6 la tecla para mayús
        //Regla para definir una variable en Java*/

 /*var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //Ejercicio: Caracteres especiales en java
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n" + nombre);//Diagonal inversa y letra n:salto de linea
        System.out.println("tabulador: \t" + nombre);//Tabulador: espacio para centrar
        System.out.println("\t \t.:MENÚ:.");
        System.out.println("Retroceso: \b"+nombre);//Retroceso:retrocede un espacio o más
        System.out.println("Comillas simples: \'"+nombre+"\'");
        System.out.println("Comillas dobles: \""+nombre+"\"");*/
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 =" + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado; " + titulo2 + " " + usuario2);*/
 /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte:" + Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte:" + Byte.MAX_VALUE);

        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("valor minimo del short:" + Short.MIN_VALUE);
        System.out.println("valor minimo de short:" + Short.MAX_VALUE);

        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("valor minimo de int:" + Integer.MIN_VALUE);
        System.out.println("valor maximo de int:" + Integer.MAX_VALUE);

        long numEnteroLong = 10;
        System.out.println("numEnteroLong =" + numEnteroLong);
        System.out.println("valor minimo de long:" + Long.MIN_VALUE);
        System.out.println("valor maximo de long:" + Long.MAX_VALUE);

        float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("valor minimo de float:" + Float.MIN_VALUE);
        System.out.println("valor maximo de float:" + Float.MAX_VALUE);

        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("valor minimo de double:" + Double.MIN_VALUE);
        System.out.println("valor maximo de double:" + Double.MAX_VALUE);*/
        //Inferencia de tipo var y tipos primitivos
        /*var numEntero = 20;//Las literales sin punto automáticamente son de tipo int
        System.out.println("numEntero = "+ numEntero);
        var numFloat = 10.0F;// Automáticamente con el punto se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numdouble = " + numDouble);*/
        //Tipos primitivos char
        /*char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        var varCaracter1 = '\u0024';
        System.out.println("varCaracter1 = " + varCaracter1);//Indicamos a Java el codigo inicode
        var varDecimal1 = (char)36;//valor entero, le asigna valor int
        System.out.println("varDecimal1 = " + varDecimal1);
        var varCaracterSimbolo1 = '$';//Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int varCaracter = 'b';
        System.out.println("varCaracter = " + varCaracter);*/
 /*
        //Tipos Primitivos tipoa Booleanos
        var varBool = false;
        System.out.println("varBool = " + varBool);
        
        if(varBool) {
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");
        }
          
        //Algorítmo ¿es mayor de edad?
          var edad = 15;//Literal tener
          var adulto = edad >= 18;//Esta es una expreción boleana
          if (adulto){
              System.out.println("Eres mayor de edad");
          }
          else {
              System.out.println("Eres menor de edad");*/
//        /*//Converción de Tipos Primitivos
//        var edad = Integer.parseInt("20");
//        System.out.println("edad = " + edad);
//        var valorPi = Double.parseDouble("3.1416");
//        System.out.println("valorPi = " + valorPi);
//        
//        //Pedir un valor
        var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad: ");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);*/

        //Converción tipo primitivo en Java 2 (convertir un tipo entero a string)
        /*var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "Programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);*/
 /*int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion);
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 de la division = " + solucion2);
        
        solucion = num1 % num2;//guarda el residuo entero de la division
        System.out.println("solucion2 = " + solucion2);
        
        if (num1 % 2 == 0)
            System.out.println("Es un numero par");
        else
            System.out.println("Es un numero impar");*/
 /*int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;//Una operación
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1;//varNum1 = varNum1 +1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 -= 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 *= 2;
        System.out.println("varNum2 = " + varNum2);
        
        varNum2 %= 2;
        System.out.println("varNum2 = " + varNum2);
        
        varNum3 /= 2;
        System.out.println("varNum3 = " + varNum3);*/
        //Clase 8
        //Operadores Unarios: cambio de signos
        /*var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);//El resultado será negativo
        
        //Operador de negación
        var varC = true;//Esta literal por defoult en Java es de tipo boolena
        var varD = !varC;//Aquí esta invirtiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores unarios de Incremento: Preincremento
        var varE = 9; //se va a modificar su valor
        var varF = ++varE; //simbolo antes de la variable
        //priemero se incrementa la variable y después su valor
        System.out.println("varE = " + varE);//se incremanta en la unidad
        System.out.println("varF = " + varF);// va a sumar uno
        
        //Posincremento(el simbolo va después de la variable)
        var varG = 3;
        var varH = varG++;//primero el valor de la variable y luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //Operadores unarios de decremento: predecremento
        var varI = 4;
        var varJ = --varI;//la variable ya esta con decremento
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);
        
        //Posincremento
        var varK = 8;
        var varL = varK--;//primero la variablee, luego el decremento
        System.out.println("varK = " + varK);//aqui va a decrementar uno
        System.out.println("varL = " + varL);*/
        //Operadores de igualdad y relacionales
        /*var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);

        var cadenaA = "HELLO";
        var cadenaB = "HELLO";
        var cadenaC = cadenaA == cadenaB;
        System.out.println("cadenaC = " + cadenaC);

        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);

        var gVar = aNum >= bNum;
        System.out.println("gVar = " + gVar);

        if (bNum % 2 == 0) {
            System.out.println("Es número par");
        } else {
            System.out.println("El núero es impar");
        }

        var edad = 30;
        var adulto = 18;
        if (edad > adulto) {
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Es menor de edad");*/
        //Operadores Condicionales (and &&)
        /*var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");

        }
        //Operador condicional (or ||)

        var vacaciones = true;
        var diaLibre = false;
        if (vacaciones || diaLibre) {
            System.out.println("Papa puede asistir al juego de su hijo");
        } else {
            System.out.println("Ppapa no puede asistir al juego de su hijo");
            
        }*/
        
        //Operador Ternario
        
        /*var resultadoT = (5 > 4) ? "Verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numT = 4;
        resultadoT = (numT % 2 == 0) ? "Es par" : "Es impar";
        System.out.println("resultadoT = " + resultadoT);*/
        
        /*var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);//6
        System.out.println("y = " + y);//9
        System.out.println("z = " + z);//16
        
        var solucionAritmetica = 4 + 5 * 6 / 3; // 4 + ((5 * 6) / 3)= 30 /3 = 10+4=14
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3; // 9 * 6 = 54/3=18
        System.out.println("solucionAritmetica = " + solucionAritmetica);
*/

    }

}
