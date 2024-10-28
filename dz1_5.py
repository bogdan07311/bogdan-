n = int(input("Введіть число n: "))
even_numbers = [str(num) for num in range(2, n + 1, 2)][::-1]
print(", ".join(even_numbers))