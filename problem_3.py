from math import *

# Sieve of Eratosthenes
# Returns list of primes less than or equal to n
def sieve_of_eratosthenes(n):
    square_root = ceil(sqrt(n))
    sieve = [True] * (n+1)

    for i in range(2, square_root):
        if sieve[i]:
            for j in range(i**2, n+1, i):
                sieve[j] = False

    primes = []
    for i, val in enumerate(sieve):
        if val and i >= 2:
            primes.append(i)

    return primes

n = 600851475143
square_root = ceil(sqrt(n))
primes = sieve_of_eratosthenes(square_root)

for i in reversed(primes):
    if n % i == 0:
        print(i)
        break