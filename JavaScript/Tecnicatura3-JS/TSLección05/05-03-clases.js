//let persona3 = new Persona('Carla', 'Ponce'); esto no se hace: Persona is not definida

class Persona{//clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
    get nombre(){
        return this._nombre;
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

}

class Empleado extends Persona{//Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;

    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }

}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
persona1.nombre = "Juan Carlos";
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = "Maria Laura";
console.log(persona2.nombre);
//console.log(persona2);

//Aquí deben completar una tarea asignada en el video:
//Crear el método get y set para el atributo de apellido, luego modificar el apellido a través del  set y mostrar con un console.log lo que es el get donde muestra el resultado obtenido.
console.log(persona1.apellido);
persona1.apellido = 'Rodriguez';
console.log(persona1.apellido);

console.log(persona2.apellido);
persona2.apellido = "Torres";
console.log(persona2.apellido);

let empleado1 = new Empleado('Romina', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombre);