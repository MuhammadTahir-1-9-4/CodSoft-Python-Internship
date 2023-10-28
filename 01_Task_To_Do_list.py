from tkinter import *


class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do-list-app")
        self.root.geometry("650x450+300+150")
        self.root.configure(bg="beige")

        self.label1 = Label(
            self.root,
            text="To-Do List",
            font=("Comic Sans MS", 20, "bold"),
            width=10,
            bd=5,
            bg="purple",
            fg="white",
        )
        self.label1.pack(side="top", fill=BOTH)

        self.label2 = Label(
            self.root,
            text="Enter the task:",
            font="ariel 16 bold",
            width=10,
            bd=5,
            bg="beige",
            fg="black",
        )
        self.label2.place(x=20, y=85)

        self.label3 = Label(
            self.root,
            text="Tasks",
            font="calibri 20 bold underline",
            width=10,
            bd=10,
            bg="beige",
            fg="black",
        )
        self.label3.place(x=350, y=70)

        self.text = Text(self.root, heigh=2, bd=5, width=23, font="ariel 12 bold")
        self.text.place(x=20, y=120)

        self.main_text = Listbox(
            self.root,
            height=10,
            bd=5,
            width=27,
            font="ariel 18 bold italic",
        )
        self.main_text.place(x=260, y=120)

        # create an empty file if file does not exist
        try:
            with open("todo.txt", "r") as f:
                readLine = f.readlines()
                for i in readLine:
                    self.main_text.insert(END, i)
        except FileNotFoundError:
            with open("todo.txt", "w") as f:
                pass

        # Add task method
        def addTask():
            item = ""
            item = self.text.get(1.0, END)
            if item.strip():
                self.main_text.insert(END, item)
                with open("todo.txt", "a") as f:
                    f.write(item)
                self.text.delete(1.0, END)

        # delete task method
        def deleteTask():
            item_to_delete = self.main_text.curselection()
            selected_item = self.main_text.get(item_to_delete)
            with open("todo.txt", "r") as f:
                list_of_tasks = f.readlines()
            with open("todo.txt", "w") as f:
                for item in list_of_tasks:
                    if item.strip() != selected_item[0].strip():
                        f.write(item)
            self.main_text.delete(item_to_delete)

        # delete all tasks method
        def deleteAllTasks():
            self.main_text.delete(0, END)
            open("todo.txt", "w").close()  # clearing the file

        # function to exit application
        def exitApp():
            root.destroy()

        # buttons
        self.button1 = Button(
            self.root,
            text="Add Task",
            font="ariel 12 bold",
            width=14,
            bd=3,
            bg="yellow",
            fg="black",
            command=addTask,
        )
        self.button1.place(x=50, y=210)

        self.button2 = Button(
            self.root,
            text="Delete Task",
            font="arial 12 bold",
            width=14,
            bd=3,
            bg="yellow",
            fg="black",
            command=deleteTask,
        )
        self.button2.place(x=50, y=267)

        self.button3 = Button(
            self.root,
            text="Delete All Tasks",
            font="arial 12 bold",
            width=14,
            bd=3,
            bg="yellow",
            fg="black",
            command=deleteAllTasks,
        )
        self.button3.place(x=50, y=324)

        self.button4 = Button(
            self.root,
            text="Exit",
            font="arial 12 bold",
            width=14,
            bd=3,
            bg="red",
            fg="black",
            command=exitApp,
        )
        self.button4.place(x=50, y=381)


if __name__ == "__main__":
    root = Tk()
    obj = ToDoList(root)
    root.mainloop()
