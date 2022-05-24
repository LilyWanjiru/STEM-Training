x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()    

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

def myfunc():
    global x
    x = "vie"

myfunc()

print("C'est la " + x) 