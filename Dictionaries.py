# Dictionaries in python
mydict = {
    "Book" : "Dynamics",
    "Publisher" : "Longhorn",
    "Year" : 2001 ,
    "Authors" : ["Luanne", "Rice", "Lawrence"]

}
# Accessing item
x = mydict["Year"]
print(x)

# Accessing using get()
y = mydict.get("Year")
print(y)

#All keys
a = mydict.keys()
print(a)

#All values
b = mydict.values()
print(b)

#Printing all items
c = mydict.items()
print(c)

#Checking if key exixts
if "Publisher" in mydict :
    print("Publisher is one of the keys")
if "Authors" in mydict :
    print("They are all awesome")

print(len(mydict))# Dict can't have same keyword repeated  

#Dictionaries can hold diff data types
#list is seen in authors