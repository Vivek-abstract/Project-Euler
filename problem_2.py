def fibonacciGenerator():
    a = 1
    b = 2

    yield a
    yield b

    while a+b <= 4000000:
        c = a + b
        a = b
        b = c
        yield c

sum = 0
for n in fibonacciGenerator():
    if n % 2 == 0:
        sum += n
    
print(sum)
