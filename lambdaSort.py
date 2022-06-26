###Write a Python program to sort a list
# of tuples using Lambda.
#Original list of tuples

## list of tuples
l1 =  [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##sorting
l1.sort(key = lambda x:x[1])
## output
print(l1)
