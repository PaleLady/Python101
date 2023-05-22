#GUI

from tkinter import *
from tkinter import ttk


GUI = Tk()
GUI.title('โปรแกรมของฉัน')
GUI.geometry('500x300')

v_text = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_text)
E1.pack()

def Click():
	print('กำลังคลิก...')
	text = v_text.get()
	print('Text: ',text)

B1 = ttk.Button(GUI, text = 'Click me!!',command=Click)
B1.pack(ipadx = 20,ipady = 30,pady = 30)


GUI.mainloop()