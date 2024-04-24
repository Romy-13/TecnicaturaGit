ingresos_mensuales = 81000
gastos_mensuales = 8000
#if anidados y else if(elif)
if ingresos_mensuales > 18000:
    if ingresos_mensuales-gastos_mensuales>0:
        print("Estás en deficit")
    elif ingresos_mensuales-gastos_mensuales>3000:
        print("Estás bien")
    else:
        print("Estás gastando de más")
elif ingresos_mensuales>1000:
    print("Estás bien en latinoámerica")
elif ingresos_mensuales>500:
    print("Estás bien en Argentina")
elif ingresos_mensuales>200:
    print("Estás bien en Venezuela")        