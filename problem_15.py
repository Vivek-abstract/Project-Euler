# Dynamic programming problem
# Can be divided into overlapping subprograms
# No of possible ways to reach (i,j) = no(i-1, j) + no(i, j-1)

cache = {}

def update_cache(i, j, val):
    if i in cache:
        cache[i][j] = val
    else:
        cache[i] = {}
        cache[i][j] = val

def number_of_ways(i, j):

    if i in cache:
        if j in cache[i]:
            return cache[i][j]

    if i == 0 or j == 0:
        update_cache(i,j,1)
        return cache[i][j]
    
    val = number_of_ways(i-1, j) + number_of_ways(i, j-1)
    update_cache(i,j, val)
    
    return cache[i][j]

print(number_of_ways(20,20))