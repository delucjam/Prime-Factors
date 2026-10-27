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

