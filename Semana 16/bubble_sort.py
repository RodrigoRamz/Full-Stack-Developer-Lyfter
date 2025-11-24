
def bubble_sort_reverse(items): 
    if not isinstance(items, list): # step 1: How many elements are in the list # O(n2)   
        raise TypeError("items must be a. list")
    
    n = len(items) # O(1)

    for lap in range(n - 1): # step 2: Repeat Laps # O(1)

        for i in range(n - 1, lap, -1): # step 3: run from left to right # O(n) #freeze & save comparisons left side is already sorted

            if items[i] < items[i - 1]: # step 4: compare the actual element with the next one # O (1)
                items[i], items[i - 1] = items[i - 1], items[i] # step 5: interchange elements if the order is wrong # O(1)
    return items
    
numbers = [9, 5, 7, 1, 3]
print("Before:", numbers)
result = bubble_sort_reverse(numbers)
print("After:", result)

