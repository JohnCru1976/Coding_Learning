name = input("Introduce tu nombre de vendedor: ")
sales = float(input("Introduce el valor total de tus ventas: "))
commission = sales * 0.13
print(f"{name}, el monto de tus comisiones es de {round(commission, 2)} €")
