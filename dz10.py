def divider(a, b):
    if a < b:
        raise ValueError("a < b")
    if b > 100:
        raise IndexError("b > 100")
    return a / b
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Помилка: {e} при обробці пари (key={key}, value={data[key]})")
print(result)

рзщ
