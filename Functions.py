#Functions
""""
other_list = [ ]
my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10]
for x in my_list:
    print(x)
other_list.append(x)
print(other_list) 
"""
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10]
other_list = [ x for x in my_list]
print(other_list)
"""
"""
other_list = [ ]
my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10]
for x in my_list:
    if x % 2 <= 0 :
        other_list.append(x)
print(other_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10]
other_list = [x for x in my_list if x%2 == 0]
"""
def add(a, b):
    return a + b
result = add(4, 6)
print(result)
result_2 = add(8, 10)
print(result_2)