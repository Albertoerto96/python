from datetime import datetime
import time

datenow1 = datetime.now().date()
datenow2 = datetime.now()

print("Fecha1:", datenow1)
print("Fecha2:", datenow2.strftime("%d-%m-%Y %H:%M"))
print("Time: ", time.asctime())

#print("Escribe tu fecha de nacimiento: ")
fecha = input("Escribe tu fecha de nacimiento: ")
datenow3 = datetime.strptime(fecha, "%d-%m-%Y").date()      #Y-4 caracteres, y-2 caracteres
años = datenow1.year - datenow3.year

print("Fecha3: ", datenow3.strftime("%A, %d %b %Y"))
print(f"Tienes {años} años.")

