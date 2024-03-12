arr = [5, 10, 5, 0, 5]
s = 0
for i in range(len(arr)):
    if s < arr[i-1] + arr[i] + arr[i - len(arr) + 1]:
        s = arr[i-1] + arr[i] + arr[i - len(arr) + 1]
print(s)
