# Split Binary String
# Chintu has a long binary string ‘str’. A binary string is a string that contains only 0 and 1. He considers a string ‘beautiful’ if and only if the number of 0's and 1's in the string are equal.
# For example :
# 0011 , 1100 , 101010 etc are beautiful strings whereas 1110, 0001,10101 etc are not beautiful strings.
# Now Chintu wants to split the string into substrings such that each substring is beautiful. Can you help Chintu to find the maximum number of beautiful strings he can split the string into? If it is not possible to split the string in such a way that all strings are beautiful, return -1.
# For example :
# Let the given string be “101001” We will return 3 as we can divide the string into 3 beautiful strings “10” “10” and “01’.

def solution(binary_str):
    count_1, count_0, substring_count = 0, 0, 0
    for ele in binary_str:
        if int(ele) == 1:
            count_1 += 1
        else:
            count_0 += 1
        if count_1 == count_0:
            substring_count += 1
    if count_1 != count_0:
        return -1
    else:
        return substring_count


print(solution('1010'))
print(solution('100001'))


# find the length of the smallest subarray(subarray is a contiguous part of an array/list) in a given array/list ‘ARR’ of size ‘N’ with its sum greater than a given value. If there is no such subarray return 0.
# Example: Given an ‘ARR’: [1, 2, 21, 7, 6, 12] and a number ‘X’: 23. The length of the smallest subarray is 2 as the subarray is [21, 7].
# Note: Here are multiple subarrays whose sum is greater than ‘X’ such as [1, 2, 21] or [7, 6, 12] but we have to choose the minimum length subarray.

# naive
def minSubArrayLen(arr, target):
    currentSum = 0
    minLength = 1000000000
    for i in range(len(arr)):
        currentSum = 0
        for j in range(i, len(arr)):
            currentSum += arr[j]
            if currentSum > target:
                minLength = min(minLength, j - i + 1)

    return 0 if minLength == 1000000000 else minLength


print(minSubArrayLen([1, 2, 21, 7, 6, 12], 10))

# Python Program to Check if Two Strings are Anagram
# Python3 program for the above approach
from collections import Counter


def check(s1, s2):
    # implementing counter function
    if Counter(s1) == Counter(s2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)

# find amx and Min in array

# arr1 = [5, 6, 8, 12, 1, 5]
# # 1st way
# print(min(arr1))
# print(max(arr1))

# # 2nd way
# maxi = arr1[0]
# for i in range(1, len(arr1)):
#     if arr1[i] > maxi:
#         maxi = arr1[i]
# print("maxi : ", maxi)
#
# mini = arr1[0]
# for i in range(1, len(arr1)):
#     if arr1[i] < mini:
#         mini = arr1[i]
# print("mini : ", mini)
#
# # find length of array
# length = len(arr1)
# count = 0
# for ele in arr1:
#     count += 1
# print("Size : ", count)

# datetime
import datetime

current_date = datetime.datetime.today().date()
current_time = datetime.datetime.today().time()
current_datetime = datetime.datetime.today()
print(current_date)
print(current_time)
print(current_datetime)

filename = current_datetime.strftime('%Y_%m_%d_%H_%M_%S_%f')
print(filename)


# class variable vs object variable

class Roi:
    interest = .08

    def __init__(self, name, amount, interest):
        self.name = name
        self.amount = amount
        self.interest = interest

    def cal_interest(self):
        print('interest class level : ', self.amount * Roi.interest)  # this class level variable
        print('interest object level : ', self.amount * self.interest)  # this Object level variable


cust1 = Roi("Diapk", 100000, 0.05)
cust1.cal_interest()


# MRO(Method resolution order) - search is done in current class, then the search continue into parent classes in depth-first,
# left-right fashion without searching the same class twice

class moveCharacter:
    def move_fwd(self):
        print("Move 1 step forward in moveCharacter")

    def move_bwd(self):
        print("Move 1 step backward")


class jumpCharacter:
    def jump_up(self):
        print("Jump 1 step up")

    def jump_down(self):
        print("jump 1 step Down")

    def move_fwd(self):
        print("Move 1 step forward in jumpCharacter")


class pokemon(moveCharacter, jumpCharacter):
    def move_fwd(self):
        print("Move 1 step forward in pokemon")


poke = pokemon()
poke.move_fwd()
poke.jump_up()

print(pokemon.mro())
# O/p - [<class '__main__.pokemon'>, <class '__main__.moveCharacter'>, <class '__main__.jumpCharacter'>, <class 'object'>]


# Exception
try:
    print("Inside try block")
    y = int(input("Enter denominator : "))
    if y == 0:
        raise Exception("Y is zero (0)")
    print(5 / y)
except Exception as e:
    print(e)
    print("Inside except block")
else:
    print("Inside else block with except")

finally:
    print("inside finally block")


# Indexes of Subarray Sum Input: arr[] = {1,2,3,7,5}, n = 5, s = 12 Output: 2 4
# Explanation: The sum of elements from 2nd to 4th position is 12.
# Given an unsorted array arr of size n that contains only non negative integers,
# find a sub-array (continuous elements) that has sum equal to s. You mainly need to
# return the left and right indexes(1-based indexing) of that subarray.
# In case of multiple subarrays, return the subarray indexes which come first on moving
# from left to right. If no such subarray exists return an array consisting of element -1.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

def checkSubarraySum(arr1, expected_sum):
    start, end, sum1, n = 0, 0, 0, len(arr1)
    while end < n:
        sum1 += arr1[end]
        while sum1 > expected_sum and start < end:
            sum1 -= arr1[start]
            start += 1

        if sum1 == expected_sum:
            print("Sum found between indexes % d and % d" % (start, end))
            return 1
        end += 1
    print("No subarray found")
    return -1


arr1 = [1, 2, 3, 7, 5]
expected_sum = 12
checkSubarraySum(arr1, expected_sum)

# find length of string without using any builtins methods
str1 = "Dipak Singh"
str1_len = 0
for ele in str1:
    str1_len += 1
print("Length : " + str(str1_len))

# logging in Python
# DEBUG - Detailed information, typically of interest only when diagnosing problems.
# INFO - Confirmation that things are working as expected.
# WARNING - An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR - Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL - A serious error, indicating that the program itself may be unable to continue running.
import logging

# logging.warning("Warning Log")
# logging.basicConfig(level=logging.DEBUG, filename='..\Project\Logs\log_at_' + str(filename) + '.log', filemode="a")
# logging.basicConfig(format= '%(levelname)s:%(message)s',level=logging.DEBUG, filename='..\Project\Logs\logs.log', filemode="a")
logging.basicConfig(format='%(filename)s - %(asctime)s - %(message)s', level=logging.DEBUG,
                    filename='..\Project\Logs\logs.log', filemode="a")

logging.debug('Debug level - This message should go to the log file')
logging.info('Info : So should this')
logging.warning('Warning : And this, too')
logging.error('Error : And non-ASCII stuff, too, like Øresund and Malmö')
