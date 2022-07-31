from tkinter import *


def km_to_miles():
    km = float(km_input.get())
    miles = round(km / 1.609, 2)
    miles_value.config(text=f"{miles}")


window = Tk()
window.title("Km to Miles Converter")
window.config(padx=30, pady=5)
window.minsize(width=250, height=50)

km_input = Entry(width=10)
km_input.grid(column=1, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=0)

value_label = Label(text="Is Equal To")
value_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

miles_value = Label(text="0")
miles_value.grid(column=1, row=1)

btn = Button(text="Calculate", command=km_to_miles)
btn.grid(column=1, row=2)

Copyright = Label(text=u"\u00A9" + 'Aksh Tejwani')
Copyright.grid(column=1, row=6)

window.mainloop()
