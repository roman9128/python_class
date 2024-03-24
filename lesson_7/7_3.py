# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

# def same_by(characteristic, objects):
#     if len(objects) == 0:
#         return True
#     first = objects[0]
#     for i in objects:
#         if characteristic(i) != characteristic(first):
#             return False
#     return True

# def same_by(characteristic, objects):
#     result = list(filter(characteristic, objects))
#     return len(result) == len(objects) or not len(result)

def same_by(characteristic, objects):
    size = len(set(map(characteristic, objects)))
    return size < 2


values = [0, 2, 10, 61]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')