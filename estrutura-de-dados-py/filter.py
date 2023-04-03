numeros = list(range(0, 15))

numerosImpares = list(filter(lambda x: x % 2 == 1, numeros))
numerosPares = list(filter(lambda x: x % 2 == 0, numeros))


print(numeros)
print(numerosImpares)
print(numerosPares)

#Listagem de número pares e ímpares com conceito de filter