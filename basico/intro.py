#Print básico e calculo básico
nome = input("Digite seu nome: ")
nascimento = int(input("Digite seu ano de nascimento: "))

def calcularIdade():
    return 2023 - nascimento

idade = calcularIdade()

print(f"Olá {nome}, você terá {idade} anos de idade até o final deste ano")