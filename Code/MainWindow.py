from Tkinter import *
from inputWindow import *
from optionWindow import *
from priceWindow import *
from displayWindow import *
from Variables import *
from RunSimulation import *

MODIFY_BUTTON_LABEL = "Modify";
NAME_LABEL_LIST = [  "Start Day", "End Day",
                     "Extend Option", "Extend Days",
                     "Start Size", "End Size",
                     "Animal Price", "Food Cost",
                     "Facility Cost", "R value"  ];
NAME_LABEL_LIST_SIZE = len(NAME_LABEL_LIST);

def findVariableSetterByOption(infoList,option) :
    if option == 0:
        return (infoList.set_start_day)
    elif option == 1:
        return (infoList.set_end_day)
    elif option == 2:
        return (infoList.set_extend_flag)
    elif option == 3:
        return (infoList.set_extend_days)
    elif option == 6:
        return (infoList.set_animal_price_dict)
    elif option == 7:
        return (infoList.set_feed_cost_dict)
    elif option == 8:
        return (infoList.set_facility_cost_dict)
    elif option == 9:
        return (infoList.set_r)
        
def findVariableGetterByOption(infoList,option) :
    if option == 0:
        return (infoList.get_start_day)
    elif option == 1:
        return (infoList.get_end_day)
    elif option == 3:
        return (infoList.get_extend_days)
    elif option == 9:
        return (infoList.get_r)


class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.master.title("Optimal Feeding")
        self.infoList = Inforlist()
        self.label_list = [];
        self.value_list = [];
        self.valueVar_list = [];
        self.button_list = [];
        
        i = 0;
        for name_label in NAME_LABEL_LIST:
            self.label_list.append(Label(self.master, text = name_label));
            self.label_list[i].grid(row = i);
            i += 1;
        
        for i in range(0,NAME_LABEL_LIST_SIZE):
            tempVar = StringVar();
            tempVar.set('0');
            self.valueVar_list.append(tempVar);
            if i==2:
                if self.infoList.get_extend_flag()==False:
                    self.valueVar_list[i].set('No')
                else:
                    self.valueVar_list[i].set('Yes')
            if i>=6 and i <=8:
                Button(self.master, text='Show Detail',command = lambda title=NAME_LABEL_LIST[i]: self.showDetail(title)).grid(row=i, column=1)
                self.value_list.append(None)
            else:
                self.value_list.append(Label(self.master, textvariable=self.valueVar_list[i]));
                self.value_list[i].grid(row=i, column=1)
            if i==4 or i==5:
                self.button_list.append(None)
            else:
                tempButton = Button(self.master, text= MODIFY_BUTTON_LABEL, command = lambda title=NAME_LABEL_LIST[i]: self.popup(title))
                self.button_list.append(tempButton)
                self.button_list[i].grid(row=i,column=3)
                if i == 3:
                    self.button_list[3].config(state=DISABLED)
                    
        run_button = Button(self.master, text='RUN SIMULATION',command=self.start)
        run_button.grid(row = 10)


    def showDetail(self,title):
        option = NAME_LABEL_LIST.index(title);
        if option == 6:
            self.w = displayWindow(self.master,title,option,self.infoList.get_animal_price_dict())
        elif option ==7:
            self.w = displayWindow(self.master,title,option,self.infoList.get_feed_cost_dict())
        elif option ==8:
            self.w = displayWindow(self.master,title,option,self.infoList.get_facility_cost_dict())
        self.master.wait_window(self.w.top)

    def popup(self,title):
        option = NAME_LABEL_LIST.index(title);
        if option==2:
            flag = self.infoList.get_extend_flag();
            self.w = optionWindow(self.master,title,option,flag)
            #print 'optionWindow'
        elif option ==6 or option == 7 or option== 8:
            
            ##------CAUTIOUS HERE:____
            if option == 6:
                function = self.infoList.set_animal_price_dit_by_csv
            elif option == 7:
                function = self.infoList.set_feed_cost_dict_by_csv
            else:
                function = self.infoList.set_facility_cost_dict_by_csv
            self.w = priceWindow(self.master,title,option,function)
        
        else:
            self.w=inputWindow(self.master,title,option)
        #print option;
        self.master.wait_window(self.w.top)
        if(self.w.value != None):
 
            (findVariableSetterByOption(self.infoList,option))(self.w.value)
            getter_function = findVariableGetterByOption(self.infoList,option)
            if(option in {0,1,3,9}):
                self.valueVar_list[option].set(getter_function())
            if option == 0 :
                self.valueVar_list[4].set(self.infoList.get_start_size())
            if option == 1:
                self.valueVar_list[5].set(self.infoList.get_end_size())
            if option == 2:
                if self.w.value == 1:
                    self.valueVar_list[2].set('Yes')
                    self.button_list[3].config(state=ACTIVE)
                else:
                    self.valueVar_list[2].set('No')
                    self.button_list[3].config(state=DISABLED)
                self.valueVar_list[3].set(self.infoList.get_extend_days())
        
    def start(self):
        printInfoList(self.infoList)
        printDict('Animal Price',self.infoList.get_animal_price_dict())
        printDict('Food Cost',self.infoList.get_feed_cost_dict())
        printDict('Facility Cost',self.infoList.get_facility_cost_dict())
        main(self.infoList)

