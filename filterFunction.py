## Write a Python program to filter a list of
# integers (even/odd) using Lambda

def filterInt(num) :
    print('Original Numbers : - ',num)
    even = list(filter(lambda x: x%2 == 0 , num))
    print('even no :-',even)
    odd = list(filter(lambda x : x%2 != 0 , num ))
    print('odd : -' , odd)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = filterInt(nums)
