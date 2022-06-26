def filerCustom(num):
    postiveNumber = [];

    for i in num :
        if i > 0 :
            postiveNumber.append(i)
    return postiveNumber;
nums = [-2, -1, 0, 1, 2]
filt = filerCustom(nums)
print(filt)