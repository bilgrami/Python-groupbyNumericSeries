#!/usr/bin/env python 
import calc_groupby as grp_m

def run_calc_total_group_count(list_l):
		grp_o = grp_m.calc_groupby();
		total_group_count_i = grp_o.calc_total_group_count (list_l);
		return total_group_count_i;

def run_calc_group_by(list_l, total_group_count_i):	
	try:
		#print input values 
		print("Input - list: ", list_l);
		
		grp_o = grp_m.calc_groupby();

		for gc_i in range (1, total_group_count_i):
			print("\nDesired Group count: ", gc_i);
			g = grp_o.calc_group_by (list_l, gc_i)
			print ("Group Result: ", g, "\n")

	except Exception as error:	
		print("Error: ", error);

if __name__ == "__main__":
	print ("Start ..")

	list_l = [1,2,4,3,6,38,33,89,86,87,99]
	total_group_count_i = run_calc_total_group_count(list_l);
	run_calc_group_by(list_l, total_group_count_i)

	#exception test
	#list_l = [1,3]
	#run_calc_group_by(list_l, 4)

	#list_l = []
	#run_calc_group_by(list_l, 4)

	print ("Finished!")
