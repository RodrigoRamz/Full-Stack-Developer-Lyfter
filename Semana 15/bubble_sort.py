
def bubble_sort_reverse(list): # step 1: How many elements are in the list
    n = len(list)

    for lap in range(n - 1): # step 2: Repeat Laps

        for i in range(n - 1, 0, -1): # step 3: run from left to right

            if list[i] < list[i - 1]: # step 4: compare the actual element with the next one
                list[i], list[i - 1] = list[i - 1], list[i] # step 5: interchange elements if the order is wrong
                