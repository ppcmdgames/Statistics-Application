# A sample program that performs basic mathematical operations

from tkinter import *

class Window:
    #  initializing function
    def __init__(program, win):
        program.title=Label(win, text="Sample Calculator", fg="blue", font=("Arial", 15))
        program.title.place(x=105, y=70)
        program.lbl1=Label(win, text="First Number")
        program.lbl2=Label(win, text="Second Number")
        program.rlbl=Label(win, text="Result")
        program.t1=Entry(bd=2)
        program.t2=Entry(bd=2)
        program.rtxt=Entry(bd=2)
        program.addbtn=Button(win, text="+", command=program.add)
        program.subbtn=Button(win, text="-", command=program.subtract)
        program.multibtn=Button(win, text="*", command=program.multiply)
        program.dividebtn=Button(win, text="/", command=program.divide)
        # Specify locations
        program.lbl1.place(x=80, y=130)
        program.lbl2.place(x=80, y=170)
        program.t1.place(x=250, y=130)
        program.t2.place(x=250, y=170)
        program.rtxt.place(x=125, y=290)
        program.rlbl.place(x=164, y=260)
        program.addbtn.place(x=110, y=230)
        program.subbtn.place(x=150, y=230)
        program.multibtn.place(x=190, y=230)
        program.dividebtn.place(x=230, y=230)
        # Function Bindings
        program.addbtn.bind('<Button-1>', program.add)
        program.subbtn.bind('<Button-1>', program.subtract)
        program.multibtn.bind('<Button-1>', program.multiply)
        program.dividebtn.bind('<Button-1>', program.divide)
    def add(program):
        num1=int(program.t1.get())
        num2=int(program.t2.get())
        result=num1+num2
        program.rtxt.delete(0, 'end')
        program.rtxt.insert(END, str(result))
    def subtract(program):
        num1=int(program.t1.get())
        num2=int(program.t2.get())
        result=num1-num2
        program.rtxt.delete(0, 'end')
        program.rtxt.insert(END, str(result))
    def multiply(program):
        num1=int(program.t1.get())
        num2=int(program.t2.get())
        result=num1*num2
        program.rtxt.delete(0, 'end')
        program.rtxt.insert(END, str(result))
    def divide(program):
        num1=int(program.t1.get())
        num2=int(program.t2.get())
        result=num1 / num2
        program.rtxt.delete(0, 'end')
        program.rtxt.insert(END, str(result))

window=Tk()
mywin=Window(window)
window.title('Calculator Program')
window.geometry("400x400+10+10")
window.mainloop()
