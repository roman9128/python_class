# Напишите программу для печати всех уникальных значений в словаре

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
s = []
i = 0
while i < len(dictionary):
    for k, v in dictionary[i].items():
        x = [k, v]
    s = s + x
    i += 1
values_list = []
j = 0
while j < len(s):
    values_list.append(s[j+1])
    j += 2
values_list = set(values_list)

# values_list = set()
# for item in dictionary:
#     for value in item.values():
#         values_list.add(value.strip())

values_list = list(values_list)
values_list.sort()
print(values_list)

