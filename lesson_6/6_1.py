# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
import random

n = int(input("Введите размер 1 массива: "))
array_N = [random.randint(1, 10) for i in range(n)]

m = int(input("Введите размер 2 массива: "))
array_M = [random.randint(1, 10) for i in range(m)]
set_array_M = set(array_M)

result = [x for x in array_N if x not in set_array_M]

print(f"1 массив {array_N}")
print(f"2 массив {array_M}")
print(result)