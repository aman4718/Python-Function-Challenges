###Write a Python program to sort a list
# of dictionaries using Lambda

models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)

### soting with making
sorted_model = sorted(models,key = lambda x : x['make']);
print('sorting on the basis of making : -')
print(sorted_model)

### sorting with color
color_sorted = sorted(models , key =lambda c : c['color'])
print('sorting on the basis of color : -')
print(color_sorted)