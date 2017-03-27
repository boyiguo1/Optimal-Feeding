from decimal import *;
import Variables;
from Equations import max_size_by_day;

    
def build_max_size_array():
    start_day = Variables.get_start_day();
    end_day = Variables.get_end_day();
    max_size_array = {};
    
    for today in range(start_day, end_day + 1):
        max_size_array[Decimal(today)] = max_size_by_day(Decimal(today))
    
    return max_size_array

max_size_array = build_max_size_array();    
    
##need to check the correctness of the logic
def day_by_size_max_feeding(size):
    for today in max_size_array:
        if(max_size_array[today]>= size and
           today <= end_day):
               return today;
    return -1;



##input size and get the size by max feeding
def size_by_size_max_feeding(size, max_size_array):
    size = Decimal(size);
    ##getcontext().prec = 6;
    for today in max_size_array:
        if (max_size_array[today] >= size and today <= (end_day)):
            ## finding the slope of current day ##
            tempint = (max_size_array[(today+Decimal(1))] - max_size_array[(today)]);
            
            return (size + tempint).quantize(ONEPLACES)
    
    return -1