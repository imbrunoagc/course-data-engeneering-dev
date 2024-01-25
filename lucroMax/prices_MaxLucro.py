def calcularLucro(listPrices):
    
    # Se o tamanho da lista for menor que 1 o retorno do lucro é 0.
    if len(listPrices) < 1:
        return 0 
    
    # Definição de maxPreço e Menor(Sendo o primeiro elemento da lista)
    lucroMax = 0
    precoMin = listPrices[0]
    print("primeiro elemento: ", precoMin)

    for preco in listPrices:
        
        # Valor minimo encontrado na lista, após o primeiro elemento
        precoMin = min(preco, precoMin)
        
        # Verificando se a venda atual pode ser feita com base no preço mais baixo encontrado até agora.
        LucroAtual = preco - precoMin
        
        # Atualizando o maior lucro caso encontre um maior.
        lucroMax = max(lucroMax, LucroAtual)

    
    return lucroMax 


if __name__ == "__main__":
    
    prices_1 = [7, 1, 5, 3, 6, 4]
    
    prices_2 = [8, 2, 6, 4, 7, 5]
    
    lucro = calcularLucro(prices_2)
    
    print(lucro)
    
### Ambas as listas resultaram no maior lucro de 5.
