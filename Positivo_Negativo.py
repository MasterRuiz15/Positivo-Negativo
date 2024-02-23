# Programa para verificar si un numero es positivo o negativo

# input
X = int(input("Digite un numero: "))

# processing
if X > 0:
    RTA = "POSITIVO"
elif X == 0:
    RTA = "Su numero es neutro"
else:
    RTA = "NEGATIVO"

# output
print("El numero",X," es: ", RTA)