from collections import deque
from math import sqrt

def p3():
    return last(factors(600851475143))

def factors(num):
    for i in range(2, int(sqrt(num))+2):
        while num%i == 0:
            num /= i
            yield i
            if num <= 1: return

def last(iterable):
    return deque(iterable, 1).pop()
