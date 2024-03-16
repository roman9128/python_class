# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def issimple (n, i = 2):
    if n < 2:
        print("Not simple")
        return
    if n == 2:
        print("Simple")
        return
    if i < n**0.5 + 1:
        if n % i == 0:
            print("Not simple")
            return
        else:
            issimple(n, i+1)
    else:
        print("Simple")
        return
    

n = int(input("Введите: "))
issimple(n)

