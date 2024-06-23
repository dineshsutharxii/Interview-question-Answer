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
