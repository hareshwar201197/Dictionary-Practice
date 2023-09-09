# 4. Write a Python script to check whether a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


is_key_present(5)
is_key_present(9)



# dic1 = {1:9, 2:8, 3:7,4:6}
#
# d2 = {5:10}
#
# for d in dic1.keys():
#     if d == 2:
#         print('key is already exist')
#
# print(dic1)