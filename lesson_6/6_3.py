# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

import random
from collections import Counter

n = int(input("Введите размер массива: "))
arr = [random.randint(1, 10) for i in range(n)]
counter = dict(Counter(arr))
result = 0

for item in counter:
    if counter[item] > 1:
        result += counter[item] // 2

print(f"Массив: {arr}")
print(f"Количество пар одинаковых элементов: {result}")