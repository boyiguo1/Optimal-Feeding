from Tkinter import *

class displayWindow(object):
    def __init__(self,master,title,option,dict):
        top=self.top=Toplevel(master)
        top.title(title);
        self.option = option;
        counter = 0;
        for day, price in dict.iteritems():
            Label(top, text = day).grid(row=counter,column = 1)
            Label(top,text=price).grid(row=counter,column = 2)
            counter = counter + 1;
        self.b = Button(top,text='OK',command=self.canceal)
        self.b.grid(row=counter,column=1)
        
        
    def canceal(self):
        self.top.destroy()