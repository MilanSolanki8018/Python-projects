from tkinter import *

"""windows = Tk()
windows.title("GUI")
windows.minsize(width=500, height=300)

# lable
label = Label(text="I am a Label")
label.grid(row=0, column=0)
# chane value using argument
# label["text"] = "I am new Lable"

# button
def button_clicked():
    input_text = inputs.get()
    label["text"] = input_text
    # label["text"] = "I am new Lable"
    print("I Got Clicked")
button = Button(text="Click me", command=button_clicked )
# button.pack()
# button.place(x=0,y=0)
button.grid(row=0,column=2)

# entery
inputs = Entry(width=20)
inputs.grid(row=0,column=1)
windows.mainloop()"""


windows = Tk()
windows.title("GUI")
windows.minsize(width=500, height=300)
windows.config(padx=100, pady=200)
# lable
label = Label(text="I am a Label")
label.grid(row=0, column=0)

# button
def button_clicked():
    input_text = inputs.get()
    label["text"] = input_text

    print("I Got Clicked")
button = Button(text="Click me", command=button_clicked )

button.grid(row=1,column=2)

# button 2
def button_clicked():
    print("I am button 2 Clicked")


button1 = Button(text="Click me", command=button_clicked)

button1.grid(row=0, column=3)

# entery
inputs = Entry(width=20)
inputs.grid(row=3,column=4)

windows.mainloop()
