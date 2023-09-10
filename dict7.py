
# Write a Python script to merge two Python dictionaries.

dic1 = {'1': 'abhi', '2': 'raks', '3': 'pra'}
dic2 = {'4': 'name', '5': 'dany'}

dict3 = dic1.copy()
dict3.update(dic2)

print(dict3)