def recursive_merge_sort(full_list):
    """
    This algorithm sorts a list of numbers by splitting it into two
    using recursion and until there is only two number in the splitted
    list, and then starts sorting the numbers in the lists (left and
    right).
    """
    if len(full_list) <= 1:
        return

    meio = len(full_list) // 2

    left_list = full_list[:meio]
    right_list = full_list[meio:]

    recursive_merge_sort(left_list)
    recursive_merge_sort(right_list)

    i = 0
    j = 0
    k = 0

    left_list_length = len(left_list)
    right_list_length = len(right_list)

    while i < left_list_length and j < right_list_length:

        if left_list[i] < right_list[j]:
            full_list[k] = left_list[i]
            i += 1
        else:
            full_list[k] = right_list[j]
            j += 1
        k += 1

    while i < left_list_length:

        full_list[k] = left_list[i]
        i += 1
        k += 1

    while j < right_list_length:
        full_list[k] = right_list[j]
        j += 1
        k += 1

    return full_list
