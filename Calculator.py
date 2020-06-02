from tkinter import *

interface = Tk()
interface.title("Calculator")
interface.configure(background = "#4f4f4f")


input_field = Entry(interface, width=20, borderwidth=4, bg= "#7aff97", font = ("Magneto", 15), justify="right")
input_field.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5, ipadx= 10, ipady= 10)

def button_action(number):

    current = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current)+str(number))
    

def button_addition():
    number = input_field.get()
    global f_num, operation
    operation = "a"
    f_num = int(number)
    input_field.delete(0, END)

def button_subtraction():
    number = input_field.get()
    global f_num, operation
    operation = "s"
    f_num = int(number)
    input_field.delete(0, END)

def button_multiplication():
    number = input_field.get()
    global f_num, operation
    operation = "m"
    f_num = int(number)
    input_field.delete(0, END)

def button_division():
    number = input_field.get()
    global f_num, operation
    operation = "d"
    f_num = int(number)
    input_field.delete(0, END)

def button_equal_ac():
    second = input_field.get()
    input_field.delete(0, END)
    
    if (operation == "a"):
        input_field.insert(0, f_num+int(second))

    if (operation == "s"):
        input_field.insert(0, f_num-int(second))

    if (operation == "m"):
        input_field.insert(0, f_num*int(second))

    if (operation == "d"):
        input_field.insert(0, f_num/int(second))

def button_clear_():
    input_field.delete(0, END)

button_1 = Button(interface, text="1", padx=50, pady= 19, command=lambda: button_action(1), bg = "#8c8c8c")
button_2 = Button(interface, text="2", padx=50, pady= 19, command=lambda: button_action(2), bg = "#8c8c8c")
button_3 = Button(interface, text="3", padx=50, pady= 19, command=lambda: button_action(3), bg = "#8c8c8c")
button_4 = Button(interface, text="4", padx=50, pady= 19, command=lambda: button_action(4), bg = "#8c8c8c")
button_5 = Button(interface, text="5", padx=50, pady= 19, command=lambda: button_action(5), bg = "#8c8c8c")
button_6 = Button(interface, text="6", padx=50, pady= 19, command=lambda: button_action(6), bg = "#8c8c8c")
button_7 = Button(interface, text="7", padx=50, pady= 19, command=lambda: button_action(7), bg = "#8c8c8c")
button_8 = Button(interface, text="8", padx=50, pady= 19, command=lambda: button_action(8), bg = "#8c8c8c")
button_9 = Button(interface, text="9", padx=50, pady= 19, command=lambda: button_action(9), bg = "#8c8c8c")
button_0 = Button(interface, text="0", padx=108, pady= 19, command=lambda: button_action(0), bg = "#8c8c8c")

button_clear = Button(interface, text="clear", padx = 175, pady=18, command=button_clear_, bg="#e31010")

button_add = Button(interface, text="+", padx=26, pady= 19, command=button_addition, bg="#61c2ff")
button_sub = Button(interface, text="-", padx=26, pady= 19, command=button_subtraction, bg="#61c2ff")
button_multiply = Button(interface, text="x", padx=26, pady= 19, command=button_multiplication, bg="#61c2ff")
button_divide = Button(interface, text="/", padx=26, pady= 19, command=button_division, bg="#61c2ff")
button_equal = Button(interface, text="=", padx=49, pady= 19, command=button_equal_ac, bg= "#19e623")

button_0.grid(row=4, column=0, columnspan=2)

button_1.grid(row=3, column=0 )
button_2.grid(row=3, column=1 )
button_3.grid(row=3, column=2 )

button_4.grid(row=2, column=0 )
button_5.grid(row=2, column=1 )
button_6.grid(row=2, column=2 )

button_7.grid(row=1, column=0 )
button_8.grid(row=1, column=1 )
button_9.grid(row=1, column=2 )

button_add.grid(row=1, column=4 )
button_sub.grid(row=2, column=4 )
button_multiply.grid(row=3, column=4 )
button_divide.grid(row=4, column=4 )
button_equal.grid(row=4, column=2 )
button_clear.grid(row=5, column=0, columnspan=5)

interface.mainloop()