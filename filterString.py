def filterString(l):
    str = [];
    for i in l:
        if type(i) != int :
            str.append(i)

    return str

l = [25,'Raj',4714,'Mukul',8699,'Prince',55,'tony']
string_filter = filterString(l)
print(string_filter)