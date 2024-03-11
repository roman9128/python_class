# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n

string = input("Введите символы через пробел: ")
text = string.split()
count = {}
result = []

for i in text:
    if i in count:
        count[i] += 1
        result.append(f"{i}_{count[i]}")
    else:
        count[i] = 1
        result.append(i)
print(result)