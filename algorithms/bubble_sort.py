def bubble_sort(full_list):
    length = len(full_list) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(length):
            if full_list[i] > full_list[i + 1]:
                full_list[i], full_list[i + 1] = full_list[i + 1], full_list[i]
                is_sorted = False
    return full_list
