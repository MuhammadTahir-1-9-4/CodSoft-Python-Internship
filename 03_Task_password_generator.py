from tkinter import *
import random

root = Tk()
root.title("Password Generator")
root.geometry("500x410+300+150")
root.resizable(False, False)
root.config(bg="orange")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "1234567890"
symbols = """`~!@#$%^&*()_-+={[]}\\?/.,;:"'><"""
string = lower + upper + digits + symbols


def generatePassword():
    num_text = length_text.get("1.0", "end-1c")  # Get text from the Text widget
    total_len = len(string)
    num = int(num_text)
    if num <= 0:
        password_display.delete(1.0, END)
        password_display.insert(INSERT, "Invalid length")
    elif num > total_len:
        password_display.delete(1.0, END)
        password_display.insert(INSERT, "Invalid length")
    else:
        password = "".join(random.sample(string, num))
        password_display.delete(1.0, END)
        password_display.insert(INSERT, password)


Label(
    root, text="Password Generator", font=("Comic Sans MS", 20, "bold"), bg="orange"
).pack()

Label(root, text="Enter the length", font="sarif 14 bold", bg="orange").place(
    x=170, y=100
)

# Use a Text widget for entering the length
length_text = Text(
    root,
    font="calibri 14 bold",
    height=1,
    width=10,
    bd=2,
)
length_text.place(x=190, y=140)

Button(
    root,
    text="Generate Password",
    font="sarif 14 bold",
    bg="#2a2d36",
    fg="white",
    command=generatePassword,
).place(x=150, y=190)

# Use a Text widget for displaying the generated password
password_display = Text(
    root, font="calibri 12 bold", height=2, width=30, bd=3
)  # Adjust height and width as needed
password_display.place(x=130, y=240)


Button(
    root,
    text="exit",
    font="sarif 16 bold",
    bg="red",
    fg="black",
    height=1,
    width=6,
    command=root.destroy,
).pack(side="bottom")

root.mainloop()
