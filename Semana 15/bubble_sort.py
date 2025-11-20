
def bubble_sort_reverse(list): # step 1: How many elements are in the list # O(n2)
    n = len(list) # O(1)

    for lap in range(n - 1): # step 2: Repeat Laps # O(1)

        for i in range(n - 1, lap, -1): # step 3: run from left to right # O(n) #freeze & save comparisons left side is already sorted

            if list[i] < list[i - 1]: # step 4: compare the actual element with the next one # O (1)
                list[i], list[i - 1] = list[i - 1], list[i] # step 5: interchange elements if the order is wrong # O(1)
                changes = True

        if changes: #if there are no changes then the list is already sorted
            break

list = [9, 5, 7, 1, 3]
print("Before:", list)
bubble_sort_reverse(list)
print("After:", list)
