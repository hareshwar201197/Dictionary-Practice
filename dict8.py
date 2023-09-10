
# Write a Python program to iterate over dictionaries using for loops.

sample = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
new_dic = {}
for key, value in sample.items():
    new_dic.update({
        key: value
    })

print(new_dic)