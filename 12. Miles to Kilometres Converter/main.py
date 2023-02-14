from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)


def button_clicked():
    answer.config(text=f"{float(to_convert.get())*1.609344}")


# Label
is_equal_to = Label(text=f"is equal to", font=("Arial", 10, "normal"))
is_equal_to.grid(column=0, row=1)

answer = Label(text=f"0", font=("Arial", 10, "normal"))
answer.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 10, "normal"))
km.grid(column=2, row=1)

miles = Label(text="Miles", font=("Arial", 10, "normal"))
miles.grid(column=2, row=0)

# Button
convert = Button(text="Calculate", command=button_clicked)
convert.grid(column=1, row=2)

# Input
to_convert = Entry()
to_convert.grid(column=1, row=0)

window.mainloop()
