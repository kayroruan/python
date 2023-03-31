def calcularDesconto(valor, desconto = 0):
    valorComDesconto = valor - (valor * desconto)
    return valorComDesconto

valor1 = calcularDesconto(100)
valor2 = calcularDesconto(100, 0.25)

print(f"Valor do primeiro produto: {valor1}")
print(f"Valor do segundo produto: {valor2}")