nome = ["maçã", "banana", "laranja"]

for c in nome:
    print(c)

#Espaçamento
print("")    

nome2 = "kayro"
for i, c in enumerate(nome2):
    print(f"Posição = {i}, valor = {c}")

#Espaçamento
print("")  

for x in range(3):
    print(x)

#Espaçamento
print("")  

disciplina = "Linguagem de Programação"
for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)
