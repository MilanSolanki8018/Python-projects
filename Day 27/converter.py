from tkinter import *

windows =Tk()
windows.title("Mile to km Converter")
windows.minsize(width=300, height=200)
windows.config(padx=50, pady=50)

# Entry
entry = Entry(width=20)
entry.grid(column=1, row=0)
# lable
label1 = Label(text="Miles")
label1.grid(column=2, row=0)
# lable
label2 = Label(text="is equal to")
label2.grid(column=0,row=1)
# lable
label3 = Label(text="0")
label3.grid(column=1, row=1)
# lable
label4 = Label(text="km")
label4.grid(column=2, row=1)

# button
def convert():
    miles = entry.get()
    km = float(miles) * 1.609
    label3["text"] = km
    print("hii")
button= Button(text="Calculator", command=convert)
button.grid(column=1, row=2)
windows.mainloop()