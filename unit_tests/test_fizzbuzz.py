import pytest
from fizzbuzz import fizzbuzz
#Imprimir por pantalla los números del 1 al 100 
# pero considerando lo siguiente: 
# a) Si el número es divisible por 3 se debe imprimir "Fizz". 
# b) Si el número es divisible por 5 se debe imprimir "Buzz". 
# c) Si el número es divisible por 3 y por 5 se debe imprimir "FizzBuzz"

def test_fizz():
    assert fizzbuzz(6) == 'Fizz'


def test_buzz():
    assert fizzbuzz(10) == 'Buzz'


def test_fizzbuzz():
    assert fizzbuzz(15) == 'FizzBuzz'
