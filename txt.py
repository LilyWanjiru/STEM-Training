from tkinter import*

root = Tk()

#Create a task function
def myClick():
    my_Label = Label(root, text = "Hey, you clicked me!")
    my_Label.pack()

#Create a frame
myButton = Button(root, text="Click me!", command = myClick, fg ="white", bg="black")

#Pack it
myButton.pack()
root.mainloop()
