# Дан список чисел. Определите, сколько в нем встречается различных чисел

s = []
slen = int(input("Введите размер списка: "))
for i in range(slen):
    item = input(f"Введите {i+1} число: ")
    s.append(item)
s = set(s)
s = list(s)
print(f"Уникальных элементов: {len(s)}")