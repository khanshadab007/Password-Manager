from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img, anchor=CENTER)
canvas.grid(column=1, row=0, sticky='w')

label_1 = Label(text="Website:")
label_1.grid(column=0, row=1)

label_2 = Label(text="Email/Username:")
label_2.grid(column=0, row=2)

label_3 = Label(text="Password:")
label_3.grid(column=0, row=3, pady=5)

generate_button = Button(text="Generate Password")
generate_button.grid(column=1, row=3, sticky='e')

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, pady=10, columnspan=3, sticky="w")

website_entry = Entry(width=44)
website_entry.grid(column=1, row=1, pady=5)

email_entry = Entry(width=44)
email_entry.grid(column=1, row=2, pady=5)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky='w', pady=5)

window.mainloop()
