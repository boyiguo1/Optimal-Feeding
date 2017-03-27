from decimal import *
from Equations import *

MAX_INT = Decimal(999999)

class Graph(object):
    
    def __init__(self,infoList):
        self.infoList = infoList
        self.root = None
        self.nodes = {}
        self.edges = {}
        self.start_day = infoList.get_start_day()
        self.end_day = infoList.get_end_day()
        self.end_size = infoList.get_end_size()
        self.extend_days = infoList.get_extend_days()
        self.discount = infoList.get_r()/Decimal('365')     
        self.animal_price = infoList.get_animal_price_of_size
        self.feed_cost_dict = infoList.get_feed_cost_dict()
        self.max_array = build_max_size_array(self.start_day, self.end_day)
        cost_array = infoList.get_facility_cost_dict()
        self.facility_cost_array = build_facililty_array(cost_array, self.discount, self.start_day, self.end_day+self.extend_days)
    
    def add_node(self, value):   
        #self.nodes[value] = {"feeding":MAX_INT, "previous":None, "profit":Decimal(-1)};
        self.nodes[value] = {"feeding":Decimal(999999), "previous":None, "profit":Decimal(-1), "amount":Decimal(0)}
        if(len(self.nodes) == 1):
            self.root = (value, {"feeding":Decimal(0), "previous":"root", "profit":Decimal(-1),"amount":Decimal(0)})
            self.nodes[value] = {"feeding":Decimal(0), "previous":"root", "profit":Decimal(-1),"amount":Decimal(0)};
    
    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance);
        self._add_feeding(from_node, to_node, distance);
        
    def _add_feeding(self, from_node, to_node, distance):
        date_diff = (from_node[0]) - self.start_day;
        feeding_today = distance * discount_factor_value(date_diff, self.discount)
        from_feeding = self.nodes[from_node]["feeding"] + feeding_today;
        to_feeding = self.nodes[to_node]["feeding"];
        if(to_feeding > from_feeding and self.nodes[from_node]["previous"] != None):
            self.nodes[to_node]["feeding"] = from_feeding;
            self.nodes[to_node]["previous"] = from_node;
            self.nodes[to_node]["amount"] = distance;
            ##______CAUTIOUS________NOT IMPLETMENT YET
            sell_price = self.animal_price(to_node[1])
            #______CAUTIOUS_____ERROR HERE
            #rent_cost = self.facility_cost_array[to_node[0]]
            rent_cost = Decimal('0')
            feeding_cost = self.feed_cost_dict[to_node[0]] * from_feeding;
            profit = get_revenue(self.start_day, self.discount, sell_price, to_node[0], to_node[1], from_feeding) - rent_cost - feeding_cost
            '''if(to_node[0] >= self.end_day):
                #print 'to node is '+ str(to_node[0]) + ' end_day '+str(self.end_day )
                size = to_node[1]
                Ta = day_by_size_max_feeding(size,self.max_array)
                print 'ta is ' + str(Ta) + ' to_nodeis ' + str(to_node[0])
                oc = opportunity_cost(sell_price, size, Ta+300, sell_price, size, to_node[0]+300, self.discount);
                profit = profit - oc;
                print 'OC is '+str(oc)
            '''
            self.nodes[to_node]["profit"] = profit
        
 
    def _add_edge(self, from_node, to_node, distance):
        date_diff = (from_node[0]) - self.start_day;
        if(from_node not in self.nodes):
            self.add_node(from_node)
        if(to_node not in self.nodes):
            self.add_node(to_node)
        self.edges[(from_node, to_node)] = distance * discount_factor_value(date_diff, self.discount)


    def print_nodes(self):
        fp = open("nodes.txt", "wb");
        fp.write("FORMAT: day, size, feeding_cost, profit, amount, previous_node.\n");
        for n in self.nodes:
            if(self.nodes[n]["previous"] != "root" and self.nodes[n]["previous"] != None):
                day = n[0];
                size = n[1];
                feeding_price = self.feed_cost_dict[day]
                oc = 0
                if(day > self.end_day):
                    Pa = self.infoList.get_animal_price_of_size(self.end_size);
                    Pl = self.infoList.get_animal_price_of_size(size)
                    oc = opportunity_cost(Pa, self.end_size, self.end_day, Pl, size, day, self.discount)
                profit = self.nodes[n]["profit"] - oc
                result = str(day) + ", " + str(size) + ", " + str(feeding_price * self.nodes[n]["feeding"]) + ", " + str(profit)+ ", " + str(self.nodes[n]["amount"])+ ", " + str(self.nodes[n]["previous"][0])+", " + str(self.nodes[n]["previous"][1]) + "\n";
                fp.write(result);
        print "finished nodes";
        fp.close();

    def print_nodes_by_day(self, day):
        fp = open("node_at_" + str(day), "wb");
        fp.write("FORMAT: day, size, feeding_cost, profit, amount, OC,previous_node.\n");
        for n in self.nodes:
            if(self.nodes[n]["previous"] != "root" and self.nodes[n]["previous"] != None and n[0] == day):
                day = n[0];
                size = n[1];
                feeding_price = self.feed_cost_dict[day]
                oc = 0
                if(day > self.end_day):
                    Pa = self.infoList.get_animal_price_of_size(self.end_size);
                    Pl = self.infoList.get_animal_price_of_size(size)
                    oc = opportunity_cost(Pa, self.end_size, self.end_day, Pl, size, day, self.discount)
                profit = self.nodes[n]["profit"] - oc
                result = str(day) + ", " + str(size) + ", " + str(feeding_price * self.nodes[n]["feeding"]) + ", " + str(profit) + ", " + str(self.nodes[n]["amount"])+ ", "+ str(self.nodes[n]["previous"][0])+", " + str(self.nodes[n]["previous"][1]) + "\n";
                fp.write(result);
        print "finished nodes";
        fp.close();

