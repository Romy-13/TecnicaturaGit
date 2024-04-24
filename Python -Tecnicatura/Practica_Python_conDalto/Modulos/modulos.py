# importando un modulo y asignando el nombre "m_saludar"
# import modulo_saludar as m_saludar

# desde ese modulo, importamos 2 modulos y les cambiamos el nombre
from modulo_saludar import saludar as saludar_normal, saludo_raro as saludar_mal

# creamos las variables con los saludos y agregamos los nombres
saludo = saludar_normal("Fernando")
saludo_raro = saludar_mal("Leo")

# mostramos en pantalla
print(saludo)
print(saludo_raro)
