from tkinter import *

root=Tk()
root.title("Dave's Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

#e.insert(0, "Name goes here")
def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math="addition"
    f_num = int(first_number)
    e.delete(0, END)
