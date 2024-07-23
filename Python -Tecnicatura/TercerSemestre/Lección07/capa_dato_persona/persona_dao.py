import logging

from Persona import Persona
from conecction import Conexion


class PersonaDAO:
    '''
    DAO significa: Data Access Object
    CRUD significa:
                    Create -> Insertar
                    Read   -> Seleccionar
                    Update -> Actualizar
                    Delete -> Eliminar
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

# Definimos el método clase
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                logging.debug(f'Persona insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores= (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                logging.debug(f"Persona actualizada: {persona}")
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                logging.debug(f"Los objetos eliminados son: {persona}")
                return cursor.rowcount

if __name__=='__main__':
    # Eliminar un registro
    #persona1 = Persona(id_persona=18)
    #persona_eliminadas = PersonaDAO.eliminar(persona1)
    #logging.debug(f"Personas eliminadas: {persona_eliminadas}")

    # Actualizar un registro
    #persona1 = Persona(1, "Juan Jose", "Pena", 'jjpena@gmail.com')
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #logging.debug(f"Personas actualizadas: {personas_actualizadas}")


    # Insertar un registro
    #persona1 = Persona(nombre='Homero', apellido='Romos', email='homero@gmail.com')
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #logging.debug(f'Personas insertadas: {personas_insertadas}')

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        logging.debug(persona)
