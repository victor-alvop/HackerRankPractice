import random

n = int(input('Enter a number: '))
arr = [2, 3, 6, 6, 5]

max_value = max(arr)
value_count = arr.count(max_value) 
print(value_count)

if arr.count(max_value) > 1:
    for i in range(value_count):
        arr.remove(max_value)
    max_value = max(arr)
else:
    arr.remove(max_value)
    max_value = max(arr)

print(max_value)
