import csv
from Graph import *
from Equations import *


import matplotlib as mpl
#from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np




def printInfoList(infoList):
    fp = open("infolist.txt", "w");
    fp.write("INFORMATION\n");
    line = 'START DAY'+','+str(infoList.get_start_day())+'\n';
    fp.write(line);
    line = 'END DAY'+','+str(infoList.get_end_day())+'\n';
    fp.write(line);
    line = 'EXTEND PERIOD'+','+str(infoList.get_extend_days())+'\n';
    fp.write(line);
    line = 'START SIZE'+','+str(infoList.get_start_size())+'\n';
    fp.write(line);
    line = 'END SIZE'+','+str(infoList.get_end_size())+'\n';
    fp.write(line);
    line = 'R VALUE'+','+str(infoList.get_r())+'\n';
    fp.write(line);
    #print 'finished'
    fp.close();
    
def printDict(title,dict_name):
    file_name = title+'.csv'
    writer = csv.writer(open(file_name, 'wb'), delimiter=',')
    for key, value in dict_name.items():
       writer.writerow([str(key), str(value)])
       
       
def main(infoList):
    
    start_day = infoList.get_start_day()
    end_day = infoList.get_end_day()
    extend_flag = infoList.get_extend_flag()
    extend_days = infoList.get_extend_days()
    start_size = infoList.get_start_size()
    end_size = infoList.get_end_size()
    r = infoList.get_r()
    animal_price_dict = infoList.get_animal_price_dict()
    facility_cost_dict = infoList.get_facility_cost_dict()
    feed_cost_dict = infoList.get_feed_cost_dict()
    
    g = Graph(infoList)
    max_array = build_max_size_array(start_day, end_day)
    #for key,value in max_array.items():
       # print str(key)+','+str(value)
    if(extend_days!=0):
        temp={}
        for i in range(end_day+1,end_day+extend_days+1):
            temp[Decimal(i)]=Decimal(end_size)
            ####Cautious::have to check whether it is ordered
        max_array.update(temp)
    
    
    #Extend
    day_list = range(start_day,end_day+extend_days+1)
    day_list = np.array(day_list)
    day_len = len(day_list)
    size_list = np.arange(float(start_size),float(end_size+Decimal(0.1)),0.1)
    size_len = len(size_list)

    day_list, size_list = np.meshgrid(day_list, size_list)
    
    q_list = [[0]*day_len for i in range(size_len)]
    
    print str(day_len) + '   '+str(size_len)


        
    
    for today in range(start_day, end_day+extend_days):
        if(today<=end_day):
            max_size = max_size_by_day(today)
        else:
            max_size = end_size
        size = start_size
        
        x_cor = int(today-start_day)
       # print 'size is ' + str(size) + 'max_size is ' + str(max_size)
        
        while size <= max_size:
            
            max_size_tmrw = size_by_size_max_feeding(size, max_array)
            num_size = (max_size_tmrw - size)/Decimal('0.1')
            
            temp_day = day_by_size_max_feeding(size,max_array);
            day_diff = today - day_by_size_max_feeding(size,max_array);
            if(day_diff<0):
                print 'error'+str(temp_day)

            min_feed = feeding_rate(day_diff, size)
            max_feed = max_feeding_rate(size)

            if (num_size == Decimal(0)):
                v_start = (today, size.quantize(ONEPLACES))     ## Day||Size
                v_end = ((today+Decimal(1)), size.quantize(ONEPLACES));
                e_rate = min_feed;
                g.add_edge(v_start, v_end, e_rate);
                y_cor  = int(0)
                #print 'X_cor ' + str(x_cor) + ' Y_cor ' + str(y_cor)
                q_list[y_cor][x_cor] = float(e_rate)                
            else:
                each_size_feed = (max_feed - min_feed)/(num_size);

                for i in range(Decimal(0), num_size+Decimal(1)):
                    v_start = (today, size.quantize(ONEPLACES));     ## Day||Size
                    v_end = ((today+Decimal(1)), (size + Decimal(i)*Decimal('0.1')).quantize(ONEPLACES));
                    e_rate = min_feed + Decimal(i)*each_size_feed;
                    g.add_edge(v_start, v_end, e_rate);
                    
                    y_cor = int(((size + Decimal(i)*Decimal('0.1')).quantize(ONEPLACES)-start_size.quantize(ONEPLACES))*10)
                    #print 'X_cor ' + str(x_cor) + ' Y_cor ' + str(y_cor)
                    q_list[y_cor][x_cor] = float(e_rate)
                      
            size = size + Decimal('0.1');
        print "finished building the graph g on day: " + str(today); 
            
    g.print_nodes_by_day(end_day);
    print "print node finished"    
    g.print_nodes();
    print "print all nodes finished"
    

    fig = plt.figure()
    #ax = fig.gca(projection='3d')
    ax = Axes3D(fig)
    surf = ax.plot_surface(day_list, size_list, q_list, rstride=1, cstride=1, cmap=cm.coolwarm,
            linewidth=0, antialiased=False)
    ax.set_zlim(-1, end_size+1);

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    mpl.rcParams['legend.fontsize'] = 10
    
    plt.show()
    print "all done"
    
    