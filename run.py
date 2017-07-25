#!/usr/bin/env python 
import calc_groupby as grp_m
import sys 

if sys.version_info <= (3, 0):
    print ("Sorry, this program requires Python 3.x, not Python 2.x\n")
    sys.exit(1)
	
def __print_fancy_message (message, dashcount):
	print ("\n", '-' * int(dashcount/2) , message, '-' * int (dashcount/2));


def run_calc_total_group_count(list_l):
	try:
		#print input values 
		print("Input - list: ", list_l);

		grp_o = grp_m.calc_groupby();
		total_group_count_i = grp_o.calc_total_group_count (list_l);

		print("Total Group count: ", total_group_count_i);
		return total_group_count_i;

	except Exception as error:	
		print("Error: ", error);

def run_calc_group_by(list_l, group_count_i):	
	try:
		#print input values 
		print("Input - list: ", list_l);
		print("Input - Desired Group count: ", group_count_i);

		grp_o = grp_m.calc_groupby();
		g_d = grp_o.calc_group_by (list_l, group_count_i)
		
		print ("Group Result: ", g_d)
		return g_d;

	except Exception as error:	
		print("Error: ", error);


def run_calc_group_by_for_all_groups(list_l, total_group_count_i):	
	try:
		for gc_i in range (1, total_group_count_i+1):
			run_calc_group_by(list_l, gc_i)

	except Exception as error:	
		print("Error: ", error);


if __name__ == "__main__":
	__print_fancy_message (" ** Welcome to Calc Group by Demo ** ", 60)

	__print_fancy_message ("-- Scenario 0 -- ", 60)
	my_l = []
	gc_i = 44 # I want 44 groups
	my_d = run_calc_group_by (my_l, gc_i)
	print("")

	my_l = [1]
	gc_i = 44 # I want 44 groups
	my_d = run_calc_group_by (my_l, gc_i)

	__print_fancy_message ("-- Scenario 1 -- ", 60)
	my_l = [0,1]
	gc_i = 1 # I want 1 group
	my_d = run_calc_group_by (my_l, gc_i)

	__print_fancy_message ("-- Scenario 2 -- ", 60)
	my_l = [0,1]
	gc_i = 2 # I want 2 group
	my_d = run_calc_group_by (my_l, gc_i)

	__print_fancy_message ("-- Scenario 3 -- ", 60)
	my_l = [0,1,2,22,23,44,46,4,24]
	gc_i = 3 # I want 3 group
	my_d = run_calc_group_by (my_l, gc_i)

	__print_fancy_message ("-- Scenario 4 -- ", 60)
	my_l = [1,2,4,3,6,38,33,89,86,87,99]
	gc_i = 4 # I want 4 group
	my_d = run_calc_group_by (my_l, gc_i)
	
	#uncomment the following line to view all possible groups
	#total_group_count_i = run_calc_total_group_count(list_l);
	#run_calc_group_by_for_all_groups(my_l, total_group_count_i)
	__print_fancy_message (" ** Finished successfully ** ", 60)
