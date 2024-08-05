from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*']

    nr_letters = random.randint(4, 5)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }
    # # Debugging prints
    # print(f"Website: '{website}'")
    # print(f"Email: '{email}'")
    # print(f"Password: '{password}'")
    # print(len(website))
    # print(len(password))

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Invalid details", message="Please enter valid details. ")
    else:
        is_ok = messagebox.askokcancel(title="Save password", message=f"Email: {email} \n" f"Password: {password} "
                                                                      f"\nDo you confirm to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            messagebox.showinfo(title="Congratulations", message=" Data has been saved successfully.")


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

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=1, row=3, sticky='e')

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, pady=10, columnspan=3, sticky="w")

website_entry = Entry(width=44)
website_entry.grid(column=1, row=1, pady=5)
website_entry.focus()

email_entry = Entry(width=44)
email_entry.grid(column=1, row=2, pady=5)
email_entry.insert(0, 'khanshadabqasim@gmail.com')

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky='w', pady=5)

window.mainloop()
