class PowerOfTwoIterator:
    def __init__(self):
        self.exponent = 0
    def __iter__(self):
        return self
    def __next__(self):
        result = 2 ** self.exponent
        self.exponent += 1
        return result
powers_of_two = PowerOfTwoIterator()
for _ in range(10):
    print(next(powers_of_two))