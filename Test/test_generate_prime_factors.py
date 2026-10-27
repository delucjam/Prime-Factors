"""
Python 2: Assignment 3  James DeLuca
"""
from pytest import raises
import math

primefactors = []

def generate_prime_factors(number):
    if type(number) == int:
        pass
        if number == 1:
            primefactors.clear()
        if 1 < number < 4:
            primefactors.append(number)
        else:
            print('checking for prime factors\n')
            for i in range(2, number):
                if number % i == 0: #if number is divisible by i, therefore is a factor of number
                    n = int(number / i)
                    print('n: ',n)
                    primefactors.append(n)
                    if i * i == number:
                        primefactors.append(int(i))
                else:
                    pass
    else:
        raise ValueError('Incorrect data type')
    return primefactors

def test_step1():
    with raises(ValueError):
        generate_prime_factors('three')

def test_step2():
    step2 = generate_prime_factors(1)
    assert step2 == []

def test_step3():
    step3 = generate_prime_factors(2)
    assert step3 == [2]

def test_step4():
    primefactors.clear()
    step4 = generate_prime_factors(3)
    assert step4 == [3]

def test_step5():
    primefactors.clear()
    step5 = generate_prime_factors(4)
    assert step5 == [2, 2]

def test_step6():
    primefactors.clear()
    step6 = generate_prime_factors(6)
    step6.sort()
    assert step6 == [2, 3]

