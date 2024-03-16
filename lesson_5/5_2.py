# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные

import random

def replace(list_n, max_n, i = 0):
    if i == len(list_n):
        return
    if list_n[i] == max_n:
        list_n[i] = min(list_n)
    replace(list_n, max_n, i + 1)

v = int(input("Введите количество оценок: "))
j = [random.randint(1, 5) for i in range(v)]
max_n = max(j)
print(j)
replace(j, max_n)
print(j)