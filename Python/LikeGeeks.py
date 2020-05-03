#url : https://likegeeks.com/python-gui-examples-tkinter-tutorial/amp/

#Create You first GUI Application
from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.mainloop()


#setting window size
from tkinter import *
window = Tk()
window.title("set windwo size")
window.geometry('200x200')
window.mainloop()


#create a label weidget
#set label font and size
from tkinter import *
window = Tk()
window.title("add label widget")
lbl = Label(window, text = "label text:",font=("Arial Bold",50))
lbl.grid(column=0, row=0)
window.mainloop()

#add a button widget
from tkinter import *
window = Tk()
window.title("add button widget")
btn = Button(window,text="Click Me")
btn.grid(column = 1,row = 0)
window.mainloop()

#add a entry (text box)
from tkinter import *
window = Tk()
window.title("add text box (entry)")
txt = Entry(window,width = 10);txt.grid(column=0,row=0)
window.mainloop()

#get text box value when a btn is clicked
from tkinter import *
window = Tk()
window.title("get text from entry");window.geometry('400x400')
lbl=Label(window,text="Enter value: ");lbl.grid(column=0,row=0)
txt=Entry(window, width=15);txt.grid(column=1,row=0)
def get_text():
    res = "you entered: "+ txt.get()
    print(res)
btn = Button(window, text="get value",command=get_text);btn.grid(column=2,row=0)

#set focus to a widget
from tkinter import *
window = Tk()
window.title("set label widget");window.geometry('200x200')
lbl = Label(window, text = "text label");lbl.grid(column=0,row=0)
txt = Entry(window, width = 10);txt.grid(column=1,row=0)
btn = Button(window, text="Click Me");btn.grid(column=2,row=0)
txt.focus()
window.mainloop()

#set the state of an Entry (text box) [disabled, normal, or readonly]
from tkinter import *
window = Tk()
window.title("set label widget");window.geometry('200x200')
txt = Entry(window, width = 10,state="disabled");txt.grid(column=1,row=0)
window.mainloop()

#add a comobox widget
from tkinter import *
from tkinter.ttk import * #necessary to import tkinter.ttk
window = Tk();window.geometry('200x200');window.title("add combobox widget")
#create combobox
combo = Combobox(window);combo.grid(column=0,row=0)
#define choices
combo['values'] = ("val1", 2, 3.1)
#setecl value
combo.current(0)
window.mainloop()

#add checkbox widget
from tkinter import *
window = Tk();window.geometry('200x200');window.title("add checkbox")
#this is used to check the checkbox
chk_state = BooleanVar();chk_state.set(True) 
chk = Checkbutton(window, text = 'Choice', var = chk_state);chk.grid(column=0,row=0)
window.mainloop()

#add radio buttons widget
from tkinter import *
window = Tk();window.title("add radio button");window.geometry('200x200')
#you should set the a different value for each radio button
rad1 = Radiobutton(window, text = "First", value = 1);rad1.grid(column = 0, row = 0)
rad2 = Radiobutton(window, text = "Second", value = 2);rad2.grid(column = 1, row = 0)
rad3 = Radiobutton(window, text = "Third", value = 3);rad3.grid(column = 2, row = 0)
window.mainloop()

#set a command on click
from tkinter import *
window = Tk();window.title("add radio button");window.geometry('200x200')
def rad1_clicked():
    print("radio1 was choosed")
rad1 = Radiobutton(window, text = "First", value = 1,command = rad1_clicked);rad1.grid(column = 0, row = 0)
rad2 = Radiobutton(window, text = "Second", value = 2);rad2.grid(column = 1, row = 0)
window.mainloop()

#get selected radio button value
from tkinter import *
window = Tk();window.title("get selected radio button value")
#you should set the a different value for each radio button
selected = IntVar()
rad1 = Radiobutton(window, text="First", value=1 ,variable=selected);rad1.grid(column = 0, row = 0)
rad2 = Radiobutton(window, text="Second", value=2 ,variable=selected);rad2.grid(column = 1, row = 0)
rad3 = Radiobutton(window, text="Third", value=3 ,variable=selected);rad3.grid(column = 2, row = 0)
def get_Selected_rad():print(selected.get())
btn = Button(window, text="Click Me", command=get_Selected_rad);btn.grid(column=4,row=0)
window.mainloop()

#add a scrolledText widget (textArea)
from tkinter import *
from tkinter import scrolledtext
window = Tk();window.title("add textArea")
txt = scrolledtext.ScrolledText(window,width=40,height=10);txt.grid(column=0,row=0)
#aading text
txt.insert(INSERT, "inseting a text")
#deleting text after 5 sec
txt.delete(1.0, END)
window.mainloop()

#add message box
from tkinter import *
from tkinter import messagebox
window = Tk();window.title("show message box");window.geometry('400x200')
messagebox.showinfo("Message title", "Message content")
messagebox.showerror("error title", "error content")
res = messagebox.askquestion("Message title", "Message content")
res = messagebox.askyesno("Message title", "Message content")
res = messagebox.askokcancel("Message title", "Message content")
#res is True or False
window.mainloop()

#add SpinBox (numeric widget)
from tkinter import *
from tkinter import messagebox
window = Tk();window.title("add numeric widget");window.geometry('400x200')
spin = Spinbox(window, from_=0, to=100,width=5,state="normal");spin.grid(column=0,row=0)
spin1 = Spinbox(window, values=(1,4,8),width=5,state="readonly");spin1.grid(column=1,row=0)
#set defaultvalue
var = IntVar();var.set(10)
spin3 = Spinbox(window, from_=0, to=100,width=5,state="readonly",textvariable=var);spin3.grid(column=2,row=0)
window.mainloop()

#add progressbar widget
from tkinter import *
from tkinter.ttk import Progressbar
window = Tk();window.title("add progressbar widget");window.geometry('400x200')
pb = Progressbar(window, length = 200);pb.grid(column=0,row=0)
#set pb value
pb['value'] = 70
#set the color
from tkinter import ttk
#style = ttk.Style();style.theme_use("default");style.configure("black.Horizontal.TProgressbar",backgrounf='black')
#pb1 = Progressbar(window, length = 200, style='black.Horizontal.TProgressbar');pb1.grid(column=0,row=1);pb1['value'] = 70
window.mainloop()

#add file dialog
from tkinter import *
from tkinter import filedialog
window = Tk();window.title("open file dialog");window.geometry('400x200')
file = filedialog.askopenfilename()
file = filedialog.askopenfilenames()
#specify filetype
file = filedialog.askopenfilename(filetypes=(('Text Files','*.txt'),('all files','*.*')))
#directory
dir = filedialog.askdirectory()
#specify the start directory
from os import path;dir = filedialog.askdirectory(initialdir=path.dirname(__file__))
window.mainloop()

#add menubar
from tkinter import *
from tkinter import Menu
window = Tk();window.title("add menubar");window.geometry('400x200')
#add button
menu = Menu(window);menu.add_command(label="File")
#add menu to the button
new_item = Menu(menu)
new_item = Menu(menu, tearoff=0) # to remove dashes
new_item.add_command(label='Copy')
#new_item.add_separator() #optinal to separate options
def rep_clicked():print("Replace Clicked")
new_item.add_command(label='Replace', command=rep_clicked)
menu.add_cascade(label="Edit",menu=new_item)
window.config(menu=menu)
window.mainloop()

#add notebook (tab control)
"""
3 steps:
1_create a tab contorl from Notebook class
2_Create a tab contorl from Frame class
3_Add that tab to the tab control
4_Pack the tab control so it becomes visible in the window
"""
from tkinter import *
from tkinter import ttk
window = Tk();window.title("Add a NoteBook");window.geometry('200x200')
tc = ttk.Notebook(window);
tab1=ttk.Frame(tc);tc.add(tab1, text="First")
tab2=ttk.Frame(tc);tc.add(tab2, text="Second")
#add widgets to tab pages:
lbl=Label(tab1,text="Enter value: ");lbl.grid(column=0,row=0)
lb2=Label(tab2,text="Enter value: ");lb2.grid(column=0,row=0)

tc.pack(expand=1, fill="both")
window.mainloop()

#add padding to widgets
from tkinter import *
window = Tk();window.geometry('300x200');window.title('set padding');
lbl1 = Label(window, text="labl1", padx=20, pady=20);lbl1.grid(column=0,row=0)
window.mainloop()
