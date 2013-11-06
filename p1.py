def p1():
    return sum(x for x in range(1000)
               if x%5 == 0 or x%3 == 0)
