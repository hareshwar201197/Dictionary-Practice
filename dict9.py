
# Write a Python program to sum all the items in a dictionary.

sample = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
sum_values = 0
for values in sample.values():
    sum_values += values
print(sum_values)
########################################################################
sum_values = sum(value for value in sample.values())
print(sum_values)

print(sum(sample.values()))