from decimal import *
import Equations
import collections
import csv

class Inforlist(object):
    ## All variables should be in Decimal, now it is not Decimal right now.
    ## Variables ##
    def __init__(self):
        self.start_day = Decimal('0')
        self.end_day = Decimal('0')
        self.extend_flag = False;
        self.extend_days = Decimal('0')
        self.start_size = Decimal('0')
        self.end_size = Decimal('0')
        self.r = Decimal('0')

        ## dicts ##
        self.animal_price_dict = {};
        self.facility_cost_dict = {};
        self.feed_cost_dict = {};

    ## getters and setters ##
    def get_start_day(self):
        return self.start_day;

    def set_start_day(self, start):
        self.start_day = Decimal(start);
        self.update_start_size();
        
    def get_end_day(self):
        return self.end_day;
        
    def set_end_day(self, end):
        self.end_day = Decimal(end);
        self.update_end_size();
        
    def get_extend_flag(self):
        return self.extend_flag;
        
    def set_extend_flag(self,flag):
        if flag == 0:
            self.extend_flag = False
            self.extend_days = Decimal('0');
        else:
            self.extend_flag = True;

        
    def get_extend_days(self):
        return self.extend_days;
        
    def set_extend_days(self,extend):
        self.extend_days = Decimal(extend);
        #self.update_end_size();

    def update_start_size(self):
        self.start_size = Decimal(Equations.max_size_by_day(self.start_day));

    def get_start_size(self):
        return self.start_size;


    ## CAUTIOUS: WATCH OUT WHERE TO UPDATE THE MAX_SIZE IN DIFFERENT SITUATION
    def update_end_size(self):
        self.end_size = Decimal(Equations.max_size_by_day(self.end_day));

    def get_end_size(self):
        return self.end_size;

    def get_r(self):
        return self.r;
        
    def set_r(self,target_r):
        self.r = Decimal(target_r);
        
    ## dict getter setter ##
    def get_animal_price_dict(self):
        return self.animal_price_dict;
    
    
    ##_______CAUTIOUS________need to reimplement
    def set_animal_price_dict(self,price):
        self.animal_price_dict = {};
        key = self.end_size
        self.animal_price_dict[Decimal(key)] = Decimal(price)
        self.animal_price_dict = collections.OrderedDict(sorted(self.animal_price_dict.items()))
            
    def get_animal_price_of_size(self,size):
        '''
        if len(self.animal_price_dict) == 0 :
            throw excpetion
        '''
        
        for k,v in self.animal_price_dict.items():
            if(size <= k):
                return v
        '''
        throw exception
        '''
        
        '''
        ## second method
        length = len(self.animal_price_dict)
        if length == 0:
            throw exception
        
        value = self.animal_price_dict.values()[0]
        for i in range(0,length-1):
            current_key = self.animal_price_dict.keys()[i]
            next_key = self.animal_price_dict.keys()[i+1]
            if(size <= current_key):
                return self.animal_price_dict.values()[i]
        return value
        '''

    def set_animal_price_dit_by_csv(self,file_path):
        self.animal_price_dict = {};
        with open(file_path, 'r') as csvfile:
            spamreader = csv.reader(csvfile.read().splitlines())
            for day,size in spamreader:
                self.animal_price_dict[Decimal(day)] = Decimal(size);
                #print day,size
                #print file_path;
        self.animal_price_dict = collections.OrderedDict(sorted(self.animal_price_dict.items()))
        
   

    def get_facility_cost_dict(self):
        #self.facility_cost_dict = collections.OrderedDict(sorted(self.facility_cost_dict.items()))
        return self.facility_cost_dict;
        
    def set_facility_cost_dict(self,price):
        self.facility_cost_dict = {};
        for i in range(self.start_day, self.end_day + self.extend_days + 1):
            self.facility_cost_dict[Decimal(i)] = Decimal(price);
        self.facility_cost_dict = collections.OrderedDict(sorted(self.facility_cost_dict.items()))
        
    def set_facility_cost_dict_by_csv(self,file_path):
        self.facility_cost_dict = {};
        with open(file_path, 'r') as csvfile:
            spamreader = csv.reader(csvfile.read().splitlines())
            for day,size in spamreader:
                self.facility_cost_dict[Decimal(day)] = Decimal(size);
                #print day,size
                #print file_path;
        self.facility_cost_dict = collections.OrderedDict(sorted(self.facility_cost_dict.items()))    
    
    def get_feed_cost_dict(self):
        return self.feed_cost_dict;
        
    def set_feed_cost_dict(self, price):
        self.feed_cost_dict = {};
        for i in range(self.start_day, self.end_day + self.extend_days + 1):
            self.feed_cost_dict[Decimal(i)] = Decimal(price);
        self.feed_cost_dict = collections.OrderedDict(sorted(self.feed_cost_dict.items()))

    def set_feed_cost_dict_by_csv(self,file_path):
        self.feed_cost_dict = {};
        with open(file_path, 'r') as csvfile:
            spamreader = csv.reader(csvfile.read().splitlines())
            for day,size in spamreader:
                self.feed_cost_dict[Decimal(day)] = Decimal(size);
                #print day,size
                #print file_path;
        self.feed_cost_dict = collections.OrderedDict(sorted(self.feed_cost_dict.items()))    
 

    ########################






