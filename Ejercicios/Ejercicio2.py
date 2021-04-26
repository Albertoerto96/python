#Inicio variables
distancia = input("¿Cuantos metros has recorrido?")
tiempo = input("¿Cuantos minutos has tardado?")

velocidad1 = (float(distancia)/float(tiempo))#metros/minuto
velocidad2 = velocidad1*0.06 #km/h
#Fin variables

print(velocidad2)

if(velocidad2<30):
    print("Velocidad moderada.")

elif(velocidad2>=75):
    print("Velocidad alta")

elif(velocidad2>=30):
    print("Velocidad media.")