import numpy as np
import sys 

if sys.version_info <= (3, 0):
    print ("Sorry, this program requires Python 3.x, not Python 2.x\n")
    sys.exit(1)

"""
Problem Statement: 
Classify a numeric series in groups.

Use case 1: Classify a natural number series in discrete groups.
calc_groupby(list_l, gc_i) 
	In:
		list_l = [1,2,4,3,6,38,33,89,86,87,99]
		gc_i = 4 #Desired group count 
		my_d = calc_groupby (list_l, gc_i) 
	Out:
		{
			0: 1,2,3,4,6
			1: 33,38
			2: 86,87,89
			3: 99
		}	

Use case 2: Get total possible groups for a natural number series
calc_total_group_count (list_l)
	In:
		list_l = [1,2,4,3,6,38,33,89,86,87,99]
		total_gc_i = calc_total_group_count(list_l)
	Out:
		7
"""

class calc_groupby:
	self = None;


# start: private methods 
	def __get_sorted_pair (self, list_l):
		""" Return a sorted numpy array of nx2 dimensions

		Parameters
		----------
		arg1: list 
			A list of natural numbers with at least 1 element

		Returns
		-------
		array( [ [number1, number2] ] )
		[(first element, next element), (next element, element after next ), ..., (last element, None)]
			
		Example 1: 
		-------
		__get_sorted_pair ([4,3,2,1,2]) 
		array([ [1,2],[2,2],[2,3],[3,4],[4,None] ])

		Example 2: 
		-------
		__get_sorted_pair ([]) 
		None
		"""

		try:
			#convert list to a numpy array
			a = np.array(list_l);

			#sort array
			sorted_list_a = np.sort(a);

			#get series of next elements, return None for the element last 
			sorted_next_a = np.array([
					(sorted_list_a[idx+1] if idx < len(sorted_list_a)-1 else None)
					for idx,current in enumerate(sorted_list_a)
					]);

			#combine array of current and next elements, and return the result
			sorted_pair_a = np.column_stack((sorted_list_a, sorted_next_a));
			return sorted_pair_a;

		except ValueError:
			return None


	def __get_diff_between_pairs (self, sorted_pair_a): 
		try:
			current_a = sorted_pair_a[:, 0];#slice to get all current elements
			next_a = sorted_pair_a[:, 1];#slice to get all next elements
			
			if next_a[-1] is None and current_a[-1] is not None:
				next_a[-1] = current_a[-1]; 

			diff_a = next_a - current_a;
			return diff_a;

		except ValueError:
			return None


	def __get_groups (self, sorted_pair_a): 
		try:
			diff_a = self.__get_diff_between_pairs(sorted_pair_a);
			groups_a = np.unique(diff_a);
			return groups_a, diff_a;

		except ValueError:
			return None


	def __addResultItem (self, dict_d, key, valueToAdd):
		try:
			if key in dict_d:
				list_l = dict_d[key];
				if list_l is None or len(list_l) == 0:
					list_l = [];
			else:
				list_l = [];

			if valueToAdd not in list_l:
				list_l.extend([valueToAdd]);

			dict_d[key] = list_l
			return dict_d;

		except ValueError:
			return None
# end: private methods 


# start: public methods 
	def calc_total_group_count (self, list_l): 
		""" Return total number of possible groups a list of natural numbers can be divided into

		Parameters
		----------
		arg1: list 
			A list of natural numbers with at least 1 element

		Returns
		-------
		int
		Total number of possible groups the list can be divided into

		Raises
		-------
		FunctionInputError
			When list_l is empty

		Example 1: 
		-------
		>>> t.calc_total_group_count ([1,2,4,3,6,38,33,89,86,87,99]) 
		7

		Example 2: Invalid List
		-------
		>>> t.calc_total_group_count ([]) 
		Traceback (most recent call last):
			raise FunctionInputError ("Parameter [list] must be a valid natural number list with 1 or more elements", list_l)
		FunctionInputError: ('Parameter [list] must be a valid natural number list with 1 or more elements', [])

		"""
		try:
			#start: parameter validation check
			if len(list_l) < 1:
				raise FunctionInputError ("Parameter [list] must be a valid natural number list with 1 or more elements", list_l)

			#end: parameter validation check

			sorted_pair_a = self.__get_sorted_pair (list_l);
			groups_a, diff_a = self.__get_groups (sorted_pair_a);
			return len(groups_a);

		except (FunctionInputError, ValueError) as error:
			raise;


	def calc_group_by (self, list_l, groupcount_i):
		""" Return a dictionary containing group of numbers of a series

		Parameters
		----------
		arg1: list 
			A list of natural numbers with at least 1 element

		arg2: int
			Desired number of groups to split the list into. It should be <= number of elements in the list

		Returns
		-------
		dict { group_id, [series of numbers belonging to the group] }

		Raises
		-------
		FunctionInputError
			When list_l is empty
			or
			When groupcount_i (Desired Group count) is larger than number of elements in the list_l
			
		Example 1: 
		-------
		>>> t.calc_group_by ([1,2,4,3,6,38,33,89,86,87,99], 4) 
		{0: [1, 2, 3, 4, 6], 1: [33, 38], 2: [86, 87, 89], 3: [99]}

		Example 2: Invalid List
		-------
		>>> t.calc_group_by ([], 4) 
		Traceback (most recent call last):
			raise FunctionInputError ("Parameter [list] must be a valid natural number list with 1 or more elements", list_l)
		FunctionInputError: ('Parameter [list] must be a valid natural number list with 1 or more elements', [])

		Example 3: Invalid Desired Group count
		-------
		>>> t.calc_group_by ([1,2], 4) 
		Traceback (most recent call last):
		FunctionInputError: ('Parameter [Desired Group Count] cannot be more than number of list elements', [1, 2], 4)

		"""

		try:
			#start: parameter validation check
			if len(list_l) < 1:
				raise FunctionInputError ("Parameter [list] must be a valid natural number list with 1 or more elements", list_l)

			if len(list_l) < groupcount_i:
				raise FunctionInputError ('Parameter [Desired Group Count] cannot be more than number of list elements', list_l, groupcount_i)

			#end: parameter validation check

			sorted_pair_a = self.__get_sorted_pair (list_l);
			groups_a, diff_a = self.__get_groups (sorted_pair_a);
			total_group_count_i = len(groups_a);
			current_a = sorted_pair_a[:, 0];#slice to get all current elements
			next_a = sorted_pair_a[:, 1];#slice to get all next elements
			desired_group_diff = groups_a[-groupcount_i];
			groupId_i = 0;
			result_d = {}

			for i in range(0,len(current_a)-1):
				current_item_i = current_a[i]
				next_item_i = next_a[i]
				diff_i = diff_a [i]

				result_d = self.__addResultItem(result_d, groupId_i, current_item_i)

				if diff_i > desired_group_diff:
					groupId_i += 1

				self.__addResultItem (result_d, groupId_i, next_item_i)
				#print(i, current_item_i, next_item_i, diff_i, groupId_i, result_d);
			
			return result_d;

		except (FunctionInputError, ValueError) as error:
			raise;

# end: public methods 

# end of class

if __name__ == "__main__":
	import doctest;
	doctest.testmod(extraglobs= {'t': calc_groupby()});
