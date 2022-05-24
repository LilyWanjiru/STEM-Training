# Lists
fruits = ["apple", "orange", "banana"]
fruits_2 = ["cherry", "tomato"]
fruits_3 = fruits + fruits_2
print(fruits_3)
fruits.extend(fruits_2)
print(fruits)
fruits_2.clear()
print(fruits_2)
fruits.append("avocado")
print(fruits)
fruits.remove("cherry")
print(fruits)
my_fruits = fruits.pop(1)
print(fruits)
print(my_fruits)

#Tuples

fruits_4 = ("apple", "oranges", "something")
print(fruits_4)
print(fruits_4[1])
new_list = list(fruits_4)#always print out command
print(new_list)
new_list.append("tomato")
print(new_list)
fruits_4 = tuple(new_list)
print(fruits_4)

#Sets
fruits_4 = ("apples", "oranges", "oranges", "oranges")#variables redeclared
fruits_5 = {"apples", "oranges", "oranges", "oranges"}
print(fruits_5)

#Dictionaries
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in my_list:
    print(x)
