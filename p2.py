from itertools import takewhile

def p2():"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
    return sum(num for num in
               takewhile(lambda x: x<4000000, fib())
               if num%2 == 0)

def fib():
    a, b = 1, 2
    yield a
    while True:
        yield b
        a, b = b, a+b
