from datetime import datetime
import time

fecha=input("Dime tu fecha de nacimiento: ")
dt2=datetime.now().date()
dt3=datetime.strptime(fecha, "%d-%m-%Y").date()
años=dt2.year - dt3.year
falta=18 - años

if(años>18):
    print(f"Tienes {años} eres mayor de edad.")
elif(años<18):
    print(f"Te faltan {falta} años para ser mayor de edad.")