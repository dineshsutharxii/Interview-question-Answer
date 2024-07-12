# Difference between 1.extend, 2.append and 3.insert in List
list_test = [1, 4, 5]
list2 = [2, 4, 6]

# output
# append(5) - add element to the last in list - [1, 4, 5, 5]
# insert(2, 7) - it will add element at specific location - [1,4,7,5,5]
# extend(list2) - it will combine the list2 with list_test - [1,4,7,5,5,2,4,6]
list_test.append(5)
list_test.insert(2, 7)
list_test.extend(list2)
print(list_test)


# Make dict of string key and int value and extract keys and values in two different lists
dict_test = {'one': 1, "two": "2", "three": 3, "four": "4"}
key = dict_test.keys()
values = dict_test.values()

# take values list and reverse it using inbuilt methods and without inbuilt methods
new_list = []
for value in values:
    new_list.append(int(value))
# for key,value in dict_test.items():
#     print(key, value)

# using in-built method
print(sorted(new_list))
print(new_list[::-1])

# without using inbuilt method
len1 = len(new_list)
for i in range(len1):
    for j in range(i + 1, len1):
        if new_list[i] < new_list[j]:
            new_list[i], new_list[j] = new_list[j], new_list[i]

print(new_list)
list1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]
print([num for sublist in list1 for num in sublist])

from Project.utilities.logging_utility import Utility
import logging

log = Utility().custom_logger()
log.warning("From warning log")

excel = Utility().read_excel(r'C:\Users\dines\Learn And Interview\Interview_question_answer\Day_two\data.xlsx', 'Sheet1')
print(excel)