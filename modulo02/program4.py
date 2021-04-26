#Formateando cadenas

numero = 10/3
print("Resultado: " + str(numero))
print("Resultado: {n:1.2f}".format(n=numero))




variable = input("Dime tu nombre: ")
print("Dices que tu nombre es " + variable + ".")
print(f"Dices que tu nombre es {variable}.")
print("Dices que tu nombre es {}.".format(variable))
print("Dices que tu nombre es {n}.".format(n=variable))


