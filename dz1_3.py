import random
secret_number = random.randint(1, 10)
attempts = 3

print("Вгадайте число від 1 до 10! У вас є 3 спроби.")

for attempt in range(attempts):
    guess = int(input(f"Спроба {attempt + 1}: Введіть ваше число: "))

    if guess == secret_number:
        print("Вітаємо! Ви вгадали число!")
        break
    elif guess < secret_number:
        print("Більше.")
    else:
        print("Менше.")
else:
    print(f"На жаль, ви не вгадали. Загадане число було: {secret_number}.")