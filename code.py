from tkinter import *
from math import sin
from math import cos
from math import tan
from math import log
expression = ""

def press(a):
    global expression
    expression  = expression  + str(a)
    equation.set(expression)

def button_equal():
    try:

        global expression
        pi=3.14159
        e=2.71828
        total = str(eval(expression))
        equation.set(total)
        expression  = ""
    except:

        equation.set(" error ")
        expression = ""

def button_clear():
    global expression
    expression  = ""
    equation.set("")

def sin():
    global expression
    expression = expression + "sin"
    equation.set(expression)
def cos():
    global expression
    expression = expression + "cos"
    equation.set(expression)

def tan():
    global expression
    expression = expression + "tan"
    equation.set(expression)

def log():
    global expression
    expression = expression + "log"
    equation.set(expression)

if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="white")

    gui.title("Adya's Calculator")

    gui.geometry("265x175")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation)

    expression_field.grid(columnspan=4, ipadx=70)

    equation.set('enter your equation')

    sin = Button(gui, text=' sin ', fg='black', bg='white',
                     command=sin, height=1, width=7)
    sin.grid(row=2, column=0)

    cos = Button(gui, text=' cos ', fg='black', bg='white',
                     command=cos, height=1, width=7)
    cos.grid(row=2, column=1)

    tan = Button(gui, text=' tan ', fg='black', bg='white',
                     command=tan, height=1, width=7)
    tan.grid(row=2, column=2)

    log = Button(gui, text=' log ', fg='black', bg='white',
                     command=lambda: log, height=1, width=7)
    log.grid(row=2, column=3)

    button1 = Button(gui, text=' ( ', fg='black', bg='white',
                     command=lambda: press("("), height=1, width=7)
    button1.grid(row=3, column=0)

    button2 = Button(gui, text=' ) ', fg='black', bg='white',
                     command=lambda: press(")"), height=1, width=7)
    button2.grid(row=3, column=1)

    button3 = Button(gui, text=' e ', fg='black', bg='white',
                     command=lambda: press("e"), height=1, width=7)
    button3.grid(row=3, column=2)

    button4 = Button(gui, text=' pi ', fg='black', bg='white',
                     command=lambda: press("pi"), height=1, width=7)
    button4.grid(row=3, column=3)

    button5 = Button(gui, text=' 7 ', fg='black', bg='white',
                     command=lambda: press(7), height=1, width=7)
    button5.grid(row=4, column=0)

    button6 = Button(gui, text=' 8 ', fg='black', bg='white',
                     command=lambda: press(8), height=1, width=7)
    button6.grid(row=4, column=1)

    button7= Button(gui, text=' 9 ', fg='black', bg='white',
                  command=lambda: press(9), height=1, width=7)
    button7.grid(row=4, column=2)

    division = Button(gui, text=' / ', fg='black', bg='white',
                   command=lambda: press("/"), height=1, width=7)
    division.grid(row=4, column=3)

    button8 = Button(gui, text=' 4 ', fg='black', bg='white',
                      command=lambda: press(4), height=1, width=7)
    button8.grid(row=5, column=0)

    button9 = Button(gui, text=' 5 ', fg='black', bg='white',
                    command=lambda: press(5), height=1, width=7)
    button9.grid(row=5, column=1)

    button10 = Button(gui, text=' 6 ', fg='black', bg='white',
                    command=lambda: press(6), height=1, width=7)
    button10.grid(row=5, column=2)

    multiply = Button(gui, text=' * ', fg='black', bg='white',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=5, column=3)

    button11= Button(gui, text=' 1 ', fg='black', bg='white',
                    command=lambda: press(1), height=1, width=7)
    button11.grid(row=6, column=0)

    equal = Button(gui, text=' 2 ', fg='black', bg='white',
                   command=lambda: press(2), height=1, width=7)
    equal.grid(row=6, column=1)

    clear = Button(gui, text=' 3 ', fg='black', bg='white',
                   command=lambda: press(3), height=1, width=7)
    clear.grid(row=6, column=2)

    difference = Button(gui, text=' - ', fg='black', bg='white',
                   command=lambda: press("-"), height=1, width=7)
    difference.grid(row=6, column=3)

    button0 = Button(gui, text=' 0 ', fg='black', bg='white',
                   command=lambda: press(0), height=1, width=7)
    button0.grid(row=7, column=0)

    clear = Button(gui, text=' Clear ', fg='black', bg='orange',
                   command=button_clear, height=1, width=7)
    clear.grid(row=7, column=1)

    equal = Button(gui, text=' = ', fg='black', bg='orange',
                   command=button_equal, height=1, width=7)
    equal.grid(row=7, column=2)

    add = Button(gui, text=' + ', fg='black', bg='white',
                    command=lambda: press("+"), height=1, width=7)
    add.grid(row=7, column=3)


    gui.mainloop()
