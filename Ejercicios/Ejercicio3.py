numero = input("Dime un número: ")

if (numero.isdigit() == True) :
    print(f"Tabla del {numero}")
    for n in range(1,11):
        print(f"{n:2.0f} x {numero} = {(n*int(numero))}")

else:
    print(f"{numero}, no es un número.")