from tkinter import *
import tkinter.ttk

def makeMenu():
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    window.config(menu=menubar)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

def makeTab():
    notebook = tkinter.ttk.Notebook(window, width=800, height=500)
    notebook.pack()

    tab1 = tkinter.Frame(window)
    notebook.add(tab1, text=" Member ")
    tab2 = tkinter.Frame(window)
    notebook.add(tab2, text=" Product ")
    tab3 = tkinter.Frame(window)
    notebook.add(tab3, text=" LogMoniter ")

    return tab1, tab2, tab3

def makeTreeview():
    labelTitle = tkinter.Label(tab1, text="Member List")
    labelTitle.grid(row=0, column=0, columnspan=3, sticky='ew')

    tree = tkinter.ttk.Treeview(tab1, columns=["name", "age", "address", "phone"], show='headings')
    tree.grid(row=1, column=0, columnspan=3, sticky='ew')

    tree.column("name", width=100)
    tree.heading("name", text="이름", anchor="center")

    tree.column("age", width=50)
    tree.heading("age", text="나이", anchor="center")

    tree.column("address", width=250)
    tree.heading("address", text="주소", anchor="center")

    tree.column("phone", width=150)
    tree.heading("phone", text="전화", anchor="center")

    treeValueList = [["HongGilDong", "20", "Seoul GanNam", '010-1100-2200'],
                     ["KittChoi", "34", "Busan BuDong", '010-3230-2770'],
                     ["JohnPark", "21", "Deajeon SeGu", '010-1300-1220']]

    for i in range(len(treeValueList)):
        tree.insert("", "end", text='', values=treeValueList[i], iid=i)

def donothing():
   makeTreeview()


def makeTab2():
    frame = tkinter.Frame(tab2, width=300, height = 300, bg='yellow')
    frame.grid(row=0, column=0,sticky='ew')

    tree = tkinter.ttk.Treeview(frame, columns=(1, 2, 3), height=5, show="headings")
    tree.pack(side='left')

    tree.heading(1, text="A")
    tree.heading(2, text="B")
    tree.heading(3, text="C")

    tree.column(1, width=100)
    tree.column(2, width=100)
    tree.column(3, width=100)

    scroll = tkinter.ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scroll.set)

    data = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["10", "11", "12"],
            ["13", "14", "15"],
            ["16", "17", "18"]]

    for val in data:
        tree.insert('', 'end', values=(val[0], val[1], val[2]))

    label = Label(tab2, text="default text")
    label.grid(row=1, column=0,sticky='ew')

    def click_item(event):
        selectedItem = tree.focus()
        getValue = tree.item(selectedItem).get('values')
        label.configure(text=getValue)

    tree.bind('<ButtonRelease-1>', click_item)


window = Tk()
window.title("Member")
window.geometry("800x500+200+200")
tab1, tab2, tab3 = makeTab()
makeMenu()
makeTab2()

window.mainloop()
