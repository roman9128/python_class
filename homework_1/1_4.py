# Определите, можно ли от шоколадки размером a × b долек отломить c долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.

print("Укажите размер шоколадки")
a = int(input("Введите количество долек с 1 стороны: "))
b = int(input("Введите количество долек со 2 стороны: "))
c = int(input("Сколько долек Вы ходите отломить за 1 раз: "))
if c % a == 0 or c % b == 0:
    print("yes")
else:
    print("no")