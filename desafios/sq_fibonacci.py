def fibonacci(number: int):
    """
    var: number, type: Integer
    resolution: a sequência de Fibonacci até o número fornecido ou op´ro.
    return: Lista contendo os termos da sequência de Fibonacci.
    """
    n_current = 1
    n_previous = 0
    sequence = []
    
    while len(sequence) < number:
        sequence.append(n_current)
        n_temp = n_current
        n_current += n_previous
        n_previous = n_temp

    return sequence


if __name__ == "__main__":

    # apoio/entendimento
    """
    O que é a sequência de Fibonacci e por que é chamada de 'código secreto da natureza': https://www.youtube.com/watch?v=cHZWZhHQq4g
    """
    
    n = int(input("Digite um valor para gerar a sequência de Fibonacci: "))
    
    result = fibonacci(number=n)

    print(f"Sequência de Fibonacci com {n} positivos: {result}")
    
    last_element = result[-1]
    penultimate_element = result[-2]
    
    print("\nA próxima sequência é a soma de: \n")
    
    print(" ################################################")
    print(f"ultimo valor: {last_element}")
    print(f"penultimo valor: {penultimate_element}")
    print(f"Primeiro_Numero_Superior é Igual a: {last_element + penultimate_element}")
    print(" ################################################")