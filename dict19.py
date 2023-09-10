#  Write a Python program to create and display all combinations of letters,
#  selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
data = {'1':['a','b'], '2':['c','d']}
result_lst = []

for value1 in data['1']:
    for value2 in data['2']:
        combination = value1 + value2
        result_lst.append(combination)
print(result_lst)

for comb in result_lst:
    print(comb)
