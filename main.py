from tkinter import *


def calculate():
    miles = float(user_input.get())
    km = miles * 1.6
    calculation.config(text=f"{km:.2f}")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

user_input = Entry()
user_input.config(width=10)
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

calculation = Label(text=0)
calculation.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=2)

window.mainloop()
