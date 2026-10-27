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
            for i in range(2, number):
                n = number / i
                if number % i == 0:
                    primefactors.append(int(i))
                    if n == i:
                        primefactors.append(int(n))
                print(primefactors)
            for j in primefactors:
                print('j: ', j)
                for k in range(2, j):
                    if j != 2:  # but instead is 4 for example
                        n_two = j / k  # so probably n_two = 2
                        if j % k == 0:
                            primefactors.append(int(k))
                            primefactors.remove(int(j))
                            if n_two == k:
                                primefactors.append(int(n_two))
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

def test_step7():
    primefactors.clear()
    step7 = generate_prime_factors(8)
    step7.sort()
    assert step7 == [2,2,2]

def test_step8():
    primefactors.clear()
    step8 = generate_prime_factors(9)
    step8.sort()
    assert step8 == [3,3]
