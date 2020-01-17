import sys
sys.setrecursionlimit(100000)

cache = {1: 1}

# Returns length of Collatz sequence for n 
def length_of_sequence(n):

    if n in cache:
        return cache[n]

    if n == 1:
        return 1

    if n % 2 == 0:
        cache[n] = length_of_sequence(n // 2) + 1
        return cache[n]
    else:
        cache[n] =  length_of_sequence(3*n + 1) + 1
        return cache[n]

longest_chain = 0
longest_chain_start = 0
for x in range(1,1000001):
    length = length_of_sequence(x)
    if length > longest_chain:
        longest_chain = length
        longest_chain_start = x

print(longest_chain_start)