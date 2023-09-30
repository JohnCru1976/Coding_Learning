nombre = input("Dime tu nombre (Juan, Pedro u otro): ")
altura = int(input("Introduce tu altura en cms: "))

def control_altura(alt):
    if altura < 169:
        print("Eres demasiado pequeño")
    else:
        print("Tienes la altura adecuada")

if nombre == "Juan":
    print("Hola Juan")
    control_altura(altura)
elif nombre == "Pedro":
    print("Pedro no me cae muy bien")
    control_altura(altura)
else:
    print(f"Me caes bien {nombre}") 
    control_altura(altura)

