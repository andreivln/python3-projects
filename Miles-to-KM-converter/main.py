from tkinter import *


def calculate():
    total = round(float(message.get()) * 1.609)  
    result.config(text=f"{total}"), 2  


window = Tk()

window.title("Miles to Kilometers converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


message = Entry(width=15)
message.grid(column=1, row=0)


mile = Label(text="Mile")
mile.grid(column=2, row=0)
mile.config(padx=10, pady=10)

text = Label(text="is equal to")
text.grid(column=0, row=1)
text.config(padx=10, pady=10)


Km = Label(text="Km")
Km.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)
# result.config(padx=10, pady=10)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
