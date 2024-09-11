# Python program to create a simple GUI

# import everything from tkinter module
import tkinter
from tkinter import *


# Global variables for the program
expression = ""

def btn_click(item):
	global expression
	expression += str(item)
	input_text.set(expression)

def btn_clear():
	global expression
	expression = ""
	input_text.set("")

def btn_equal():
	global expression
	try:
		result = str(eval(expression))
	except ZeroDivisionError:
		result = "Error"
	except Exception as e:
		result = "Error"
	input_text.set(result)
	expression = ""




#  Creating the calculator window
root = Tk()
root.geometry("400x300")
root.title("Simple Calculator")
# Declaring the string variable for line input
input_text = StringVar()

# Creating the entry window and calculator buttons
entry1 = tkinter.Entry(root, textvariable=input_text, font=("Arial", 20, "bold"))
entry1.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

button1 = Button(root, text='1', fg='white', bg='black', command=lambda: btn_click(1), width=10, height=3)
button1.grid(row=1, column=0)

button2 = Button(root, text='2', fg='white', bg='black', command=lambda: btn_click(2), width=10, height=3)
button2.grid(row=1, column=1)

button3 = Button(root, text='3', fg='white', bg='black', command=lambda: btn_click(3), width=10, height=3)
button3.grid(row=1, column=2)

button_add = Button(root, text="+", fg='white', bg='black', command=lambda: btn_click("+"), width=10, height=3)
button_add.grid(row=1, column=3)

button4 = Button(root, text='4', fg='white', bg='black', command=lambda: btn_click(4), width=10, height=3)
button4.grid(row=2, column=0)

button5 = Button(root, text='5', fg='white', bg='black', command=lambda: btn_click(5), width=10, height=3)
button5.grid(row=2, column=1)

button6 = Button(root, text='6', fg='white', bg='black', command=lambda: btn_click(6), width=10, height=3)
button6.grid(row=2, column=2)

button_sub = Button(root, text="-", fg='white', bg='black', command=lambda: btn_click("-"), width=10, height=3)
button_sub.grid(row=2, column=3)

button7 = Button(root, text='7', fg='white', bg='black', command=lambda: btn_click(7), width=10, height=3)
button7.grid(row=3, column=0)

button8 = Button(root, text='8', fg='white', bg='black', command=lambda: btn_click(8), width=10, height=3)
button8.grid(row=3, column=1)

button9 = Button(root, text='9', fg='white', bg='black', command=lambda: btn_click(9), width=10, height=3)
button9.grid(row=3, column=2)

button_mul = Button(root, text="*", fg='white', bg='black', command=lambda: btn_click("*"), width=10, height=3)
button_mul.grid(row=3, column=3)

button0 = Button(root, text='0', fg='white', bg='black', command=lambda: btn_click(0), width=10, height=3)
button0.grid(row=4, column=1)

button_dec = Button(root, text=".", fg='white', bg='black', command=lambda: btn_click("."), width=10, height=3)
button_dec.grid(row=4, column=0)

button_equal = Button(root, text="=", fg='white', bg='black', command=lambda: btn_equal(), width=10, height=3)
button_equal.grid(row=4, column=2)

button_div = Button(root, text="/", fg='white', bg='black', command=lambda: btn_click("/"), width=10, height=3)
button_div.grid(row=4, column=3)

button_clear = Button(root, text="C", fg='white', bg='black', command=lambda: btn_clear(), width=10, height=3)
button_clear.grid(row=5, column=0)

button_open_parenthesis = Button(root, text="(", fg='white', bg='black', command=lambda: btn_click("("), width=10, height=3)
button_open_parenthesis.grid(row=5, column=1)

button_close_parenthesis = Button(root, text=")", fg='white', bg='black', command=lambda: btn_click(")"), width=10, height=3)
button_close_parenthesis.grid(row=5, column=2)

# Run the main event loop
root.mainloop()
