# find amx and Min in array

arr1 = [5, 6, 8, 12, 1, 5]
# 1st way
print(min(arr1))
print(max(arr1))

# 2nd way
maxi = arr1[0]
for i in range(1, len(arr1)):
    if arr1[i] > maxi:
        maxi = arr1[i]
print("maxi : ", maxi)

mini = arr1[0]
for i in range(1, len(arr1)):
    if arr1[i] < mini:
        mini = arr1[i]
print("mini : ", mini)

# find length of array
length = len(arr1)
count = 0
for ele in arr1:
    count += 1
print("Size : ", count)

#