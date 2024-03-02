# Посчитать сумму всех цифр числа

n = float(input("Введите число: "))
sum = 0
if n - int(n) > 0:
    while n - int(n) != 0:
        n = n * 10
while n > 0:
    sum+=n%10
    n=n//10
sum = int(sum)
print(sum)