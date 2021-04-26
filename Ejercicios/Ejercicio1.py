from datetime import datetime

#Variables
fecha = input("Dime tu fecha de nacimiento: ")
dt2 = datetime.now().date()
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date()
años = dt2.year - dt3.year

if(años >= 18):
    print(f"Tienes {años} eres mayor de edad.")
elif(años < 18):
    falta = 18 - años
    print(f"Te faltan {(18 - años)} años para ser mayor de edad.")