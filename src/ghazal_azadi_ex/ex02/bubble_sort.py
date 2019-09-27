def bubble_sort(my_data):
    my_data = list(my_data)
    # Changing type of data to list which becomes mutable
    dim = len(my_data)
    made_swap = True
    swaps = 0
    while made_swap:
        made_swap = False
        for cnt in range(dim-1):
            if my_data[cnt] > my_data[cnt+1]:
                my_data[cnt], my_data[cnt+1] = my_data[cnt+1], my_data[cnt]
                # Comparing elements and swap them if needed.
                made_swap = True
                swaps = swaps + 1
    return my_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
