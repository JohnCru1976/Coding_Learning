import datetime

fecha_actual = datetime.date.today()
anio = fecha_actual.year
mes = fecha_actual.month
dia = fecha_actual.day

print(f"Fecha actual: {fecha_actual}")
print(f"Dia: {dia}, mes: {mes}, año: {anio}")

# Mostra la hora actual
hora_actual = datetime.datetime.now().hour
minuto_actual = datetime.datetime.now().minute
print(hora_actual,minuto_actual,sep=":")

mi_hora = datetime.time(23,12,6)
print(mi_hora)
mi_dia = datetime.date(2022,10,12)
print(mi_dia)

mi_fecha = datetime.datetime(2024,12,1,23,10,12)
print(mi_fecha)
mi_fecha = mi_fecha.replace(month = 1)
print(mi_fecha)

# Tiempo entre dos fechas
fecha1 = datetime.date(1976,8,9)
fecha2 = datetime.date(2043,2,12)
intervalo = fecha2 - fecha1
print(intervalo)
print(intervalo.days)

# Tiempo entre dos fechas con hora
hora1 = datetime.datetime(2023,10,7,22,00)
hora2 = datetime.datetime(2023,10,8,6,00)
intervalo_hora = hora2 - hora1
print(intervalo_hora)

hora1 = datetime.datetime(1976,8,9)
hora2 = datetime.datetime(2057,2,12)
intervalo_hora = hora2 - hora1
print(intervalo_hora)
print(hora2.year - hora1.year)
