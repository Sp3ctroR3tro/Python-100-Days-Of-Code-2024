# Imports
from tkinter import *

# Defining Global Functions

def btn_click():
    mi_entry = float(Entry.get())
    km = float(mi_entry * 1.609344)
    km_value_label.config(text=f"{km:.2f}")




# Creating the GUI window
window = Tk()
window.title("MI to KM Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# Converter Text
Entry = Entry(width=10)
Entry.grid(row=0, column=3)
left_label = Label(text="is equal to")
left_label.grid(row=1, column=2)
km_value_label = Label(text="0")
km_value_label.grid(row=1, column=3)
ConvertButton = Button(text="Convert", command=lambda: btn_click())
ConvertButton.grid(row=2, column=3)
MILabel = Label( text="Miles")
MILabel.grid(row=0, column=5)
KMLabel = Label( text="Kilometers")
KMLabel.grid(row=1, column=5)










window.mainloop()