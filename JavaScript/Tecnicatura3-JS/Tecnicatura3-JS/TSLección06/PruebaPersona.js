class Persona{

    static contadorPersona = 0;
    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersona;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get idPersona(){
        return this._idPersona;
    }
    get nombre(){
        this._nombre;
    }
    
    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }
    get edad(){
        return this._edad;
    }
    set edad(edad){
        this._edad = edad;
    }
    toString(){
        return this._idPersona+' '+this._nombre+' '+this._apellido+' '+this._edad;
    }
}
class Empleado extends Persona{

    static contadorEmpleado = 0;

    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadorEmpleado;
        this._sueldo = sueldo;
    }

    get idEmpleado(){
        return this._idEmpleado;
    }
    get sueldo(){
        return this._sueldo
    }
    set sueldo(sueldo){
        this._sueldo = sueldo;
    }
    toString(){
        return super.toString()+' '+this._idEmpleado+' '+this._sueldo};
    
}

class Cliente extends Persona{

    static contadorCliente = 0;

    constructor(nombre, apellido, edad, fechaRegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorCliente;
        this._fechaRegistro = fechaRegistro;
    }

    get idCliente(){
        return this._fechaRegistro;
    }

    get fechaRegistro(){
        return this._fechaRegistro;
    }
    set fechaRegistro(fechaRegistro){
        this._fechaRegistro = fechaRegistro;
    }
    toString(){
        return super.toString()+' '+this._idCliente+' '+this._fechaRegistro;
    }
}
//Prueba clase Persona
let persona1 = new Persona('Juan', 'Perez',32);
console.log(persona1.toString());

let persona2 = new Persona('Carla', 'Ortega',22);
console.log(persona2.toString());

//Prueba clase Empleado
let empleado1 = new Empleado('Roman', 'Oviedo',18, 5000);
console.log(empleado1.toString());

let empleado2 = new Empleado('Fernando', 'Torres',40, 8000);
console.log(empleado2.toString());

//Prueba clase cliente
let cliente1 = new Cliente("Miguel", "Zala", 29, new Date());
console.log(cliente1.toString()); 

let cliente2 = new Cliente("Natalia", "Ortega", 22, new Date());
console.log(cliente2.toString());