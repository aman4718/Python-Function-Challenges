#Write a Python program to create a
# function that takes one argument,
# and that argument will be
#multiplied with an unknown given number.

def muliplied(n):
    return lambda x : x * n

res = muliplied(2)
print(res(15))

res1 = muliplied(4)
print(res1(15))