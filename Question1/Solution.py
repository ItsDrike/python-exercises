# Solution:
number_list = []

for x in range(100, 8001):
    if (x % 7 == 0) and (x % 5 == 0):
        number_list.append(str(x))
print(','.join(number_list))
