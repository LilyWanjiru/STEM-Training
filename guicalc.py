#Creating a simple calc
from tkinter import*

root = Tk()

#Creating text field space
e = Entry(root, width=50, bg="black", fg="white")
e.pack()
e.insert(0, "Enter First Number: ")

e2 = Entry(root, width=50, bg="black", fg="white")
e2.pack()
e2.insert(0, "Enter Second Number: ")

#Create a task function
def myClick():
   f_no = float(e.get())
   s_no = float(e2.get())

   sub = f_no - s_no
   add = f_no + s_no
   mult = f_no * s_no
   div = f_no / s_no


   Answer = "Add: " + str(add) + "\nSub: " +str(sub) + "\nMult: " + str(mult) +"\nDiv: " +str(div)
   myLabel = Label(root, text=Answer )
   myLabel.pack()

#Create a frame
myButton = Button(root, text="Calculator", command = myClick, fg= "white", bg="black")


#Pack it
myButton.pack()
root.mainloop()

