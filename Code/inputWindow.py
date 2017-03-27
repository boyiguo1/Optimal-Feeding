from Tkinter import *
import tkMessageBox

class inputWindow(object):
    def __init__(self,master,title,option):
        top=self.top=Toplevel(master)
        top.title(title)
        self.option = option
        self.l=Label(top,text="Please Type In The Value").grid(row = 0)
        #self.l.pack()
        self.e=Entry(top)
        self.e.grid(row=1)
        #self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.grid(row =2)
        self.b2 = Button(top,text='Canceal',command=self.canceal)
        self.b2.grid(row=2,column=1)
        
        
    def cleanup(self):
        self.value=self.e.get()
        if self.option == 0 or self.option == 1 or self.option == 3:
            try:
                int(self.value)
            except ValueError:
                tkMessageBox.showwarning(
                    'Input Error',
                    'Please input an Integer'
                )
                self.value = None
        else:
            try:
                float(self.value)
            except ValueError:
                tkMessageBox.showwarning(
                    'Input Error',
                    'Please input an Float'
                )
                self.value = None
        self.top.destroy()
        
    def canceal(self):
        self.value = None;
        self.top.destroy()