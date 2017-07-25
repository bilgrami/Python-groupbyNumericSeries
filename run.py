#!/usr/bin/env python 
import calc_groupby as grp_m
import sys 

if sys.version_info <= (3, 0):
    print ("Sorry, this program requires Python 3.x, not Python 2.x\n")
    sys.exit(1)
	
def __print_seperator(n):
	print ('-' * n);
	
def run_calc_total_group_count(list_l):
	try:
		#print input values 
		__print_seperator (40)
		print("Input - list: ", list_l);

		grp_o = grp_m.calc_groupby();
		total_group_count_i = grp_o.calc_total_group_count (list_l);

		print("Total Group count: ", total_group_count_i);
		return total_group_count_i;

	except Exception as error:	
		print("Error: ", error);
		
	finally:
		__print_seperator (40)

def run_calc_group_by(list_l, group_count_i):	
	try:
		#print input values 
		__print_seperator (40)
		print("Input - list: ", list_l);
		print("Input - Desired Group count: ", group_count_i);

		grp_o = grp_m.calc_groupby();
		g_d = grp_o.calc_group_by (list_l, group_count_i)
		
		print ("Group Result: ", g_d, "\n")
		return g_d;

	except Exception as error:	
		print("Error: ", error);
		
	finally:
		__print_seperator (40)


def run_calc_group_by_for_all_groups(list_l, total_group_count_i):	
	try:
		__print_seperator (50)
		for gc_i in range (1, total_group_count_i+1):
			run_calc_group_by(list_l, gc_i)

	except Exception as error:	
		print("Error: ", error);
		
	finally:
		__print_seperator (50)


if __name__ == "__main__":
	print ("Start ..")

	list_l = [1,2,4,3,6,38,33,89,86,87,99]
	run_calc_group_by(list_l, 4);
	
	#uncomment the following line to view all possible groups
	#total_group_count_i = run_calc_total_group_count(list_l);
	#run_calc_group_by_for_all_groups(list_l, total_group_count_i)

	list_l = [0,1,2,22,23,44,46,4,24]
	run_calc_group_by(list_l, 3)

	list_l = [1,2,4,3,6,38,33,89,86,87,99]
	total_group_count_i = run_calc_total_group_count(list_l);
	print ("total_group_count_i", total_group_count_i);

	#exception test
	list_l = [1,3]
	run_calc_group_by(list_l, 4)

	list_l = []
	run_calc_group_by(list_l, 4)

	print ("Finished!")
