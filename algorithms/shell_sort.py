def shell_sort(full_list):

    # Start with a big gap, then reduce the gap
    n = len(full_list)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire full_listay
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = full_list[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and full_list[j - gap] > temp:
                full_list[j] = full_list[j - gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
            full_list[j] = temp
        gap //= 2

    return full_list
