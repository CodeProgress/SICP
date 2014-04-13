
#Testing for Primality
#SICP 1.2.6
#http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.6
#

import random

def is_prime(n, times = 12):
    """Probabilistic function using Fermat's Little Theorem
    """
    if n < 2: return False
    for i in range(times):
        a = random.randint(1, n-1)
        if not pow(a, n, n) == a:
            return False
    return True


def is_prime_determ(n):
    """Brute force, deterministic
    O(x**.5)"""
    if n < 2:
        return False
    i = 2
    limit = int((n**.5)+1)
    while i < limit:
        if n % i == 0:
            return False
        i += 1
    return True



#Carmichael numbers
def is_prime_w_carm(n, times = 12, carmichaels = set()):
    """probabilistic function using Fermat's Little Theorem
    checks to see if n is a carmichael number (provide via carmichaels set)
    """
    if n in carmichaels: return False

    if n < 2: return False
    for i in range(times):
        a = random.randint(1, n-1)
        if not pow(a, n, n) == a:
            return False
    return True

def carmichaels(limit = 10000, times = 12):
    """returns a set of (very likely) carmichaels below limit"""
    cars = set()
    primes = [0]*(limit+1)
    for i in range(2, limit+1):
        if primes[i] == 1:
            if is_prime(i):
                cars.add(i)
            continue
        for j in range(i, limit+1, i):
            primes[j] = 1
            
    return cars

assert carmichaels(10000) == {561, 1105, 1729, 2465, 2821, 6601, 8911}


