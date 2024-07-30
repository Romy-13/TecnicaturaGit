import logging as log

# llamamos una configuración básica

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__=='__main__':
    log.debug('Mensaje a nivel debug')#Los mensajes de este nivel son
    # utilizados para información detallada y útil para diagnóstico.
    log.info('Mensaje a nivel info')# Proporciona información general
    # sobre el estado del programa o sus operaciones.
    log.warning('Mensaje a nivel warning')#Indica que algo inesperado pero
    # no necesariamente erróneo ha ocurrido, o una situación que
    # podría llevar a un problema en el futuro si no se corrige.
    log.error('Mensajea anivel error')#Indica que ha ocurrido un error que
    # debería ser investigado y corregido.
    log.critical('Mensaje a nivel critical')#Indica un error grave que ha
    # llevado al programa a un estado no recuperable, y que el programa
    # podría no continuar ejecutándose correctamente.

# Este código muestra cómo configurar y utilizar el módulo logging
# en Python para registrar mensajes de diferentes niveles
# (DEBUG, INFO, WARNING, ERROR, CRITICAL), lo cual es útil para
# el seguimiento, la depuración y la administración de
# aplicaciones Python.


#Esta línea configura el sistema de logging para que registre
# mensajes desde el nivel de DEBUG en adelante. Esto significa
# que todos los mensajes de DEBUG, INFO, WARNING, ERROR y CRITICAL
# serán registrados.


