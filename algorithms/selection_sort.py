def selection_sort(full_list):
    for i in range(len(full_list)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(full_list)):
            if full_list[min_idx] > full_list[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        full_list[i], full_list[min_idx] = full_list[min_idx], full_list[i]

    return full_list
