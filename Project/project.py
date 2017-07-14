import random as rn
from tabulate import tabulate

def arrival_table():
	arriv = [i for i in range(4,9)]
	return rn.choice(arriv) 

def clerk_table():
	start = [i for i in range(8,13)]
	return rn.choice(start)

def cashier_table():
	start = [i for i in range(5,8)]
	return rn.choice(start)
	
def choose_clerk_random():
	lis = [0,1]
	return rn.choice(lis)
	
if (__name__=="__main__"):
	student_count = 0
	student_arr = 0
	curr_arr_time = 0
	
	table = []
	
	service_start_a = 0
	service_start_b = 0
	
	service_end_a = 0
	service_end_b = 0
	
	service_start_cash = 0
	service_end_cash = 0
	service_time_cash = 0
	
	service_time_a = 0
	service_time_b = 0
	
	#idle_time_clerk = 0
	#idle_time_cashier = 0
	
	queue_time_clerk = 0
	queue_time_cash = 0
	
	util_clerk_a = 0
	util_clerk_b = 0
	
	util_cash = 0
	
	process_time = 0
	
	head = ["student#","student_arr","curr_arr_time","clerk1_service_begin","clerk1_service","clerk1_service_end","clerk2_service_begin","clerk2_service","clerk2_serivce_end","cashier_service_begin","cashier_service","cashier_service_end","queue_time_clerk", "queue_time_cash"]
	
	#i = curr_arr_time
	while curr_arr_time <= 6000 and max(service_end_a,service_end_b) <=6000 :
		student_count+=1
		curr_arr_time +=student_arr
		
		if(service_end_a < service_end_b):
			service_start_a = max(service_end_a, curr_arr_time)
			service_time_a = clerk_table()
			util_clerk_a += service_time_a
			service_end_a = service_start_a + service_time_a
			queue_time_clerk = (service_start_a - curr_arr_time)
			
			if(queue_time_clerk<0):
				queue_time_clerk = 0
			
			service_start_cash = max(service_end_cash, service_end_a)
			service_time_cash = cashier_table()
			util_cash += service_time_cash
			service_end_cash = service_time_cash + service_start_cash
			
			process_time += (service_time_a+service_time_cash)
			
			queue_time_cash = service_start_cash - service_end_a
				
			if(queue_time_cash<0):
				queue_time_cash = 0
				
			table.append([student_count, student_arr, curr_arr_time,service_start_a,service_time_a,service_end_a,'-','-','-',service_start_cash, service_time_cash, service_end_cash,queue_time_clerk,queue_time_cash])
			
		elif(service_end_b<service_end_a):
			service_start_b = max(service_end_b, curr_arr_time)
			service_time_b = clerk_table()
			util_clerk_b += service_time_b
			service_end_b = service_start_b + service_time_b
			queue_time_clerk = (service_start_b - curr_arr_time)
			
			if(queue_time_clerk<0):
				queue_time_clerk = 0
			
			service_start_cash = max(service_end_cash, service_end_b)
			service_time_cash = cashier_table()
			util_cash += service_time_cash
			service_end_cash = service_time_cash + service_start_cash
			
			queue_time_cash = service_start_cash - service_end_b
			process_time += (service_time_b+service_time_cash)	
			if(queue_time_cash<0):
				queue_time_cash = 0
				
			table.append([student_count, student_arr, curr_arr_time,'-','-','-',service_start_b,service_time_b,service_end_b,service_start_cash, service_time_cash, service_end_cash,queue_time_clerk,queue_time_cash])
		
		elif(service_end_a==service_end_b):
			n = choose_clerk_random()
			
			if(n == 0):
				service_start_a = max(service_end_a, curr_arr_time)
				service_time_a = clerk_table()
				util_clerk_a += service_time_a
				service_end_a = service_start_a + service_time_a
				queue_time_clerk = (service_start_a - curr_arr_time)
			
				if(queue_time_clerk<0):
					queue_time_clerk = 0
				
				service_start_cash = max(service_end_cash, service_end_a)
				service_time_cash = cashier_table()
				util_cash += service_time_cash
				
				service_end_cash = service_time_cash + service_start_cash
				
				queue_time_cash = service_start_cash - service_end_a
				process_time += (service_time_a+service_time_cash)
				if(queue_time_cash<0):
					queue_time_cash = 0
				
				table.append([student_count, student_arr, curr_arr_time,service_start_a,service_time_a,service_end_a,'-','-','-',service_start_cash, service_time_cash, service_end_cash,queue_time_clerk,queue_time_cash])
			
			else:
				service_start_b = max(service_end_b, curr_arr_time)
				service_time_b = clerk_table()
				util_clerk_b += service_time_b
				
				service_end_b = service_start_b + service_time_b
				queue_time_clerk = (service_start_b - curr_arr_time)
			
				if(queue_time_clerk<0):
					queue_time_clerk = 0
				service_start_cash = max(service_end_cash, service_end_b)
				service_time_cash = cashier_table()
				util_cash += service_time_cash
				service_end_cash = service_time_cash + service_start_cash
				
				queue_time_cash = service_start_cash - service_end_b
				process_time += (service_time_b+service_time_cash)
				if(queue_time_cash<0):
					queue_time_cash = 0
					
				table.append([student_count, student_arr, curr_arr_time,'-','-','-',service_start_b,service_time_b,service_end_b,service_start_cash, service_time_cash, service_end_cash,queue_time_clerk, queue_time_cash])
		
		
		student_arr = arrival_table()
		
	print(tabulate(table,headers = head))
	f = open("util.txt","w")
	d = {}
	ma = max(service_end_a, service_end_b)
	
	util_c_a = (util_clerk_a/6000)*100
	util_c_b = (util_clerk_b/6000)*100
	
	util_ca = (util_cash/service_end_cash)*100
	total_service_time = process_time/student_count
	lis = ["Utilization of clerk a:","Utilization of clerk b:","Utilization of cashier:","Average Service Time:"]
	d["Utilization of clerk a:"] = util_c_a
	d["Utilization of clerk b:"] = util_c_b
	d["Utilization of cashier:"] = util_ca
	d["Average Service Time:"] = total_service_time
	
	for i in lis:
		if(lis.index(i) != len(lis)-1):
			f.write(i+"\t"+"{0:.2f}".format(d[i])+"%\n")
		else:
			f.write(i+"\t"+"{0:.2f}".format(d[i]))
		
	f.close()