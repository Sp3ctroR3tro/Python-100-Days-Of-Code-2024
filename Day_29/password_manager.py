# Imports
from tkinter import *
import string
import random
from tkinter import simpledialog
from tkinter import messagebox
import pyperclip

# Function to generate a password of a specified length to the password entry field
def generate_password():
    password_length = simpledialog.askinteger("Password Length", " Min 8 characters. Enter the desired password length:", minvalue=8, maxvalue=32)
    if password_length:
        password = ""
        for i in range(password_length):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)

# Function to write password information to text document.
def add_password():
    # Confirm that fields are not empty
    if website_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="Invalid Entry", message="Please fill in all fields.")
        return

    # Save information to password document
    confirmation = messagebox.askyesno(title="Confirm", message=f"Are you sure you want to save the following information?\nWebsite: {website_entry.get()}\nEmail/Username: {email_entry.get()}\nPassword: {password_entry.get()}")
    if confirmation:
        with open("passwords.txt", "a") as password_file:
            website = website_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            password_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)




# Password Manager UI
window = Tk()
window.title("Password Manager")
logo_img = PhotoImage(file="logo.png")
# Add an empty padding column (left side of the layout)
window.grid_columnconfigure(0, weight=1)
canvas = Canvas(width=1024, height=500)
canvas.create_image(514, 250, image=logo_img)
# Center the canvas (logo image)
canvas.grid(row=0, column=1, columnspan=3)

# Change column for 'website_label' to align with center
website_label = Label(text="Website:")
website_label.grid(row=2, column=1, padx=10, pady=10, sticky="E")  # Align to the right (East)

# Place the 'website_entry' right next to the label
website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, padx=10, pady=10, sticky="W")  # Align to the left (West)
website_entry.focus()

# Change column for 'Email/Username' to align with center
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1, padx=10, pady=10, sticky="E")

# Place the 'Email/Username' right next to the label
email_entry = Entry(width=35)
email_entry.grid(row=3, column=2, padx=10, pady=10, sticky="W")
email_entry.insert(0, "dizzy@gmail.com")
# Change column for 'Email/Username' to align with center
password_label = Label(text="Password:")
password_label.grid(row=4, column=1, padx=10, pady=10, sticky="E")

# Place the 'Password' right next to the label
password_entry = Entry(width=21)
password_entry.grid(row=4, column=2, padx=10, pady=10, sticky="W")


generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=4, column=3, padx=10, pady=10, sticky="W")

# Placing the add button below all entry fields
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=5, column=1, columnspan=3, padx= 10, pady=10)

# Add another padding column (right side of the layout)
window.grid_columnconfigure(3, weight=1)

window.mainloop()