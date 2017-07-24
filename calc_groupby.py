#!/usr/bin/env python 
"""
Problem Statement: 
Classify a numeric series in groups. 
Do not use any machine learning algorithm. 

For example: Provide the following numeric series
    list = [1,2,4,3,6,38,33,89,86,87,99]

After calling GroupBy(list), produces following groups 
    Group A: 1,2,3,4,6
    Group B: 33,38
    Group C: 86,87,89
    Group D: 99
       """
import numpy as np
list = [1,2,4,3,6,38,33,89,86,87,99];
print("Input list", list);

#sort the array
a = np.array(list);
sorted_a = np.sort(a);

currentNextPair_a = [
		(current, sorted_a[idx+1] if idx < len(sorted_a)-1 else None)
		for idx,current in enumerate(sorted_a)
		];
#calculate diff K for each pair
data_a =    np.array (
		[
			(current, 
			 next_item if next_item is not None else current, 
			 next_item - current if next_item is not None else 0, 
			 "")
		for current, next_item in currentNextPair_a],
		dtype=[
			('current_item',np.int32),
			('next_item',np.int32),
			('diff_k',np.int32),
			('group_name','S1')
			 ]
		)
	
#calculate unique diff K
diff_k_a = np.array([(diff_k) for current_item, next_item, diff_k, group_name in data_a])
unique_k_a = np.unique([x for x in diff_k_a if x > 0])
print ("unique_k_a", unique_k_a)

#pick a suitable k, we will just pick a median value from unique array of k's, where k>0
median_k = np.median(np.sort(unique_k_a))
print ("median_k", median_k)

#find group 
groups = [chr(i) for i in range(ord('a'),ord('z')+1)]
#print (groups)
k = median_k
i = 0
rowid = 0
current_group_name = groups[i]
print ("c", "n", "k", "group")

for current_item, next_item, diff_k, group_name in data_a:
	if diff_k < k:
		group_name = current_group_name
	else:
		i+=1
		current_group_name = groups[i]
		group_name = current_group_name

	print(current_item, next_item, diff_k,group_name);
