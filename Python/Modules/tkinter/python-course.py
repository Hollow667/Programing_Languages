#url : https://www.python-course.eu/tkinter_labels.php
'''
#0f01_Hello Tkinter Label
import tkinter as tk
#import Tkinter as tk #for python2
root = tk.Tk()
lbl=tk.Label(root, text="Hello Tkinter!");lbl.pack()
#root.mainloop()

#0f02_Using Images in Labels
import tkinter as tk
root = tk.Tk()
logo = tk.PhotoImage(file = "logo.gif")
#tk.Label(rootcompound = tk.CENTER,image=logo).pack(side="right")

#0f03_Colorized Labels in Various fonts
import tkinter as tk
root = tk.Tk()
tk.Label(root, text="colorized label", bg="black", fg="white").pack()

#0f05_Create a simple calculator
import tkinter as tk
root= tk.Tk();root.title("set a dynamic label content")
lbl = tk.Label(root, fg="green");lbl.pack()
def set_label():
    lbl.config(text="new text")
btn = tk.Button(root, text="Stop", width=25, command=set_label);btn.pack()
root.mainloop()

#0f06_message widget
import tkinter as tk
master = tk.Tk()
msg = tk.Message(master, text="message");msg.pack()
msg.config(width=0.04, bg="black",fg="white",font=('times',24,'italic'))
master.mainloop()

#0f07_Buttons
import tkinter as tk
root = tk.Tk();root.title("add button")
btn = tk.Button(root, text = "Click Me to exit", command=root.destroy)
btn.pack()
root.mainloop()

#0f08_add radio button
import tkinter as tk
root = tk.Tk()
v = tk.IntVar()
def Show_Choice():
    print(v.get())
langs = [["Python",1],["Java",2],["Ruby",3],["Sql",4]]
for [lang, val] in langs:
    tk.Radiobutton(root, text = lang, variable = v, value=val, command=Show_Choice).pack()
root.mainloop()

#0f09_add radio button with indicator
import tkinter as tk
root = tk.Tk()
v = tk.IntVar()
def Show_Choice():
    print(v.get())
langs = [["Python",1],["Java",2],["Ruby",3],["Sql",4]]
for [lang, val] in langs:
    tk.Radiobutton(root, text = lang, variable = v, value=val,width=20, command=Show_Choice, indicator=0).pack()
root.mainloop()

#0f10_checkboxes
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).pack()
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).pack()
def show():
    print("male {0}\nfemale {1}".format(var1.get(), var2.get()))
Button(master, text = "Click Me to exit", command=show).pack()
master.mainloop()

#0fa_add Entry widgets
from tkinter import *
root = Tk();root.title("add Entry")
entry1 = Entry(root);entry1.pack()
#add text (position, text)
entry1.insert(0,"some text")
#get text
print(entry1.get())
root.mainloop()

#0fb_simple calcualter
from tkinter import *
root = Tk();root.title("add Entry")
entry1 = Entry(root);entry1.pack()
lbl = Label(root, fg="green")
def set_label():
    lbl.config(text=str(eval(entry1.get())))
btn = Button(root, text="Calculate", width=10, command=set_label);btn.pack()
lbl.pack()
root.mainloop()

#0fc_add scale
from tkinter import *
master = Tk();master.geometry('400x400')
w = Scale(master,length=200, from_=-50, to=+50,tickinterval=10);w.pack()
w = Scale(master,orient=HORIZONTAL,length=600, from_=0, to=200,tickinterval=20);w.pack()
#tickinterval is the axis naming step
#set value
w.set(10)
#get value
print(w.get())
master.mainloop()

#0fd_add Text Widget
import tkinter as tk
root = tk.Tk()
txt=tk.Text(root, height=2, width=30)
txt.pack()
txt.insert(tk.END, "line1\nline2\nline3")
root.mainloop()

#0fe_add Text widget and Scrollbars
import tkinter as tk
root = tk.Tk()
s = tk.Scrollbar(root);s.pack(side=tk.RIGHT, fill=tk.Y)
txt=tk.Text(root, height=2, width=30)
s.config(command=txt.yview)
txt.pack()
txt.insert(tk.END, "line1\nline2\nline3")
txt.config(yscrollcommand=s.set)
root.mainloop()

#0ff_add menu
from tkinter import *
from tkinter.filedialog import askopenfilename
root = Tk()
txt=Text(root, height=20, width=100);txt.pack()
def NewFile():print("New File!")
def OpenFile():
    name=askopenfilename()
    text = open(name,"r")
    txt.insert(END,str(text.read()))
def About():
    print("thisi is a simple example of a menu")

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=NewFile)
filemenu.add_command(label="Open",command=OpenFile)

#0f10_widget.bind(event=<...>,handler=function_to_call)
#0f10_0f01_Button Click Event
from tkinter import *
root = Tk()
def hello(event):
    print("Single Click, Button-1")
def quit(event):
    print("Double Click")
widget = Button(None, text="Mouse Clicks")
widget.pack()
widget.bind('<Button-1>',hello);widget.bind('<Double-1>',quit);

#0f10_0f02_Mouse movement
from tkinter import *
def motion(event):
    print("Mouse position: (%s %s)" %(event.x, event.y))
    return
master = Tk()
msg = Message(master, text="mouse position")
msg.bind('<Motion>',motion)
msg.pack()
mainloop()
'''

'''
widget.bind(event=<...>,handler=function_to_call)
event:
<Button-1> : Left Mouse button Clicked
<Button-2> : Middle Mouse Button Clicked
<Button-3> : Right Mouse Button Clicked 
<Button-4> : Scroll Mouse Wheel Up
<Button-5> : Scroll Mouse Wheel Down
<Double-Button-1> : Left Mouse button Double Clicked
<Double-Button-2> : Middle Mouse Button Double Clicked
<Double-Button-3> : Right Mouse Button Double Clicked
<Motion> : Mouse Moved
<B1-Motion> : Mouse move and Left Button is hold down
<B2-Motion> : Mouse move and Middle Button is hold down
<B3-Motion> : Mouse move and Right Button is hold down
<ButtonRelease-1> : Left mouse button released
<ButtonRelease-2> : Middle mouse button released
<ButtonRelease-3> : Right mouse button released
<Enter> : The mouse entered a widget
<Leave> : mouse pointer left the widget
<FoucsIn> : Keyboard foucs moved to the widget
<FoucsOut> : Keyboard foucs moved from the widget
<Return> : user pressed the enter key
<Key> : the user pressed a key (string or special character)
<Shift-Up> : the user pressed the arrow-up and shift key
<Alt-Up> : the user pressed the arrow-up and Alt key
<Control-Up> : the user pressed the arrow-up and Control key
<Configure> : widget size changed

'''





















