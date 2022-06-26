def primeNumber(n1, n2):
    l1 = []
    for num in range(n1, n2 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                l1.append(num)
    return l1


a = primeNumber(1, 1000)
print(a)
