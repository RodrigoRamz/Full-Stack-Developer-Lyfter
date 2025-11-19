Functions Analysis

print_numbers_times_2 -> O (n)

def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)
		
- Run the list once
- if the list has n elements, for is executed n times
- A cycle depends on the list size then -> O(n)
		
check_if_lists_have_an_equal -> O(n2)

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False

- Two cycles with two list with the same size then -> O(n2)

print_10_or_less_elements -> O(1)

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])
- The number of iterations is limited by a constant (10) then -> O(1) Constant Time
		
generate_list_trios -> O(n3)

def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

- we have 3 list with the same size
- generates all the possible combinations (element_a run all element_b, for each pair element_a, element_b runs all elements_c)

