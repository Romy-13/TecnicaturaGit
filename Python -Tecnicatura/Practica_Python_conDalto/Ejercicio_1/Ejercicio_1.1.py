#a)-Diferencia en porcentaje entre el curso actual y:
#-el más rapido de otros cursos
#-el más lento de otros cursos
#-el promedio de los cursos

#b)-Porcentaje de material inservible que se reduce en:
#-el promedio de los cursos
#-el curso actual(este curso)

#c)-Ver 10 horas de este curso equivale?¿y al revés?

#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max =7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duración de crudo
crudo_promedio = 5
crudo_dalto = 3.5

#Diferncia de duración
diferencia_con_min = 100 - dalto_curso/otros_cursos_min *100
diferencia_con_max = 100 - dalto_curso *1000 //otros_cursos_max *10
diferencia_con_promedio =100 - dalto_curso/otros_cursos_promedio*100

#Calculando el tiempo vacio removido
tiempo_vacio_promedio = 100- otros_cursos_promedio * 1000 // crudo_promedio/ 10
tiempo_vacio_dalto = 100-dalto_curso*1000//crudo_dalto/10

print("---------------------------")
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el más rápido")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el más rápido")
print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el más rápido")
print("-----------------------------")

#Mostrando la cantidas de espacio vacio que se remueve (ejercicio b)
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso elimino un {tiempo_vacio_dalto} % de tiempo vacio")
print("----------------------------")

#Mostrando la diferencia si los cursos duran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cusros")
print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} de este curso")
print("-----------------------------")