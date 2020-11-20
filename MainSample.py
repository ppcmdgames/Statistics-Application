from tkinter import *
window=Tk()
# Code to add widgets
# Syntax for Button: Variable = Button(window, attributes)
# Place specifies location. Syntax: Variable.place(x= x position, y= y position)
# Position is an integer value
btn1=Button(window, text="Button 1", fg="blue")
btn1.place(x=150, y=250)
btn2=Button(window, text="Button 2", fg="green")
btn2.place(x=300, y=250)
# Create label widget
title=Label(window, text="Label Widget", fg="black", font=("Arial", 16))
title.place(x=175, y=95)
# Entry widget's constructor has two variables, bd (border size) and show
# Defaults: bd = 2px
txtfield=Entry(window, text="Entry widget", bd=2)
txtfield.place(x=190, y=150)

window.title('Sample Window')
window.geometry("500x400+10+20")
window.mainloop()
