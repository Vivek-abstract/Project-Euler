sum_of_squares = 0
square_of_sum = 0
sum = 0

for i in range(1, 101):
    sum_of_squares += i**2
    sum += i

square_of_sum = sum ** 2

print(square_of_sum - sum_of_squares)