##POP
def pop_item(lst):
    lst[:] = [x for x in lst if x != lst[-1]]
    return lst


print(pop_item([2, 5, 6, 89]))