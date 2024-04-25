# Ejercicio 7 : Dada las horas trabajadas de 5 personas
# y la tarifa de pago. Calcular el salario y la sumatoria
# de todos los salarios
horas_trabajadas = []
tarifas_pago = []
for i in range(5):
    horas = float(input(f"Ingrese las horas trabajadas de la persona {i+1}: "))
    tarifa = float(input(f"Ingrese la tarifa de pago de la persona {i+1}: "))
    horas_trabajadas.append(horas)
    tarifas_pago.append(tarifa)
# Calcular el salario y la sumatoria de todos los salarios
sumatoria_salarios = 0
for i in range(5):
    salario = horas_trabajadas[i] * tarifas_pago[i]
    sumatoria_salarios += salario
    print(f"El salario de la persona {i+1} es: {salario}")
print("La sumatoria de todos los salarios es:", sumatoria_salarios)








