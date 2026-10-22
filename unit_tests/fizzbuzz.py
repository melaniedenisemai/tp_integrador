def es_divisible(numero, divisor):
    return numero % divisor == 0


def fizzbuzz(numero):
    if es_divisible(numero, 3) and es_divisible(numero, 5):
        return 'FizzBuzz'
    if es_divisible(numero, 3):
        return 'Fizz'
    if es_divisible(numero, 5):
        return 'Buzz'
    return numero


def get_lista(numero):
    lista = []
    for i in range(1, numero + 1):
        lista.append(fizzbuzz(i))
    return lista
