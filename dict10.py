
# Write a Python program to multiply all the items in a dictionary.

sample = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
mult_values = 1
for value in sample.values():
    mult_values = mult_values * value
print(mult_values)

for key in sample:
    result=result * sample[key]