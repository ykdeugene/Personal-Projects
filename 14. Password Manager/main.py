import tkinter.messagebox
import random
import pyperclip
from chars import all_chars
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    gen_password = ""
    for _ in range(15):
        gen_password += random.choice(all_chars)
    password_entry.insert(0, string=gen_password)
    pyperclip.copy(gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()
    if website == "" or password == "" or email_user == "":
        tkinter.messagebox.showerror(title="Error", message="Please fill in all fields.")
        return
    else:
        with open("password_log.txt", mode="a") as password_log_file:
            password_log_file.write(f"{website} | {email_user} | {password} \n")
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    tkinter.messagebox.showinfo(title="Hello World", message="Password added 😊")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Label


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entry


website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_user_entry.insert(0, string="john_doe@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")


# Buttons


generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
