# Числа Фибоначчи. Какое по счёту число А в ряду этих чисел

a = int(input("Введите a: "))
i = 1
ii = 1
j = 3

while ii < a:
    j += 1
    i, ii = ii, ii + i

if a == 0:
    print(f"Ряд Фибоначчи начинается с 0 - это первое число в нём")
elif a == 1:
    print(f"Единица в ряду Фибоначчи находится под номерами 2 и 3")
elif a == ii:
    print(f"Число {a} в ряду Фибоначчи находится под номером {j}")
else:
    print(-1)