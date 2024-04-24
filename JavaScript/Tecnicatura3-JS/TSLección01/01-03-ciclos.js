//while
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");

//do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("Fin del ciclo do while");

//For
for(let contando = 0; contando < 3; contando++){
    console.log(contando);
}
console.log("Fin del ciclo for")

//break(palabra reservada)
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando);//Mostramos todos los pares
        break;
    }
}
console.log("Termina el ciclo al encontrar el primer número par");

// Palabra continue y Etiquetas labels
inicio:

for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue inicio;// ir a la siguiente iteración    
    }
    console.log(contando);
}
console.log("Termina el ciclo");



