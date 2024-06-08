# combine lists and convert in string
list1 = ['hello', 'world']
list2 = ['in', 'python']
list1.extend(list2)
print(" ".join(list1))

# combine two list into dict
list1 = ['hello', 'world']
list2 = [1, 2]
dict1 = {}
# dict1 = {list1[i]:list2[i] for i in range(len(list1))}
# print(dict1)
# OR
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)


# number of times class/class instance is called
class home:
    count = 0
    def __init__(self):
        home.count += 1
a = home()
b = home()
print(home.count)

#find duplicate in list
list1 = ['india', 'is', 'good']
str1 = "".join(list1)
str = ""
for ele in str1:
    if str1.count(ele) > 1 and ele not in str:
        str += ele + " "
print(str)

#print all the word start with k
list1 = ['kiran', 'ketan', 'nitin', 'ramesh']
list2 = [word for word in list1 if word.startswith('k')]
print(list2)