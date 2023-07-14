from tkinter import *
import random


root = Tk()
root.title("Password Generator")
root['bg'] = "light blue"
value = StringVar()
value2 = StringVar()

def func(event):
    get = value.get()
    get2 = value2.get()
    pas = ''
    for x in range(int(get)): 
        pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ@!&^%$#@)(*_+~`'))
    text_file = open(f"{get2}.txt", "w")
    text_file.write(get2 + ":" + pas)
    g["text"] = pas
l = Label(root,text="Enter the number of password characters below",bg="light blue")
e2 = Entry(root,textvariable=value2,bg="light blue")
e = Entry(root,textvariable=value,bg="light blue")
b = Button(root,text="Generate",bg="light blue")
g = Label(root,text="Here will be your password",bg="light blue")
t = Label(root,text="Enter name of program/game/social media,below",bg="light blue")


b.bind('<Button-1>', func)
l.pack()
e.pack()
b.pack()
g.pack()
t.pack()
e2.pack()

root.mainloop()
