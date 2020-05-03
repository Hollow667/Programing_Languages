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
