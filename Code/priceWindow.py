from Tkinter import *
from inputWindow import *
from decimal import *
import tkFileDialog
import csv
import collections

class priceWindow(object):
    def __init__(self,master,title,option,function):
        self.master = master
        self.function = function;
        top=self.top=Toplevel(master)
        top.title(title);
        self.option = option;
        self.l=Label(top,text="Please Type In The Value").grid(row = 0)
        #self.l.pack()
        #self.e.pack()
        self.b=Button(top,text='Type In',command=lambda:self.type(title))
        self.b.grid(row =2)
        self.b2 = Button(top,text='Import File',command=lambda:self.importFile(function))
        self.b2.grid(row=2,column=1)
        
        
    def type(self,title):
        self.w = inputWindow(self.master,title,self.option)
        self.master.wait_window(self.w.top)
        self.value = self.w.value;
        if self.w.value != None:
            self.value = self.w.value;
        self.top.destroy()
        
    def importFile(self,function):
        file_path = tkFileDialog.askopenfilename()
        function(file_path)
        '''
        with open(file_path, 'r') as csvfile:
            spamreader = csv.reader(csvfile.read().splitlines())
            for day,size in spamreader:
                self.dict[day] = size;
                #print day,size
        '''
        self.value = None;
        self.top.destroy()