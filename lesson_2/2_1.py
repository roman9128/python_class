# Факториал

n = int(input("Введите n: "))
result = 1
while n != 0:
    result = result * n
    n -= 1
print(f"Факториал n равен {result}")