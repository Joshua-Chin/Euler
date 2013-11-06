import numpy as np

def p7():
    return oddprimes(1000000)[9999]

def oddprimes(num):
    isprimes = np.ones(num//2 + 1, dtype = np.bool)
    isprimes[0] = False
    for index, isprime in enumerate(isprimes):
        if isprime:
            isprimes[2*index*(index+1)::2*index+1] = False
    return 2*np.nonzero(isprimes)[0] + 1
