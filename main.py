from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=0)
root.configure(bg='SteelBlue4')
frm.grid()
root.geometry("500x500")
root.resizable(width=False, height=False)
root.title('Autotrader v1.0.0')

text = Label(text="Autotrader pre alpha v1.0.0")
text.place(x=350, y=2)

ttk.Button(frm, text="Quit/Stop", command=root.destroy).grid(column=0, row=0)



root.mainloop()