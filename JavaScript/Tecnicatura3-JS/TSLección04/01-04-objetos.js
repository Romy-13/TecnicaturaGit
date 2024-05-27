let x = 10; //varible tipo primitivo
console.log(x.lenght);
console.log("tipos primitivos");

// Objeto
let persona ={
    nombre: "Romina",
    apellido: "Rodriguez",
    email: "romi@gmail.com",
    edad: 28,
    idioma: "ES",
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){//Método o función
        return this.nombre+" "+this.apellido;
    },
    get nombreEdad(){
        return 'El nombre es: '+this.nombre+', edad: '+this.edad;
    },

}
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.edad);
console.log(persona.email);
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");

let persona2 = new Object();//debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "2613458790";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona["apellido"]);//accedemos como si fuera un arreglo
console.log("Usamos un ciclo for");

//For in y accedemos al objeto como un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
console.log("comabiamos y eliminamos un error");

persona.apellida = "Betancud";//cambiamos dinamicamente un valor del objeto
delete persona.apellida;//borramos el error que teniamos
console.log(persona);

//Distinta formas de imprimir un objeto
//Numero 1: la más sencilla: concatenar cada valor de cada propiedad
console.log("//Distinta formas de imprimir un objeto: forma1");
console.log(persona.nombre+" "+persona.apellido);

//Número 2: a traves del ciclo for
console.log("//Distinta formas de imprimir un objeto: forma 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Número 3: La función objet.value()
console.log("Distinatas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);

// Número 4: Utilizamos el método JSON.srtingify
console.log("//Distinta formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("Comenzamos a ver el método get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el método get y set para idioma");
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){//constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3("Leo", "Lopez", "lopez1@gmail.com");
padre.nombre = "Luis";//modificamos el nombre
padre.telefono = "265478098";//una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto());//Utilizamos la función


let madre = new Persona3("Laura", "Contrera", "laucont@gmail.com");
console.log(madre);
console.log(madre.telefono);
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
//caso objeto 1
let miObjeto = new Object();//Esta es una opción formal
//caso objeto 2
let miObjeto2 = {};//Esta opción es breve y recomendada

//Caso String 1
let miCadena1 = new String("Hola");//Sintaxis formal
//Caso String 2
let miCadena2 = "Hola";//Esta es una sintaxis simplificada y recomendada

//Caso con números 1
let miNumero = new Number(1);//Es formal no recomendable
//Caso con números 2
let miNumero1 = 1;//sintaxis recomendada

//Caso boolean 1
let miBolean1 = new Boolean(false);//Formal
//caso boolean 2
let miBolean2 = false;//sintaxis recomendada

//Caso arreglos 1
let miArreglo1 = new Array();//formal
//caso arreglos 2
let miArreglo2 = [];//sintaxis recomendada

//Caso function 1
let miFuncion1 = new function(){};//Todo despues de new es considerado objeto
//caso function 2
let miFuncion2 = function(){};//notacion simplificada y recomendada

//uso prototype
Persona3.prototype.telefono = "2613462778";
console.log(padre);
console.log(madre);
madre.telefono = "251347897";
console.log(madre);

//Uso de call
let persona4 = {
    nombre:"Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, telefono){
        return titulo+": "+this.nombre+" "+this.apellido+" "+telefono;
        //return this.nombre+' '+this.apellido;
    }

}
let persona5 = {
    nombre: "Carlos",
    apellido: "Lara"
}
console.log(persona4.nombreCompleto2('Lic.', '23897654'));
console.log(persona4.nombreCompleto2.call(persona5, "Ing.","2783425788"));

//Método Apply
let arreglo =['Ing', '243675893']
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));