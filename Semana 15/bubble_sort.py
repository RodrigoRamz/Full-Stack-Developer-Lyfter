
def bubble_sort_reverse(list):
    n = len(list)

    for lap in range(n - 1):

        for i in range(n - 1, 0, -1):

            if list[i] < list[i]:
                list[i], list[i - 1] = list[i - 1], list[i]
                