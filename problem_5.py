# I have used table method of wikipedia
# https://en.wikibooks.org/wiki/Undergraduate_Mathematics/Least_common_multiple
# Keep dividing all numbers by prime numbers until all are equal to 1

elements = [x for x in range(1,21)]
prime_factors = []
divisors = [2,3,5,7,11,13,17,19]
k = 0
# print(elements)

while k < len(divisors):
    flag = False
    for i in range(len(elements)):
        if (elements[i] % divisors[k]) == 0 and (elements[i] / divisors[k]) != elements[i]:
            elements[i] = elements[i] // divisors[k]
            flag = True

    if flag:
        # print(elements)
        prime_factors.append(divisors[k])
    else:
        # If no change in elements, we increment k
        k += 1

# print(prime_factors)

product = 1
for e in prime_factors:
    product *= e

print(product)