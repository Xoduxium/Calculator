from tkinter import *
from cmath import *

def button_click(num):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(num))

def button_clear():
    input.delete(0, END)

def button_add():
    first_num = input.get()
    global f_num
    global math
    math = "+"
    f_num = float(first_num)
    input.delete(0, END)
    global down
    down = "True"

def button_equal():
    global second_num
    second_num = input.get()
    input.delete(0, END)

    if math == "+":
        input.insert(0, f_num + float(second_num))
    
    if math == "-":
        input.insert(0, f_num - float(second_num))

    if math == "*":
        input.insert(0, f_num * float(second_num))

    if math == "/":
        input.insert(0, f_num / float(second_num))
    
    Storia()

def button_sub():
    first_num = input.get()
    global f_num
    global math
    math = "-"
    f_num = float(first_num)
    input.delete(0, END)
    global down
    down = "True"

def button_mul():
    first_num = input.get()
    global f_num
    global math
    math = "*"
    f_num = float(first_num)
    input.delete(0, END)
    global down
    down = "True"

def button_div():
    first_num = input.get()
    global f_num
    global math
    math = "/"
    f_num = float(first_num)
    input.delete(0, END)
    global down
    down = "True"

def button_sqr():
    first_num = input.get()
    global f_num
    global math
    math = "²"
    f_num = float(first_num)
    input.delete(0, END)
    input.insert(0, f_num ** 2)
    Storia()

def button_root():
    first_num = input.get()
    global f_num
    global math
    math = "²√"
    f_num = float(first_num)
    input.delete(0, END)
    global radice
    radice = sqrt(f_num)
    input.insert(0, radice.real)
    Storia()

def button_1div():
    first_num = input.get()
    global f_num
    global math
    math = "1 /"
    f_num = float(first_num)
    input.delete(0, END)
    input.insert(0, 1 / f_num)
    Storia()

def button_Asso():
    first_num = input.get()
    global f_num
    global math
    math = "+/-"
    f_num = float(first_num)
    input.delete(0, END)
    input.insert(0, -1 * f_num)
    Storia()

def button_BSpace():
    global current
    current = input.get()
    current = current[:-1]
    input.delete(0, END)
    input.insert(0, current)

def button_Percen():
    first_num = input.get()
    global f_num
    global math
    math = "%"
    f_num = float(first_num)
    input.delete(0, END)
    input.insert(0, f_num / 100)
    Storia()

history_text = ""
down = ""

def Storia():
    global history_text
    global f_num  # Include f_num to properly store the first number
    global down

    # Construct the history entry
    if down == "True":
        history_entry = f"{f_num} {math} {float(second_num)}"

    if math == "1 /":
        history_entry = f"{math} {f_num}"

    if math == "%":
        history_entry = f"{f_num}{math}"

    if math == "+/-":
        history_entry = f"{math}{f_num}"
    
    if math == "²√":
        history_entry = f"{math}{f_num}"

    if math == "²":
        history_entry = f"{f_num}{math}"

    # Append the entry to the history_text
    history_text += history_entry
    
    # Update the history textbox
    history.delete(0, END)
    history.insert(END, history_text)

def button_DelAll():
    global history_text
    history_text = ""  # Reset history text to empty string
    history.delete(0, END)
    input.delete(0, END)

def answer():
    history.delete(0, END)
    global history_text
    history_text = ""

# window
window = Tk()
window.title('Calculator')
# window.geometry('with x height')

# title
title_label = Label(master = window, text = 'Calculator', font = 'Calibri 20 bold')
title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# input
input = Entry(window, width=35)
input.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# history
history = Entry(window, width=25)
history.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# buttons
button1 = Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1), bg='white')
button2 = Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2), bg='white')
button3 = Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3), bg='white')

button4 = Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4), bg='white')
button5 = Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5), bg='white')
button6 = Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6), bg='white')

button7 = Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7), bg='white')
button8 = Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8), bg='white')
button9 = Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9), bg='white')
button0 = Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0), bg='white')

buttonAdd = Button(window, text="+", padx=19, pady=10, command=button_add)
buttonSub = Button(window, text="-", padx=20, pady=10, command=button_sub)
buttonMul = Button(window, text="*", padx=20, pady=10, command=button_mul)
buttonDiv = Button(window, text="/", padx=20, pady=10, command=button_div)
buttonEqual = Button(window, text="=", padx=19, pady=10, command=button_equal, bg='#0067C0', fg='white')
buttonClear = Button(window, text="C", padx=19, pady=10, command=button_clear)
buttonSqr = Button(window, text="x²", padx=18, pady=10, command=button_sqr)
buttonRoot = Button(window, text="²√x", padx=14, pady=10, command=button_root)
button1div = Button(window, text="¹/x", padx=16, pady=10, command=button_1div)
buttonAssoluto = Button(window, text="+/-", padx=14, pady=10, command=button_Asso, bg='white')
buttonComma = Button(window, text=".", padx=22, pady=10, command=lambda: button_click("."), bg='white')
buttonBSpace = Button(window, text="←", padx=18, pady=10, command=button_BSpace)
buttonPercentage = Button(window, text="%", padx=18, pady=10, command=button_Percen)
buttonDelAll = Button(window, text="CE", padx=16, pady=10, command=button_DelAll)
buttonANS = Button(window, text="Ans", padx=41, pady=10, command=answer, bg='#0A9627', fg='white')

# Row 3
buttonPercentage.grid(row=3, column=0) #
buttonDelAll.grid(row=3, column=1) #
buttonClear.grid(row=3, column=2) #
buttonBSpace.grid(row=3, column=3) #

# Row 4
button1div.grid(row=4, column=0) #
buttonSqr.grid(row=4, column=1) #
buttonRoot.grid(row=4, column=2) #
buttonDiv.grid(row=4, column=3) #

# Row 5
button7.grid(row=5, column=0) #
button8.grid(row=5, column=1) #
button9.grid(row=5, column=2) #
buttonMul.grid(row=5, column=3) #

# Row 6
button4.grid(row=6, column=0) #
button5.grid(row=6, column=1) #
button6.grid(row=6, column=2) #
buttonSub.grid(row=6, column=3) #

# Row 7
button1.grid(row=7, column=0) #
button2.grid(row=7, column=1) #
button3.grid(row=7, column=2) #
buttonAdd.grid(row=7, column=3) #

# Row 8
buttonAssoluto.grid(row=8, column=0) #
button0.grid(row=8, column=1) #
buttonComma.grid(row=8, column=2) #
buttonEqual.grid(row=8, column=3) #

# Row 9
buttonANS.grid(row=9, column=0, columnspan=4)

# run
window.mainloop()