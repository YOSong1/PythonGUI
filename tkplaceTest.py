import tkinter as tk

win=tk.Tk()
win.geometry("640x400+100+100")
win.resizable(False, False)

frame1 =tk.Frame(win, width=200, height = 300, bg='yellow')
frame2 =tk.Frame(win, width=200, height = 100, bg='red')
frame3 = tk.LabelFrame(win, text='선택종류', width=300, height=80, bg='blue')

label_name = tk.Label(frame1, text='이름')
label_addr = tk.Label(frame1, text='주소')
entryname = tk.Entry(frame1, width=100)
entryaddr = tk.Entry(frame1, width=100)

label_kor = tk.Label(frame2, text='국어')
label_math = tk.Label(frame2, text='수학')
entrykor = tk.Entry(frame2, width=100)
entrymath = tk.Entry(frame2, width=100)

frame1.place(x=10, y=10)
frame2.place(x=120, y=0)
# frame3.place(x=0, y = 120)
label_name=label_name.place(x=0, y=0)
label_addr=label_addr.place(x=0, y=20)
entryname=entryname.place(x=40, y=0)
entryname=entryaddr.place(x=40, y=20)

label_kor.pack()
label_math.pack()
entrykor.pack()
entrymath.pack()


win.mainloop()
