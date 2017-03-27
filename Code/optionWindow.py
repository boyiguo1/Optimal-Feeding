from Tkinter import *

class optionWindow(object):
    def __init__(self,master,title,option,flag):
        
        self.flag = flag
        top=self.top = Toplevel(master)
        top.title(title)
        self.option = option;
        self.l=Label(top,text="Please Select").grid(row = 0)
        
        self.option_Value = IntVar()
        
        
        yes_button = Radiobutton(top, text="Yes", variable=self.option_Value, value=1)
        yes_button.grid(row=1)
        no_button = Radiobutton(top, text="No", variable=self.option_Value, value=0)
        no_button.grid(row=2)

        if flag == True:
            yes_button.select();
        else:
            no_button.select();

        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.grid(row =3)
        self.b2 = Button(top,text='Canceal',command=self.canceal)
        self.b2.grid(row=3,column=1)
        
        
    def cleanup(self):
        #self.value=self.e.get()
        self.value = self.option_Value.get();
        self.top.destroy()
        
    def canceal(self):
        self.value = None;
        self.top.destroy()