from tkinter import *

root = Tk()
top_frame = Frame(root)
top_frame.pack()

button1=Button(top_frame,text="Кнопка 1",fg="green")
button2=Button(top_frame,text="Кнопка 2",fg="blue")
button3=Button(top_frame,text="Кнопка 3",fg="red")
button4=Button(top_frame,text="Кнопка 4",fg="green")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=BOTTOM)
button4.pack(side=BOTTOM)

root.mainloop()
