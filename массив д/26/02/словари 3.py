my_dictionary = {'data1': 111, 'data2': 345, 'data3': 452, 'data4': 567}
result = 1
for key in my_dictionary:
    result = result * my_dictionary[key]
print(result)