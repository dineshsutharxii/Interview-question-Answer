# lambda function
# - A lambda function is a small anonymous function.
# - A lambda function can take any number of arguments, but can only have one expression

sumi = lambda x: x * 2
print(sumi(2))
print((lambda x, y, z: x + y + z)(2, 3, 1))
full_name = lambda first, last: f"Full Name: {first} and Last Name: {last}"
print(full_name('Dipak', 'Singh'))

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11))

