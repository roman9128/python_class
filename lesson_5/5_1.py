# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fib (n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("Введите: "))
print(fib(n)) 