from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = ([choice(letters) for _ in range(randint(8, 10))]
                     + [choice(numbers) for _ in range(randint(2, 4))]
                     + [choice(symbols) for _ in range(randint(2, 4))])
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

# Message box title won't show on Mac

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please make sure no fields are empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}\n"
                                                              f"Email: {email_username}\nPassword: {password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as password_data_file:
                password_data_file.write(f"{website} | {email_username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_username_entry.delete(0, END)
            email_username_entry.insert(0, "abc@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightbackground="white")
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:", bg="white", fg="black")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35, bg="white", highlightbackground="white", fg="black")
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35, bg="white", highlightbackground="white", fg="black")
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(END, "abc@gmail.com")
password_entry = Entry(width=20, bg="white", highlightbackground="white", fg="black")
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate, width=11, bg="white", fg="black", highlightbackground="white")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", command=save, width=33, bg="white", fg="black", highlightbackground="white")
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()

