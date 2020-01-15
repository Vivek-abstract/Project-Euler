import numpy as np

def calculate_product(s):
    product = 1

    for i in range(len(s)):
        product *= int(s[i])

    return product

grid = []
line = input()
while line != "":
    row = list(map(int, line.split()))
    grid.append(row)
    line = input()

max_product = 1
grid = np.array(grid)
# Horizontal

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if j + 4 > len(grid[0]):
            break

        product = calculate_product(grid[i, j:j+4])
        if product > max_product:
            max_product = product

# Vertical

for i in range(len(grid[0])):
    for j in range(len(grid)):
        if j + 4 > len(grid):
            break

        product = calculate_product(grid[j:j+4,i])
        if product > max_product:
            max_product = product

# Diagonal upper left to lower right \

for i in range(len(grid)):
    for j in range(len(grid)):
        # Check if diagonal starting here to lower right exceeds bounds

        if i + 3 >= len(grid) or j + 3 >= len(grid):
            break

        elements = [grid[i+x][j+x] for x in range(4)]
        product = calculate_product(elements)
        if product > max_product:
            max_product = product

# Diagonal upper right to lower left

for i in range(len(grid)):
    for j in range(len(grid)-1, -1, -1):
        # Check if diagonal starting here to lower right exceeds bounds

        if j - 3 < 0 or i + 3 >= len(grid):
            break

        elements = [grid[i+x][j-x] for x in range(4)]
        product = calculate_product(elements)
        if product > max_product:
            max_product = product

print(max_product)