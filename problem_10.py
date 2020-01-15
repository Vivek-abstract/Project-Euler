from math import *

# Sieve once again!
def generate_primes_upto(n):
    sieve = [True] * (n+1)

    for i in range(2, int(sqrt(n))+1):
        if sieve[i]:
            for j in range(i**2, n+1, i):
                sieve[j] = False

    sieve[0] = False
    sieve[1] = False

    primes = [i for (i, x) in enumerate(sieve) if x]

    return primes

print(sum(generate_primes_upto(2000000)))