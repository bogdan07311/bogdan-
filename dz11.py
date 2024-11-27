def powers_of_three():
    exponent = 0
    while True:
        yield 3 ** exponent
        exponent += 1
generator = powers_of_three()
for _ in range(10):
    print(next(generator))










