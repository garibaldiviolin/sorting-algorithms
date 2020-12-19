def recursive_quick_sort(full_list, start_list=0, end_list=None):
    if end_list is None:
        end_list = len(full_list) - 1
    if start_list < end_list:
        p = partition(full_list, start_list, end_list)
        recursive_quick_sort(full_list, start_list, p - 1)
        recursive_quick_sort(full_list, p + 1, end_list)
    return full_list


def partition(full_list, start_list, end_list):
    pivot = full_list[end_list]
    i = start_list
    for j in range(start_list, end_list):
        if full_list[j] <= pivot:
            full_list[j], full_list[i] = full_list[i], full_list[j]
            i = i + 1
    full_list[i], full_list[end_list] = full_list[end_list], full_list[i]
    return i
