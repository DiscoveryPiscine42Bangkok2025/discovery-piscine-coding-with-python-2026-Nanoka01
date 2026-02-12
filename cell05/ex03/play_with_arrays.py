array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for number in array:
    new_array.append(number + 2)

unique = []

for number in new_array:
    if new_array.count(number) == 1:
        unique.append(number)

print(array)
print(unique)
