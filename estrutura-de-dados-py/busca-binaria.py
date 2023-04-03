def busca_binaria(lista, elemento):
        minimo = 0 
        maximo = len(lista) - 1
        encontrado = False
    
        while minimo <= maximo and not encontrado:
            meio_lista = (minimo + maximo) // 2
            if lista[meio_lista] == elemento:
                encontrado = True
            else:
                if elemento < lista[meio_lista]:
                    maximo = meio_lista - 1
                else:
                    minimo = meio_lista + 1
    
        if encontrado == True:
            return "Encontrado!"
        else:
             return "Não encontrado :("
    
testelista = range(1, 15)
print(busca_binaria(testelista, 6))
    
#Exemplo de busca binária