import operator

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

d1 = {"ram": 3, "sham": 2, "ganesh": 1}

print('Original dictionary : ',d1)
sorted_d = sorted(d1.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict(sorted(d1.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)