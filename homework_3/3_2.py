# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
list_1 = [1, 2, 3, 4, 5]
k = int(input("Введите k: "))

num = 0
if k in list_1:
    num = k
else:
    list_1.append(k)
    list_1.sort()
    if list_1.index(k) == 0:
        num = list_1[list_1.index(k)+1]
    elif list_1.index(k) == len(list_1) - 1:
        num = list_1[len(list_1) - 2]
    elif abs(abs(list_1[list_1.index(k)-1]) - abs(k)) < abs(abs(k) - abs(list_1[list_1.index(k)+1])):
        num = list_1[list_1.index(k)-1]
    elif abs(abs(list_1[list_1.index(k)-1]) - abs(k)) > abs(abs(k) - abs(list_1[list_1.index(k)+1])):
        num = list_1[list_1.index(k)+1]
print(num)