from math import *

# Generator that generates triangle numbers
def triangle_numbers():
    x = 1
    i = 1
    yield x
    while True:
        i += 1
        x += i
        yield x

# Returns number of factors of a number
# First we find the prime factors of the number
# Then we multiply the distinct exponents + 1 to get number of factors

def number_of_factors(n, primes):
    prime_factors = {}
    i = 0
    while n != 1:
        if n % primes[i] == 0:
            try:
                prime_factors[primes[i]] += 1
            except KeyError:
                prime_factors[primes[i]] = 1
        
            n = n / primes[i]
        else:
            i += 1

    n = 1
    for factor_exponent in prime_factors.values():
        n *= (factor_exponent+1)

    return n

# Algorithm to generate primes
def generate_primes_upto(n):
    
    sieve = [True] * (n+1)

    for i in range(2, int(sqrt(n))+1):
        if sieve[i]:
            for j in range(i**2, n+1, i):
                sieve[j] = False

    sieve[0] = False
    sieve[1] = False

    primes = [i for (i, x) in enumerate(sieve) if x == True]

    return primes

count = 0
primes = generate_primes_upto(100000)

for i in triangle_numbers():
    num_factors = number_of_factors(i, primes)

    if num_factors >= 500:
        print(i)
        break

    