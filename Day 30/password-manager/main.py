from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- SEARCH DATA------------------------------- #
def search_data():
    one = web_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showerror(title="error", message="No data File Found.")
    else:
        if one in data:
            messagebox.showinfo(title=one, message=f"Email: {data[one]["email"]}  \n Password: {data[one]["password"]} ")
        else:
            messagebox.showerror(title="error" , message=f"Data not found in file")

# ----------------------------  PASSWORD GENERATOR  ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    l=random.randint(8, 10)
    n=random.randint(2, 5)
    s=random.randint(2, 4)
    password_list = []

    password_list += [random.choice(letters) for _ in range(l)]
    password_list += [random.choice(numbers) for _ in range(n)]
    password_list += [random.choice(symbols) for _ in range(s)]


    #Random value from list
    random.shuffle(password_list)

    # list into string using join all value joined
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    one = web_input.get()
    two = email_input.get()
    three = password_input.get()

    new_data = {one:
        {
        "email":two,
        "password":three
      }
    }

    if len(one)==0 or len(three)==0:
         messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=one, message=f"These are the details entered: \n Email: {two} \n Password: {three} \n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    data = json.load(data_file)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file, indent=4)
            else:
                #update old data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data,data_file, indent=4)
            finally:
                web_input.delete(0, END)
                    # email_input.delete(0,END)
                password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=190)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100,95, image=password_image )
canvas.grid(row=0,column=1)

# lable
web_name = Label(text="Website:")
web_name.grid(row=1,column=0)

email = Label(text="Email/Username:")
email.grid(row=2,column=0)

password = Label(text="Password:")
password.grid(row=3,column=0)

# Entry
web_input = Entry(width=27)
web_input.grid(row=1,column=1)
web_input.focus()

email_input = Entry(width=45)
email_input.grid(row=2,column=1, columnspan=2)
email_input.insert(0, "my@gmail.com")

password_input = Entry(width=27)
password_input.grid(row=3,column=1)

# button
save_add = Button(text="Add",width=38, command=save)
save_add.grid(row=4,column=1, columnspan=2)

password_generate = Button(text="Generate password", command=generate_password)
password_generate.grid(row=3,column=2)

search = Button(text="Search", command=search_data,width=14)
search.grid(row=1,column=2)

window.mainloop()