# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10^5.
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def FindDividers(number):
    return sum(n for n in range(1, number // 2 + 1) if number % n == 0)

k = int(input("Введите k: "))

for n in range(2, k + 1):
    if n == FindDividers(FindDividers(n)) and FindDividers(n) != n:
        if n < FindDividers(n):
            print(n, FindDividers(n))


# sum_dividers_less_k = {}

# for n in range(2, k + 1):
#     if n == FindDividers(FindDividers(n)) and FindDividers(n) != n:
#         sum_dividers_less_k[n] = FindDividers(n)

# for k, v in sum_dividers_less_k.items():
#     if k < v:
#         print(k, v)