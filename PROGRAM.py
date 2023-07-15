from tkinter import *
import random

Theme = "light Blue"

root = Tk()
root.title("Password Generator")
root['bg'] = Theme
root.geometry('800x600')

symbol_count = StringVar()
name = StringVar()
Type_pasword = StringVar()

def func():
    Type_pasword_get = Type_pasword.get()
    if Type_pasword_get == 'all' or ['']:
        symbol_count_get, name_get = symbol_count.get(), name.get()
        pas = str('')
        try:
            for x in range(int(symbol_count_get)):
                pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ@!&^%$#@)(*_+~`'))
    
            with open(f"{name_get}.txt", "w") as text_file: 
                text_file.write(f"{name_get} password: {pas}")

            password_here["text"] = pas
        except Exception:
            password_here["text"] = "Failed to generate password"
    if Type_pasword_get == 'num':
        symbol_count_get, name_get = symbol_count.get(), name.get()
        pas = str('')
        try:
            for x in range(int(symbol_count_get)):
                pas = pas + random.choice(list('1234567890'))
    
            with open(f"{name_get}.txt", "w") as text_file: 
                text_file.write(f"{name_get} password: {pas}")

            password_here["text"] = pas
        except Exception:
            password_here["text"] = "Failed to generate password"
    if Type_pasword_get == 'sym':
        symbol_count_get, name_get = symbol_count.get(), name.get()
        pas = str('')
        try:
            for x in range(int(symbol_count_get)):
                pas = pas + random.choice(list('()-=+:;"{./,}<>!@#$%^&*[]'))
    
            with open(f"{name_get}.txt", "w") as text_file: 
                text_file.write(f"{name_get} password: {pas}")

            password_here["text"] = pas
        except Exception:
            password_here["text"] = "Failed to generate password"
    if Type_pasword_get == 's_l':
        symbol_count_get, name_get = symbol_count.get(), name.get()
        pas = str('')
        try:
            for x in range(int(symbol_count_get)):
                pas = pas + random.choice(list('abcdefghigklmnopqrstuvyxwz'))
    
            with open(f"{name_get}.txt", "w") as text_file: 
                text_file.write(f"{name_get} password: {pas}")

            password_here["text"] = pas
        except Exception:
            password_here["text"] = "Failed to generate password"

    if Type_pasword_get == 'b_l':
        symbol_count_get, name_get = symbol_count.get(), name.get()
        pas = str('')
        try:
            for x in range(int(symbol_count_get)):
                pas = pas + random.choice(list('ABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    
            with open(f"{name_get}.txt", "w") as text_file: 
                text_file.write(f"{name_get} password: {pas}")

            password_here["text"] = pas
        except Exception:
            password_here["text"] = "Failed to generate password"
    if Type_pasword_get ==  'b_l_s_l':
            symbol_count_get, name_get = symbol_count.get(), name.get()
            pas = str('')
            try:
                for x in range(int(symbol_count_get)):
                    pas = pas + random.choice(list('ABCDEFGHIGKLMNOPQRSTUVYXWZabcdefghigklmnopqrstuvyxwz'))
        
                with open(f"{name_get}.txt", "w") as text_file: 
                    text_file.write(f"{name_get} password: {pas}")

                password_here["text"] = pas
            except Exception:
                password_here["text"] = "Failed to generate password"
    if Type_pasword_get ==  'b_l_s_l_n':
            symbol_count_get, name_get = symbol_count.get(), name.get()
            pas = str('')
            try:
                for x in range(int(symbol_count_get)):
                    pas = pas + random.choice(list('ABCDEFGHIGKLMNOPQRSTUVYXWZabcdefghigklmnopqrstuvyxwz1234567890'))
        
                with open(f"{name_get}.txt", "w") as text_file: 
                    text_file.write(f"{name_get} password: {pas}")

                password_here["text"] = pas
            except Exception:
                password_here["text"] = "Failed to generate password"
def theme():
    global Theme
    if Theme == "light Blue":
       Theme = "light green"
       root['bg'],text["bg"],input_name["bg"],text_2["bg"],input_symbol_count["bg"],password_here["bg"],Generate_pswd_button["bg"],resize_btn["bg"],Type_pasword_input["bg"],text_3["bg"] = Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme
    elif Theme == "light green":
       Theme = "violet"
       root['bg'],text["bg"],input_name["bg"],text_2["bg"],input_symbol_count["bg"],password_here["bg"],Generate_pswd_button["bg"],resize_btn["bg"],Type_pasword_input["bg"],text_3["bg"] = Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme

    elif Theme == "violet":
       Theme = "orange"
       root['bg'],text["bg"],input_name["bg"],text_2["bg"],input_symbol_count["bg"],password_here["bg"],Generate_pswd_button["bg"],resize_btn["bg"],Type_pasword_input["bg"],text_3["bg"] = Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme

    elif Theme == "orange":
       Theme = "light Blue"
       root['bg'],text["bg"],input_name["bg"],text_2["bg"],input_symbol_count["bg"],password_here["bg"],Generate_pswd_button["bg"],resize_btn["bg"],Type_pasword_input["bg"],text_3["bg"] = Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme,Theme
text = Label(root,text="Enter the number of password characters below",bg=Theme)
input_name = Entry(root,textvariable=name,bg=Theme)
text_2 = Label(root,text="Enter name of program/game/social media,below",bg=Theme)
input_symbol_count = Entry(root,textvariable=symbol_count,bg=Theme)
password_here = Label(root,text="Here will be your password",bg=Theme)
Type_pasword_input = Entry(root,textvariable=Type_pasword,bg=Theme)
text_3 = Label(root,text="Enter type of password,types:all,numbers,small_letters,big_letters,symbols,big_leters_small_leters_numbers,big_leters_small_leters below",bg=Theme)
Generate_pswd_button = Button(root,text="Generate",bg=Theme,command=func)
resize_btn = Button(root,text="Theme",command=theme,bg=Theme)

text.pack()
input_symbol_count.pack()
text_2.pack()
input_name.pack()
password_here.pack()
text_3.pack()
Type_pasword_input.pack()
Generate_pswd_button.pack()
resize_btn.pack(side=BOTTOM)

root.mainloop()
