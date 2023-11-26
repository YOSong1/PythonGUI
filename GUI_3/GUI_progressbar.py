import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import  sleep         # careful - this can freeze the GUI

win = tk.Tk()   

      
win.title("Python GUI")  

tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible


mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)


a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky='W')


def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get())


name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')               # align left/West


action = ttk.Button(mighty, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)


def _spin():
    value = spin.get()
    print(value)
    scrol.insert(tk.INSERT, value + '\n')
     

spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=_spin) # using range
spin.grid(column=0, row=2)

 
scrol_w  = 30
scrol_h  =  3
scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scrol.grid(column=0, row=3, sticky='WE', columnspan=3)                    


mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)


chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=0, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=0, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=0, sticky=tk.W)                     


def checkCallback(*ignoredArgs):
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 


chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   


colors = ["Blue", "Gold", "Red"]   


def radCall():
    radSel=radVar.get()
    if   radSel == 0: mighty2.configure(text='Blue')
    elif radSel == 1: mighty2.configure(text='Gold')
    elif radSel == 2: mighty2.configure(text='Red')


radVar = tk.IntVar()

radVar.set(99)                                 
 

for col in range(3):                             
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=1, sticky=tk.W)             # row=6



progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2) 

def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i   # increment progressbar
        progress_bar.update()       # have to call update() in loop
    progress_bar["value"] = 0       # reset/clear progressbar  

def start_progressbar():
    progress_bar.start()
    
def stop_progressbar():
    progress_bar.stop()
 
def progressbar_stop_after(wait_ms=1000):    
    win.after(wait_ms, progress_bar.stop)
    

buttons_frame = ttk.LabelFrame(mighty2, text=' ProgressBar ')
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)        


ttk.Button(buttons_frame, text=" Run Progressbar   ", command=run_progressbar).grid(column=0, row=0, sticky='W')  
ttk.Button(buttons_frame, text=" Start Progressbar  ", command=start_progressbar).grid(column=0, row=1, sticky='W')  
ttk.Button(buttons_frame, text=" Stop immediately ", command=stop_progressbar).grid(column=0, row=2, sticky='W')  
ttk.Button(buttons_frame, text=" Stop after second ", command=progressbar_stop_after).grid(column=0, row=3, sticky='W')  
 
for child in buttons_frame.winfo_children():  
    child.grid_configure(padx=2, pady=2) 
 
for child in mighty2.winfo_children():  
    child.grid_configure(padx=8, pady=2) 

    
def _quit():
    win.quit()
    win.destroy()
    exit() 
    
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)


def _msgBox():
    msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2023.')  
    

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
menu_bar.add_cascade(label="Help", menu=help_menu)


win.iconbitmap('pyc.ico')

name_entered.focus()      # Place cursor into name Entry

win.mainloop()
