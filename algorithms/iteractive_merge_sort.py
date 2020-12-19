def iteractive_merge_sort(full_list):
    current_size = 1

    # Outer loop for traversing Each
    # sub array of current_size
    while current_size < len(full_list) - 1:

        left = 0
        # Inner loop for merge call
        # in full_list sub array
        # Each complete Iteration sorts
        # the iterating sub array
        while left < len(full_list) - 1:

            # mid index = left index of
            # sub array + current sub
            # array size - 1
            mid = min((left + current_size - 1), (len(full_list) - 1))

            # (False result,True result)
            # [Condition] Can use current_size
            # if 2 * current_size < len(full_list)-1
            # else len(full_list)-1
            right = (
                (2 * current_size + left - 1, len(full_list) - 1)[
                    2 * current_size + left - 1 > len(full_list) - 1
                ]
            )

            # Merge call for each sub array
            merge(full_list, left, mid, right)
            left = left + current_size * 2

        # Increasing sub array size by
        # multiple of 2
        current_size = 2 * current_size

    return full_list


# Merge Function
def merge(full_list, low, m, r):
    n1 = m - low + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = full_list[low + i]
    for i in range(0, n2):
        R[i] = full_list[m + i + 1]

    i, j, k = 0, 0, low
    while i < n1 and j < n2:
        if L[i] > R[j]:
            full_list[k] = R[j]
            j += 1
        else:
            full_list[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        full_list[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        full_list[k] = R[j]
        j += 1
        k += 1
