score = int(input("Введіть кількість балів на екзамені (0-100): "))
if 0 <= score < 50:
    grade = "незадовільно"
elif 50 <= score < 70:
    grade = "задовільно"
elif 70 <= score < 90:
    grade = "добре"
elif 90 <= score <= 100:
    grade = "відмінно"
else:
    grade = "недійсне значення"  # Для випадків, коли число не в діапазоні
print(f"Оцінка: {grade}")