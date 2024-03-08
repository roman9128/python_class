import random

n = int(input("Введите число арбузов: "))
i = 0
lw = 12
hw = 0
print("У нас есть арбузы весом:")
while i < n:
    w = random.randint(4, 12)
    print(f"{w} кг")
    if w > hw:
        hw = w
    if w < lw:
        lw = w
    i += 1
print(f"Итак, самый тяжёлый арбуз весит {hw} кг, а самый лёгкий - {lw} кг")