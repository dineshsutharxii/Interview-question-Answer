# Difference between 1.extend, 2.append and 3.insert in List
from Project.testcases.test_flight_booking import TestSearchFlightAndVerifyResults

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

from Project.utilities.Utility import Utility
import logging

utility = Utility()
log = utility.custom_logger()
log.warning("From warning log")

execution_list = Utility().read_excel(
    r'C:\Users\dines\Learn And Interview\Interview_question_answer\Project\SuiteFiles\ExecutionList.xlsx',
    'ExecutionList')
modules_to_be_execute = []
for modules in execution_list:
    if modules[0] == 'Y':
        modules_to_be_execute.append(modules)
if len(modules_to_be_execute) < 1:
    log.info("No Module is selected in ExecutionList to execute")
else:
    for module in modules_to_be_execute:
        testcases_to_be_execute = []
        testcase_list = utility.read_excel(
            r'C:\Users\dines\Learn And Interview\Interview_question_answer\Project\SuiteFiles\S' + str(
                module[1]) + '.xlsx', str(module[1]))
        testcase_data_list = utility.read_excel(
            r'C:\Users\dines\Learn And Interview\Interview_question_answer\Project\SuiteFiles\S' + str(
                module[1]) + '.xlsx', "TestData")
        for i in range(len(testcase_list)):
            if testcase_list[i][1] == 'Y':
                matching_sublist = next(
                    (sublist for sublist in testcase_data_list if sublist[0] == testcase_list[i][2]), None)
                print(matching_sublist)
                if matching_sublist: testcase_list[i].extend(matching_sublist[1:])
                testcases_to_be_execute.append(testcase_list[i])
        if module[1] == 'Flights':
            flight = TestSearchFlightAndVerifyResults()
            for i in range(len(testcases_to_be_execute)):
                print(str(testcases_to_be_execute[i][4]).strip())
                if hasattr(flight, (testcases_to_be_execute[i][4]).strip()):
                    method_to_call = getattr(flight, (testcases_to_be_execute[i][4]).strip(), None)
                params = [testcases_to_be_execute[i][5], testcases_to_be_execute[i][6]]
                method_to_call(*params)
                testcase = str(testcases_to_be_execute[i][4])+"("+testcases_to_be_execute[i][5]+ ","+testcases_to_be_execute[i][6]+")"
                flight.testcase
        print(testcases_to_be_execute)
        # print(testcase_data_list)

# print(execution_list)
print("modules_to_be_execute", modules_to_be_execute)
