def p9():
    return next(a*b*(1000-a-b)
                for a in range(1, 1001)
                for b in range(1, 1001-a)
                if a**2 + b**2 == (1000-a-b)**2)
