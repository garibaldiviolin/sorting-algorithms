def build_max_heap(full_list, length):

    for i in range(length):

        # if child is bigger than parent
        if full_list[i] > full_list[int((i - 1) / 2)]:
            j = i

            # swap child and parent until
            # parent is smaller
            while full_list[j] > full_list[int((j - 1) / 2)]:
                (full_list[j],
                 full_list[int((j - 1) / 2)]) = (
                    full_list[int((j - 1) / 2)], full_list[j]
                )
                j = int((j - 1) / 2)


def iteractive_heap_sort(full_list, length=None):
    if length is None:
        length = len(full_list)

    build_max_heap(full_list, length)

    for i in range(length - 1, 0, -1):

        # swap value of first indexed
        # with last indexed
        full_list[0], full_list[i] = full_list[i], full_list[0]

        # maintaining heap property
        # after each swapping
        j, index = 0, 0

        while True:
            index = 2 * j + 1

            # if left child is smaller than
            # right child point index variable
            # to right child
            if (index < (i - 1) and full_list[index] < full_list[index + 1]):
                index += 1

            # if parent is smaller than child
            # then swapping parent with child
            # having higher value
            if index < i and full_list[j] < full_list[index]:
                full_list[j], full_list[index] = full_list[index], full_list[j]

            j = index
            if index >= i:
                break

    return full_list
