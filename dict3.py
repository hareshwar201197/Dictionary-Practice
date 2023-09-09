# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d4 = {}

for d in (dic1, dic2, dic3):
    d4.update(d)
print(d4)
# d4.update(dic1)
# d4.update(dic2)
# d4.update(dic3)
#
# print(d4)