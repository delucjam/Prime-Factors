"""
Python 2: Assignment 3  James DeLuca
"""
from pytest import raises
import math

def generate_prime_factors(number):
    if type(number) == int:
        pass
    else:
        raise ValueError('Incorrect data type')

def test_step1():
    with raises(ValueError):
        generate_prime_factors('three')

