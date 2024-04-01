from tkinter import *
from cmath import *

def button_click(num):
    # input.delete(0, END)
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(num))

def button_clear():
    input.delete(0, END)

def button_add():
    first_num = input.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    input.delete(0, END)

def button_equal():
    second_num = input.get()
    input.delete(0, END)

    if math == "addition":
        input.insert(0, f_num + int(second_num))
    
    if math == "subtraction":
        input.insert(0, f_num - int(second_num))

    if math == "multiplication":
        input.insert(0, f_num * int(second_num))

    if math == "division":
        input.insert(0, f_num / int(second_num))
    
    if math == "1divx":
        input.insert(0, 1 / f_num)
    
def button_sub():
    first_num = input.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    input.delete(0, END)

def button_mul():
    first_num = input.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    input.delete(0, END)

def button_div():
    first_num = input.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    input.delete(0, END)

def button_sqr():
    first_num = input.get()
    global f_num
    global math
    math = "sqr"
    f_num = float(first_num)
    input.delete(0, END)
    input.insert(0, f_num ** 2)

def button_root():
    first_num = input.get()
    global f_num
    global math
    math = "root"
    f_num = float(first_num)
    input.delete(0, END)
    global radice
    radice = sqrt(f_num)
    input.insert(0, radice.real)

def button_1div():
    first_num = input.get()
    global f_num
    global math
    math = "1divx"
    f_num = float(first_num)
    input.delete(0, END)
    input.insert(0, 1 / f_num)

def button_Asso():
    first_num = input.get()
    global f_num
    global math
    math = "Asso"
    f_num = int(first_num)
    input.delete(0, END)
    input.insert(0, -1 * f_num)

# window
window = Tk()
window.title('Calculator')
# window.geometry('300x350') # window.geometry('with x height')

# title
title_label = Label(master = window, text = 'Calculator', font = 'Calibri 20 bold')
title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# input
input = Entry(window, width=35)
input.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# buttons
button1 = Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button2 = Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button3 = Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))

button4 = Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button5 = Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button6 = Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))

button7 = Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button8 = Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button9 = Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))
button0 = Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

buttonAdd = Button(window, text="+", padx=19, pady=10, command=button_add)
buttonSub = Button(window, text="-", padx=20, pady=10, command=button_sub)
buttonMul = Button(window, text="*", padx=20, pady=10, command=button_mul)
buttonDiv = Button(window, text="/", padx=20, pady=10, command=button_div)
buttonEqual = Button(window, text="=", padx=19, pady=10, command=button_equal)
buttonClear = Button(window, text="Del", padx=14, pady=10, command=button_clear)
buttonSqr = Button(window, text="x²", padx=18, pady=10, command=button_sqr)
buttonRoot = Button(window, text="²√x", padx=14, pady=10, command=button_root)
button1div = Button(window, text="¹/x", padx=15, pady=10, command=button_1div)
buttonAssoluto = Button(window, text="+/-", padx=15, pady=10, command=button_Asso)

button1.grid(row=5, column=0)
button2.grid(row=5, column=1) 
button3.grid(row=5, column=2) 

button4.grid(row=4, column=0) 
button5.grid(row=4, column=1) 
button6.grid(row=4, column=2) 

button7.grid(row=3, column=0) 
button8.grid(row=3, column=1) 
button9.grid(row=3, column=2) 
button0.grid(row=6, column=1) 

buttonEqual.grid(row=6, column=2) 
buttonAdd.grid(row=6, column=3)
buttonSub.grid(row=3, column=3)
buttonMul.grid(row=4, column=3)
buttonDiv.grid(row=5, column=3)
buttonClear.grid(row=2, column=3)
buttonSqr.grid(row=2, column=1)
buttonRoot.grid(row=2, column=2)
button1div.grid(row=2, column=0)
buttonAssoluto.grid(row=6, column=0)


# run
window.mainloop()