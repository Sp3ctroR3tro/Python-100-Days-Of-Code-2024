
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
root.title("Simple Calculator")

# Declaring the string variable for line input
input_text = StringVar()

# Configuring root to automatically resize to fit its contents
root.rowconfigure(0, weight=1)
for i in range(1, 6):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

# Creating the entry window and calculator buttons using grid
entry1 = tkinter.Entry(root, textvariable=input_text, font=("Arial", 20, "bold"))
entry1.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('0', 4, 1), ('.', 4, 0), ('=', 4, 2), ('/', 4, 3),
    ('C', 5, 0), ('(', 5, 1), (')', 5, 2)
]

for (text, row, col) in buttons:
    button = Button(root, text=text, fg='white', bg='black',
                    command=lambda t=text: btn_click(t) if t != '=' else btn_equal(), width=10, height=3)
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Clear button defined separately to call btn_clear
button_clear = Button(root, text="C", fg='white', bg='black', command=lambda: btn_clear(), width=10, height=3)
button_clear.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

# Adding the open and close parenthesis buttons separately to their respective commands
button_open_parenthesis = Button(root, text="(", fg='white', bg='black', command=lambda: btn_click("("), width=10,
                                 height=3)
button_open_parenthesis.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)

button_close_parenthesis = Button(root, text=")", fg='white', bg='black', command=lambda: btn_click(")"), width=10,
                                  height=3)
button_close_parenthesis.grid(row=5, column=2, sticky="nsew", padx=5, pady=5)

# Run the main event loop
root.mainloop()
