import tkinter as tk
import os

cal = tk.Tk()
cal.title("Calculator")

operator = ""
variable = tk.StringVar()
display = tk.Entry(cal,font=("arial", 20, "bold"),bd=25,textvariable=variable)
display.grid(columnspan=5)

def click(number):
    global operator
    operator = operator + str(number)
    variable.set(operator)

button1 = tk.Button(cal, text="1", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(1))
button1.grid(row=1, column=0)
button2 = tk.Button(cal, text="2", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(2))
button2.grid(row=1, column=1)
button3 = tk.Button(cal, text="3", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(3))
button3.grid(row=1, column=2)
button4 = tk.Button(cal, text="4", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(4))
button4.grid(row=2, column=0)
button5 = tk.Button(cal, text="5", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(5))
button5.grid(row=2, column=1)
button6 = tk.Button(cal, text="6", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(6))
button6.grid(row=2, column=2)
button7 = tk.Button(cal, text="7", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(7))
button7.grid(row=3, column=0)
button8 = tk.Button(cal, text="8", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(8))
button8.grid(row=3, column=1)
button9 = tk.Button(cal, text="9", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(9))
button9.grid(row=3, column=2)
button0 = tk.Button(cal, text="0", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(0))
button0.grid(row=4, column=1)
button_dot = tk.Button(cal, text=".", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click("."))
button_dot.grid(row=4, column=0)
button_coma = tk.Button(cal, text=",", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click(","))
button_coma.grid(row=4, column=2)
button_clear = tk.Button(cal, text="C", font=("arial",20,"bold"),bd=5,padx=10)
button_clear.grid(row=1, column=3)
button_plus = tk.Button(cal, text="+", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click("+"))
button_plus.grid(row=2, column=3)
button_min = tk.Button(cal, text="-", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click("-"))
button_min.grid(row=3, column=3)
button_ex = tk.Button(cal, text="*", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click("*"))
button_ex.grid(row=4, column=3)
button_div = tk.Button(cal, text="/", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click("/"))
button_div.grid(row=5, column=3)
button_eq = tk.Button(cal, text="=", font=("arial",20,"bold"),bd=5,padx=10,command= lambda : click("="))
button_eq.grid(row=5, column=1)




cal.mainloop()