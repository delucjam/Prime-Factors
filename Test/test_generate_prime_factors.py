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
            return primefactors
        elif number > 1 < 3:
            primefactors.append(number)
            return primefactors
        else:
            pass
    else:
        raise ValueError('Incorrect data type')

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

