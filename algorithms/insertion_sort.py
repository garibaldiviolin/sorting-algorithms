def insertion_sort(full_list):

    # Traverse through 1 to len(full_list)
    for i in range(1, len(full_list)):

        key = full_list[i]

        # Move elements of full_list[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < full_list[j]:
            full_list[j + 1] = full_list[j]
            j -= 1
        full_list[j + 1] = key

    return full_list
